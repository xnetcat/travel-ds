from travelds.exceptions import LocationError
from travelds.scrapers.scraper import Scraper
from travelds.scrapers.hotels.constants import *
from travelds.scrapers.hotels.graphql.listing import LISTING_QUERY
from travelds.scrapers.hotels.graphql.search import SEARCH_QUERY
from travelds.etl.models import HotelsListing, HotelsPrice
from travelds import utils
from typing import Dict, Optional, List

import json
import copy
import requests
import re
import logging


class Hotels(Scraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        HEADERS["x-currency"] = self.currency
        self.search_query = SEARCH_QUERY
        self.listing_query = LISTING_QUERY
        self.batch = 10
        self.Listing = HotelsListing
        self.Price = HotelsPrice

    def get_listings(
        self, location: Dict, checkin: str, checkout: str, offset: int = 0
    ) -> List[Dict]:
        search_variables = copy.deepcopy(SEARCH_VARIABLES)
        search_variables["sqmState"]["destination"]["id"] = location["destinationId"]
        search_variables["sqmState"]["destination"]["value"] = (
            location.get("name")
            if location.get("name") is not None
            else re.sub(r"<.*?>", r"", location.get("firstLine", ""))
        )
        search_variables["sqmState"]["destination"]["type"] = location["type"]
        search_variables["sqmState"]["destination"]["latitude"] = location["latitude"]
        search_variables["sqmState"]["destination"]["longitude"] = location["longitude"]
        search_variables["sqmState"]["checkIn"] = checkin
        search_variables["sqmState"]["checkOut"] = checkout
        search_variables["pagination"]["pn"] = offset
        search_variables["pagination"]["startIndex"] = (
            (offset * 10) if offset > 0 else 0
        )

        response: Dict = utils.send_request(
            BASE_URL,
            method="post",
            proxies=self.proxies,
            json={
                "operationName": "searchPageQuery",
                "variables": search_variables,
                "query": SEARCH_QUERY,
            },
            headers=HEADERS,
            timeout=self.timeout,
            max_retries=self.max_retries,
            transform=lambda x: x.json(),
        )  # type: ignore

        logging.debug(
            f"{search_variables['sqmState']['destination']['value']} - Finished offset {offset}"
        )

        return [
            {
                "id": int(listing["hotelId"]),
                "name": listing["altText"],
                "city": search_variables["sqmState"]["destination"]["value"],
                "lat": float(listing["coordinate"]["lat"]),
                "lon": float(listing["coordinate"]["lon"]),
                "room_and_property_type": None,
                "url": f"https://uk.hotels.com/ho{listing['hotelId']}/",
                "rate_with_service_fee": None
                if listing["ratePlan"]["price"]["exactCurrent"] == 0
                else listing["ratePlan"]["price"]["exactCurrent"],
                "currency": self.currency,
                "available": listing["ratePlan"]["price"]["exactCurrent"] == 0,
                "checkin": checkin,
                "checkout": checkout,
            }
            for listing in response["data"]["searchPage"]["body"]["searchResults"][
                "results"
            ]
        ]

    def get_listing_data(self, id: int, checkin: str, checkout: str) -> Optional[Dict]:
        listing_variables = copy.deepcopy(LISTING_VARIABLES)
        listing_variables["sqmState"]["destination"]["id"] = str(id)
        listing_variables["sqmState"]["checkIn"] = checkin
        listing_variables["sqmState"]["checkOut"] = checkout

        response: Dict = utils.send_request(
            BASE_URL,
            method="post",
            proxies=self.proxies,
            json={
                "operationName": "propertyPageQuery",
                "variables": listing_variables,
                "query": LISTING_QUERY,
            },
            headers=HEADERS,
            timeout=self.timeout,
            max_retries=self.max_retries,
            transform=lambda x: x.json(),
        )  # type: ignore

        body = None
        price = None
        num_rooms = None
        country = None
        is_multiple = None
        try:
            body = response["data"]["propertyPage"]["body"]
            is_multiple = len(body["roomsAndRates"]["groups"]["base"]["rooms"]) > 1
            price = float(body["featuredPrice"]["currentPrice"]["plain"])
            country = body["propertyDescription"]["address"]["countryName"]
            entry = body["atAGlance"]["keyFacts"]["hotelSize"][0]
            m1 = re.match(r"^This hotel has (\d+) rooms$", entry)
            m2 = re.match(r"^(\d+) rooms$", entry)
            if m1:
                num_rooms = int(m1.groups()[0])
            elif m2:
                num_rooms = int(m2.groups()[0])
        except Exception:
            pass

        return {
            "rate_with_service_fee": (price if price and price > 0 else None),
            "available": (True if price and price > 0 else False),
            "is_bookable": body["unavailable"]["isStopSell"] is None if body else None,
            "currency": self.currency,
            "num_rooms": num_rooms if num_rooms is not None else None,
            "hotel_stars": body["propertyDescription"]["starRating"]
            if body is not None
            else None,
            "country": country,
            "is_multiple": is_multiple,
        }

    def get_total_count(self, location: Dict, checkin: str, checkout: str) -> int:
        search_variables = copy.deepcopy(SEARCH_VARIABLES)
        search_variables["sqmState"]["destination"]["id"] = location["destinationId"]
        search_variables["sqmState"]["destination"]["value"] = (
            location.get("name")
            if location.get("name") is not None
            else re.sub(r"<.*?>", r"", location.get("firstLine", ""))
        )
        search_variables["sqmState"]["destination"]["type"] = location["type"]
        search_variables["sqmState"]["destination"]["latitude"] = location["latitude"]
        search_variables["sqmState"]["destination"]["longitude"] = location["longitude"]
        search_variables["sqmState"]["checkIn"] = checkin
        search_variables["sqmState"]["checkOut"] = checkout
        search_variables["pagination"]["pn"] = 0
        search_variables["pagination"]["startIndex"] = 0
        response: Dict = utils.send_request(
            url=BASE_URL,
            method="post",
            proxies=self.proxies,
            json={
                "operationName": "searchPageQuery",
                "variables": search_variables,
                "query": SEARCH_QUERY,
            },
            headers=HEADERS,
            timeout=self.timeout,
            max_retries=self.max_retries,
            transform=lambda x: x.json(),
        )  # type: ignore

        total_count = response["data"]["searchPage"]["body"]["searchResults"][
            "totalCount"
        ]
        return 840 if total_count > 840 else total_count

    def test_connection(self, proxy: Dict = None, timeout: int = 10) -> bool:
        return (
            requests.get(
                "https://www.hotels.com/",
                proxies=proxy,
                timeout=timeout,
            ).status_code
            == 200
        )

    def get_city_data(self, query: str) -> Optional[Dict]:
        params = copy.deepcopy(CITY_PARAMS)
        params["query"] = query
        params["currency"] = self.currency

        response: Dict = utils.send_request(
            url=COUNTRY_URL,
            method="get",
            proxies=self.proxies,
            params=params,
            headers=HEADERS,
            timeout=self.timeout,
            max_retries=self.max_retries,
            transform=lambda x: x.json(),
        )  # type: ignore

        for suggestion in response["suggestions"]:
            if suggestion["group"] == "CITY_GROUP":
                for city in suggestion["entities"]:
                    if city["type"] == "CITY":
                        return city

        raise LocationError("Invalid city")

    def get_country_data(self, query: str) -> Optional[Dict]:
        params = copy.deepcopy(COUNTRY_PARAMS)
        params["query"] = query
        params["currency"] = self.currency

        response: Dict = utils.send_request(
            url=COUNTRY_URL,
            method="get",
            proxies=self.proxies,
            params=params,
            headers=HEADERS,
            timeout=self.timeout,
            max_retries=self.max_retries,
            transform=lambda x: json.loads(x.text.split("(", 1)[1].rsplit(")", 1)[0]),
        )  # type: ignore

        for suggestion in response["suggestions"]:
            if suggestion["type"] in ["COUNTRY", "STATE"]:
                return suggestion

        raise LocationError("Invalid country")
