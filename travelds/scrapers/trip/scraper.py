from typing import Dict
from travelds.exceptions import LocationError
from travelds.scrapers.base import Scraper
from travelds.scrapers.trip.constants import *

class Trip(Scraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.headers = HEADERS

    def get_city(self, query: str) -> Dict:
        response: Dict = self.send_request(
            url=CITY_URL,
            method="post",
            json={
                "keyword": query,
                **CITY_JSON
            },
            transform=lambda x: x.json()
        ) # type: ignore

        for result in response["Response"]["searchResults"]:
            if result["type"] in ["IntlCity", "City"]:
                return result

        raise LocationError(f"Could not find city: {query}")
