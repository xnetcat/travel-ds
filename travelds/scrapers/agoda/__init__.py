from travelds.scrapers.agoda.graphql import SEARCH_QUERY
from travelds.scrapers.agoda.constants import *
from travelds.exceptions import *
from travelds.scrapers.base import Scraper
from datetime import date 
from typing import Any, Dict, Optional

import copy
import requests
import bs4
import re

class Agoda(Scraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.today = date.today().strftime("%Y-%m-%d") + "T20:00:00.000Z"
        self.headers = HEADERS

    def get_total_count(self, location: Dict, checkin: str, checkout: str) -> int:
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
        ] = 0

        response: Dict = self.send_request(
            url=SEARCH_URL,
            method="post",
            json={
                "operationName": "citySearch",
                "variables": search_variables,
                "query": SEARCH_QUERY,
            },
            transform=lambda x: x.json()
        ) # type: ignore

        return response["data"]["citySearch"]["searchResult"]["searchInfo"][
            "totalFilteredHotels"
        ]

    def get_credentials(self, proxy: Optional[Dict], timeout: int) -> Dict:
        response: str = self.send_request(
            url=BASE_URL,
            proxies=[proxy] if proxy else None,
            transform=lambda x: x.text
        ) # type: ignore

        soup = bs4.BeautifulSoup(response, "html.parser")
        script_tags = soup.find_all("script")
        for script_tag in script_tags:
            if script_tag.string and "agoda.pageConfig" in script_tag.string:
                results = re.search(r"\"userId\":\"([\w-]+)\"", script_tag.string)
                if results is not None:
                    print({"uid": results.group(1)})

        raise CredentialsError("Credentials not found")

    def get_city_data(self, query: str, **creds) -> Dict:
        city_params = copy.deepcopy(CITY_PARAMS)
        city_params["searchText"] = query
        city_params["guild"] = creds["uid"]
        
        response: Dict = self.send_request(
            url=CITY_URL,
            params=city_params,
            transform=lambda x: x.json()
        ) # type: ignore

        view_list = response.get("ViewModelList")
        if view_list is None:
            raise LocationError("City not found")

        for city in view_list:
            if city["SearchType"] == 1:
                return city

        raise LocationError("City not found")

    def test_connection(self, proxy: Dict, timeout: int) -> bool:
        response = requests.get(
            url=BASE_URL,
            headers=self.headers,
            proxies=proxy,
            timeout=timeout
        )

        soup = bs4.BeautifulSoup(response.text, "html.parser")
        script_tags = soup.find_all("script")
        for script_tag in script_tags:
            if script_tag.string and "agoda.pageConfig" in script_tag.string:
                results = re.search(r"\"userId\":\"([\w-]+)\"", script_tag.string)
                if results is not None:
                    return True

        return False