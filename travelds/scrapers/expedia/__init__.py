from travelds.exceptions import LocationError
from travelds.scrapers.expedia.constants import *
from travelds.exceptions import *
from travelds.scrapers.expedia.graphql.search import SEARCH_QUERY
from travelds.scrapers.expedia.graphql.listing import LISTING_QUERY
from travelds.scrapers.scraper import Scraper
from travelds.etl.models import ExpediaListing, ExpediaPrice
from travelds import utils
from datetime import datetime
from typing import Dict, List

import re
import copy
import requests


class Expedia(Scraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        session = requests.session()
        session.get("https://expedia.co.uk/")
        self.duaid = session.cookies.get("DUAID")
        self.batch = 500
        self.Listing = ExpediaListing
        self.Price = ExpediaPrice

    def get_listings(
        self, location: Dict, checkin: str, checkout: str, offset: int
    ) -> List[Dict]:
        checkin_datetime = datetime.strptime(checkin, "%Y-%m-%d")
        checkout_datetime = datetime.strptime(checkout, "%Y-%m-%d")

        search_variables = copy.deepcopy(SEARCH_VARIABLES)
        search_variables["currency"] = self.currency
        search_variables["context"]["identity"]["duaid"] = self.duaid
        search_variables["destination"]["regionName"] = location["regionNames"][
            "displayName"
        ]
        search_variables["destination"]["regionId"] = location["gaiaId"]
        search_variables["destination"]["coordinates"]["latitude"] = float(
            location["coordinates"]["lat"]
        )
        search_variables["destination"]["coordinates"]["longitude"] = float(
            location["coordinates"]["long"]
        )
        search_variables["searchPagination"]["startingIndex"] = offset * 500
        search_variables["dateRange"]["checkInDate"]["day"] = checkin_datetime.day
        search_variables["dateRange"]["checkInDate"]["month"] = checkin_datetime.month
        search_variables["dateRange"]["checkInDate"]["year"] = checkin_datetime.year
        search_variables["dateRange"]["checkOutDate"]["day"] = checkout_datetime.day
        search_variables["dateRange"]["checkOutDate"]["month"] = checkout_datetime.month
        search_variables["dateRange"]["checkOutDate"]["year"] = checkout_datetime.year

        response: Dict = utils.send_request(
            url=BASE_URL,
            method="post",
            proxies=self.proxies,
            headers=HEADERS,
            json={
                "query": SEARCH_QUERY,
                "operationName": "LodgingPwaPropertySearch",
                "variables": search_variables,
            },
            timeout=self.timeout,
            max_retries=self.max_retries,
            transform=lambda x: x.json(),
        )  # type: ignore

        return [
            {
                "id": listing["id"],
                "name": listing["name"],
                "city": location["q"],
                "lat": listing["mapMarker"]["latLong"]["latitude"],
                "lon": listing["mapMarker"]["latLong"]["longitude"],
                "room_and_property_type": "property",
                "url": listing["propertyDetailsLink"]["uri"]["value"],
                "checkin": checkin,
                "checkout": checkout,
                "currency": self.currency,
                "price": float(
                    re.sub(r"[^0-9|\.]", "", listing["price"]["lead"]["formatted"])
                ),
                "available": listing["availability"]["available"],
            }
            for listing in response["data"]["propertySearch"]["propertySearchListings"]
            if listing["__typename"] == "Property"
        ]

    def get_total_count(self, location: Dict, checkin: str, checkout: str) -> int:
        checkin_datetime = datetime.strptime(checkin, "%Y-%m-%d")
        checkout_datetime = datetime.strptime(checkout, "%Y-%m-%d")

        search_variables = copy.deepcopy(SEARCH_VARIABLES)
        search_variables["currency"] = self.currency
        search_variables["context"]["identity"]["duaid"] = self.duaid
        search_variables["destination"]["regionName"] = location["regionNames"][
            "displayName"
        ]
        search_variables["destination"]["regionId"] = location["gaiaId"]
        search_variables["destination"]["coordinates"]["latitude"] = float(
            location["coordinates"]["lat"]
        )
        search_variables["destination"]["coordinates"]["longitude"] = float(
            location["coordinates"]["long"]
        )
        search_variables["searchPagination"]["startingIndex"] = 0
        search_variables["dateRange"]["checkInDate"]["day"] = checkin_datetime.day
        search_variables["dateRange"]["checkInDate"]["month"] = checkin_datetime.month
        search_variables["dateRange"]["checkInDate"]["year"] = checkin_datetime.year
        search_variables["dateRange"]["checkOutDate"]["day"] = checkout_datetime.day
        search_variables["dateRange"]["checkOutDate"]["month"] = checkout_datetime.month
        search_variables["dateRange"]["checkOutDate"]["year"] = checkout_datetime.year

        response: Dict = utils.send_request(
            url=BASE_URL,
            method="post",
            proxies=self.proxies,
            headers=HEADERS,
            json={
                "query": SEARCH_QUERY,
                "operationName": "LodgingPwaPropertySearch",
                "variables": search_variables,
            },
            timeout=self.timeout,
            max_retries=self.max_retries,
            transform=lambda x: x.json(),
        )  # type: ignore

        return response["data"]["propertySearch"]["summary"]["matchedPropertiesSize"]

    def get_listing_data(self, id: int, checkin: str, checkout: str) -> Dict:
        checkin_datetime = datetime.strptime(checkin, "%Y-%m-%d")
        checkout_datetime = datetime.strptime(checkout, "%Y-%m-%d")

        listing_variables = copy.deepcopy(LISTING_VARIABLES)
        listing_variables["currency"] = self.currency
        listing_variables["context"]["identity"]["duaid"] = self.duaid
        listing_variables["propertyId"] = str(id)
        listing_variables["searchCriteria"]["primary"]["dateRange"]["checkInDate"][
            "day"
        ] = checkin_datetime.day
        listing_variables["searchCriteria"]["primary"]["dateRange"]["checkInDate"][
            "month"
        ] = checkin_datetime.month
        listing_variables["searchCriteria"]["primary"]["dateRange"]["checkInDate"][
            "year"
        ] = checkin_datetime.year
        listing_variables["searchCriteria"]["primary"]["dateRange"]["checkOutDate"][
            "day"
        ] = checkout_datetime.day
        listing_variables["searchCriteria"]["primary"]["dateRange"]["checkOutDate"][
            "month"
        ] = checkout_datetime.month
        listing_variables["searchCriteria"]["primary"]["dateRange"]["checkOutDate"][
            "year"
        ] = checkout_datetime.year

        response: Dict = utils.send_request(
            url=BASE_URL,
            method="post",
            proxies=self.proxies,
            headers=HEADERS,
            timeout=self.timeout,
            json={
                "query": LISTING_QUERY,
                "operationName": "PropertyOffers",
                "variables": listing_variables,
            },
            max_retries=self.max_retries,
            transform=lambda x: x.json(),
        )  # type: ignore

        categorized_listings = response["data"]["propertyOffers"]["categorizedListings"]
        for listing in categorized_listings:
            if listing["__typename"] == "LodgingCategorizedUnit":
                price_data = listing["primarySelections"][0]["propertyUnit"][
                    "ratePlans"
                ][0]["priceDetails"][0]
                return {
                    "rate_with_service_fee": price_data["price"]["options"][0][
                        "displayPrice"
                    ]["amount"],
                    "currency": price_data["price"]["options"][0]["displayPrice"][
                        "currencyInfo"
                    ]["code"],
                    "available": price_data["availability"]["available"],
                }

        raise ListingError("Could not find listing data")

    def get_city_data(self, query: str) -> Dict:
        response: Dict = utils.send_request(
            url=CITY_URL + query,
            method="get",
            proxies=self.proxies,
            params=CITY_PARAMS,
            headers=HEADERS,
            data="",
            timeout=self.timeout,
            max_retries=self.max_retries,
            transform=lambda x: x.json(),
        )  # type: ignore

        for result in response["sr"]:
            if result["type"] in ["CITY", "MULTICITY"]:
                result["q"] = query
                return result

        raise LocationError("Invalid country")

    def test_connection(self, proxy, timeout) -> bool:
        return (
            requests.get(
                "https://www.expedia.co.uk/",
                headers=HEADERS,
                proxies=proxy,
                timeout=timeout,
            ).status_code
            == 200
        )
