import logging
from travelds.scrapers.agoda.graphql import SEARCH_QUERY
from travelds.scrapers.agoda.constants import *
from travelds.scrapers.base import Scraper
from travelds.etl.models import AgodaListing, AgodaPrice
from travelds.exceptions import *
from travelds.utils import update
from datetime import date, datetime
from typing import Any, Dict, List, Optional, Tuple

import copy
import requests
import bs4
import re


class Agoda(Scraper):
    requires_credentials = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.today = date.today().strftime("%Y-%m-%d") + "T20:00:00.000Z"
        self.batch_size = 100
        self.headers = HEADERS
        self.Listing = AgodaListing
        self.Price = AgodaPrice

        credentials = self.get_credentials(None, self.timeout)
        if credentials is None:
            raise CredentialsError("Credentials not found")

        self.uid = credentials["uid"]

    def get_listings(
        self, location: Dict, checkin: str, checkout: str, offset: int
    ) -> List[Dict]:
        response = self.send_listings_request(location, checkin, checkout, offset)

        logging.debug(
            f'Finished offset {offset} {location["Name"]} {checkin}/{checkout}'
        )

        listings: List[Dict] = []
        for listing in response["data"]["citySearch"]["properties"]:
            content = listing["content"]

            if listing["pricing"]["offers"] == []:
                available = False
                price = None
            else:
                pricing = listing["pricing"]["offers"][0]["roomOffers"][0]["room"][
                    "pricing"
                ][0]
                available = listing["pricing"]["isAvailable"]
                price = pricing["price"]["perNight"]["exclusive"]["display"]

            listings.append(
                {
                    "id": listing["propertyId"],
                    "name": content["informationSummary"]["displayName"],
                    "city": location["Name"],
                    "lat": content["informationSummary"]["geoInfo"]["latitude"],
                    "lon": content["informationSummary"]["geoInfo"]["longitude"],
                    "room_and_property_type": content["informationSummary"][
                        "propertyType"
                    ],
                    "url": "https://www.agoda.com"
                    + content["informationSummary"]["propertyLinks"]["propertyPage"]
                    if content["informationSummary"]["propertyLinks"]
                    else None,
                    "rate_with_service_fee": price,
                    "currency": self.currency,
                    "available": available,
                    "checkin": checkin,
                    "checkout": checkout,
                    "country_name": content["informationSummary"]["address"]["country"][
                        "name"
                    ],
                    "hotel_stars": int(content["reviews"]["cumulative"]["score"])
                    if content["reviews"]["cumulative"]
                    else None,
                }
            )

        return listings

    def get_listing_data(self, id: int, checkin: str, checkout: str) -> Dict:
        checkin_datetime = datetime.strptime(checkin, "%Y-%m-%d")
        checkout_datetime = datetime.strptime(checkout, "%Y-%m-%d")
        time_of_stay = (checkout_datetime - checkin_datetime).days

        listing_params = copy.deepcopy(LISTING_PARAMS)
        listing_params["checkIn"] = checkin
        listing_params["currencyCode"] = self.currency
        listing_params["los"] = time_of_stay
        listing_params["hotel_id"] = str(id)

        response: Dict = self.send_request(
            url=LISTING_URL,
            params=listing_params,
            transform=lambda x: x.json(),
        )  # type: ignore

        price = float(response["inquiryProperty"]["cheapestPrice"])
        return {
            "rate_with_service_fee": price if price > 0 else None,
            "available": True if price > 0 else False,
            "currency": self.currency,
            "room_count": response["numberOfFitRoom"] + response["numberOfNotFitRoom"],
        }

    def get_total_count(self, location: Dict, checkin: str, checkout: str) -> int:
        response = self.send_listings_request(location, checkin, checkout, 0)

        return response["data"]["citySearch"]["searchResult"]["searchInfo"][
            "totalFilteredHotels"
        ]

    def send_listings_request(
        self, location: Dict, checkin: str, checkout: str, offset: int
    ) -> Dict:
        search_variables: Dict[str, Any] = copy.deepcopy(SEARCH_VARIABLES)
        search_variables["ContentSummaryRequest"]["context"]["searchCriteria"][
            "cityId"
        ] = location["CityId"]
        search_variables["CitySearchRequest"]["cityId"] = location["CityId"]

        search_variables["PricingSummaryRequest"]["pricing"][
            "localCheckInDate"
        ] = checkin
        search_variables["PricingSummaryRequest"]["pricing"]["checkIn"] = (
            checkin + "T20:00:00.000Z"
        )
        search_variables["CitySearchRequest"]["searchRequest"]["searchCriteria"][
            "localCheckInDate"
        ] = checkin
        search_variables["CitySearchRequest"]["searchRequest"]["searchCriteria"][
            "checkInDate"
        ] = (checkin + "T20:00:00.000Z")

        search_variables["PricingSummaryRequest"]["pricing"][
            "localCheckOutDate"
        ] = checkout
        search_variables["PricingSummaryRequest"]["pricing"]["checkout"] = (
            checkout + "T11:00:00.000Z"
        )

        search_variables["PricingSummaryRequest"]["pricing"]["bookingDate"] = self.today
        search_variables["CitySearchRequest"]["searchRequest"]["searchCriteria"][
            "bookingDate"
        ] = self.today

        search_variables["PricingSummaryRequest"]["pricing"]["currency"] = self.currency
        search_variables["CitySearchRequest"]["searchRequest"]["searchCriteria"][
            "currency"
        ] = self.currency

        search_variables["CitySearchRequest"]["searchRequest"]["page"][
            "pageNumber"
        ] = offset

        if not self.proxies:
            search_variables["PricingSummaryRequest"]["context"]["clientInfo"][
                "userId"
            ] = self.uid
            search_variables["CitySearchRequest"]["searchRequest"]["searchContext"][
                "userId"
            ] = self.uid
            search_variables["ContentSummaryRequest"]["context"]["rawUserId"] = self.uid

        response: Dict = self.send_request(
            url=SEARCH_URL,
            method="post",
            json={
                "operationName": "citySearch",
                "variables": search_variables,
                "query": SEARCH_QUERY,
            },
            set_credentials=lambda credits, _headers, json, _params, _cookies: update(
                json,
                {
                    "variables": {
                        "PricingSummaryRequest": {
                            "context": {"clientInfo": {"userId": credits}}
                        },
                        "CitySearchRequest": {
                            "searchRequest": {"searchContext": {"userId": credits}}
                        },
                        "ContentSummaryRequest": {"context": {"rawUserId": credits}},
                    }
                },
            )
            if self.proxies
            else None,
            transform=lambda x: x.json(),
        )  # type: ignore

        return response

    def get_city_data(self, query: str) -> Dict:
        city_params = copy.deepcopy(CITY_PARAMS)
        city_params["searchText"] = query

        response: Dict = self.send_request(
            url=CITY_URL, params=city_params, transform=lambda x: x.json()
        )  # type: ignore

        view_list = response.get("ViewModelList")
        if view_list is None:
            raise LocationError(f"Could not find city: {query}")

        for city in view_list:
            if city["SearchType"] == 1:
                return city

        raise LocationError(f"Could not find city: {query}")

    def get_credentials(self, proxy: Optional[Dict], timeout: int) -> Optional[Dict]:
        response = requests.get(
            url=BASE_URL, headers=self.headers, proxies=proxy, timeout=timeout
        )

        soup = bs4.BeautifulSoup(response.text, "html.parser")
        script_tags = soup.find_all("script")
        for script_tag in script_tags:
            if script_tag.string and "agoda.pageConfig" in script_tag.string:
                results = re.search(r"\"userId\":\"([\w-]+)\"", script_tag.string)
                if results is not None:
                    return {"uid": results.group(1)}

        return None

    def test_connection(self, proxy: Dict, timeout: int) -> Tuple[bool, Optional[Dict]]:
        response = requests.get(
            url=BASE_URL, headers=HEADERS, proxies=proxy, timeout=timeout
        )

        soup = bs4.BeautifulSoup(response.text, "html.parser")
        script_tags = soup.find_all("script")
        for script_tag in script_tags:
            if script_tag.string and "agoda.pageConfig" in script_tag.string:
                results = re.search(r"\"userId\":\"([\w-]+)\"", script_tag.string)
                if results is not None:
                    return True, {"uid": results.group(1)}

        return False, None
