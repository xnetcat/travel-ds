from datetime import datetime, timedelta
from travelds.exceptions import LocationError, ScraperError
from travelds.scrapers.base import Scraper
from travelds.scrapers.booking.constants import *
from typing import Dict, Optional, Tuple
from bs4 import BeautifulSoup

import re
import copy
import requests

from travelds.utils import update


class Booking(Scraper):
    requires_credentials = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.creds = self.get_credentials(None, self.timeout)

    def get_city_data(self, query: str) -> Dict:
        params = copy.deepcopy(LOCATION_PARAMS)
        city_params = copy.deepcopy(CITY_PARAMS)
        city_params["selected_currency"] = self.currency
        if self.creds:
            params["aid"] = self.creds["aid"]
            params["term"] = query
            city_params["label"] = self.creds["label"]
            city_params["sid"] = self.creds["sid"]

        response: Dict = self.send_request(
            url=LOCATION_URL,
            method="get",
            params=params,
            transform=lambda x: x.json(),
            headers=self.creds["headers"] if self.creds else None,
            cookies=self.creds["cookies"] if self.creds else None,
            set_credentials=lambda creds, headers, _json, params, cookies: update(
                params, {"aid": creds["aid"], "term": query}
            )
            and update(headers, creds["headers"])
            and update(cookies, creds["cookies"])
            if self.proxies
            else None,
        )  # type: ignore

        results = response["city"]
        for result in results:
            if result["dest_type"] == "city":
                city_params["ss"] = result["city_name"]
                city_params["ssne"] = result["city_name"]
                city_params["ssne_untouched"] = result["city_name"]
                city_params["dest_id"] = result["dest_id"]
                result["params"] = city_params
                return result

        raise LocationError(f"No city found for query: {query}")

    def get_country_data(self, query: str) -> Dict:
        params = copy.deepcopy(LOCATION_PARAMS)
        country_params = copy.deepcopy(COUNTRY_PARAMS)
        country_params["selected_currency"] = self.currency
        if self.creds:
            params["aid"] = self.creds["aid"]
            params["term"] = query
            today = datetime.today()
            tomorrow = today + timedelta(days=2)
            country_params["checkin_year"] = (today.year,)
            country_params["checkin_month"] = (today.month,)
            country_params["checkin_monthday"] = (today.day,)
            country_params["checkout_year"] = (tomorrow.year,)
            country_params["checkout_month"] = (tomorrow.month,)
            country_params["checkout_monthday"] = (tomorrow.day,)
            country_params["sid"] = self.creds["sid"]
            country_params["label:"] = self.creds["label"]

        response: Dict = self.send_request(
            url=LOCATION_URL,
            method="get",
            params=params,
            transform=lambda x: x.json(),
            headers=self.creds["headers"] if self.creds else None,
            cookies=self.creds["cookies"] if self.creds else None,
            set_credentials=(
                lambda creds, headers, _json, params, cookies: update(
                    params, {"aid": creds["aid"], "term": query}
                )
                and update(headers, creds["headers"])
                and update(cookies, creds["cookies"])
            )
            if self.proxies
            else None,
        )  # type: ignore

        results = response["city"]
        for result in results:
            if result["dest_type"] == "country":
                country_params["ss"] = result["country_name"]
                country_params["dest_id"] = result["dest_id"]
                del country_params["checkin_year"]
                del country_params["checkin_month"]
                del country_params["checkin_monthday"]
                del country_params["checkout_year"]
                del country_params["checkout_month"]
                del country_params["checkout_monthday"]
                result["params"] = country_params
                return result

        raise LocationError(f"No country found for query: {query}")

    def get_credentials(self, proxy: Optional[Dict], timeout: int) -> Dict:
        session = requests.session()

        resp = session.get(
            "https://www.booking.com", headers=HEADERS, proxies=proxy, timeout=timeout
        )

        soup = BeautifulSoup(resp.text, "html5lib")
        scripts = soup.find_all("script")  # type: ignore
        if scripts is None:
            raise ValueError("Couldn't find script tags")

        script_text = None
        for script in scripts:
            if script.find(text=True) is None:  # type: ignore
                continue  # type: ignore
            if "ajaxHeaders" in script.find(  # type: ignore
                text=True
            ) and "X-Booking-CSRF" in script.find(  # type: ignore
                text=True
            ):
                script_text = script.find(text=True)  # type: ignore

        if script_text is None:
            raise ScraperError("Couldn't find script tag")

        data = {
            "bkng": session.cookies["bkng"],
            "headers": {
                "Connection": "keep-alive",
                "Pragma": "no-cache",
                "Cache-Control": "no-cache",
                "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                "DNT": "1",
                "X-Booking-Language-Code": "en",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
                "Accept": "*/*",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Accept-Language": "en-US;q=0.8,en;q=0.7",
            },
            "cookies": {"bkng": session.cookies["bkng"]},
        }

        for col, attr in [
            ("X-Booking-AID", "aid"),
            ("X-Booking-CSRF", "bkng_csrf"),
            ("X-Booking-Pageview-Id", "pageview_id"),
            ("X-Booking-Session-Id", "sid"),
        ]:
            data[attr] = re.match(
                r".*?" + col + r"\': \'([^\']*)\'.*$",
                script_text,
                flags=re.I | re.DOTALL,
            ).groups()[
                0
            ]  # type: ignore

        data["headers"]["X-Booking-CSRF"] = data["bkng_csrf"]
        data["label"] = re.match(
            r".*?X-Booking-Label\': encodeURIComponent\(\'([^\']*)\'\).*$",
            script_text,
            flags=re.I | re.DOTALL,
        ).groups()[
            0
        ]  # type: ignore
        for key in data.keys():
            if data[key] is None:
                raise ScraperError("Couldn't find {}".format(key))

        return data

    def test_connection(self, proxy: Dict, timeout: int) -> Tuple[bool, Optional[Dict]]:
        try:
            creds = self.get_credentials(proxy, timeout)
        except ScraperError:
            return False, None
        else:
            return True, creds


if __name__ == "__main__":
    scraper = Booking("USD", 1, None, 5, 1)
    scraper.get_country_data("Poland")
