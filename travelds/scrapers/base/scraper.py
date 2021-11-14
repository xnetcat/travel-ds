from typing import Any, List, Dict, Literal, Optional, Tuple
from travelds.exceptions import *
from travelds import utils

import concurrent.futures
import logging


class Scraper:
    requires_credentials = None

    def __init__(
        self,
        currency: str,
        threads: int,
        proxies: List[Tuple[Dict, Optional[Dict]]],
        timeout: int,
        max_retries: int,
    ) -> None:
        self.currency = currency
        self.threads = threads
        self.proxies = proxies
        self.timeout = timeout
        self.max_retries = max_retries
        self.batch_size: Optional[int] = None
        self.Listing = None
        self.Price = None
        self.headers = None
        self.requires_credentials = None

    def get_all_listings(
        self,
        query: str,
        checkin: str,
        checkout: str,
        type: Literal["city", "country", "region"],
    ) -> List[Dict]:
        """
        Get all listings for a given location
        """

        if self.batch_size is None:
            raise ScraperError("Batch size is not set")

        location = self.get_location_data(query, type)
        total_count = self.get_total_count(location, checkin, checkout)
        num_pages = int(total_count / self.batch_size)
        offsets = list(range(num_pages + 1))

        results = []
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=self.threads
        ) as executor:
            future_to_result = {
                executor.submit(
                    self.get_listings, location, checkin, checkout, offset
                ): offset
                for offset in offsets
            }

            for future in concurrent.futures.as_completed(future_to_result):
                offset = future_to_result[future]
                try:
                    result = future.result()
                    results.extend(result)
                except Exception as exc:
                    logging.exception("%r generated an exception: %s" % (offset, exc))

        return results

    def get_listings(
        self, location: Dict[str, Any], checkin: str, checkout: str, offset: int
    ) -> List[Dict]:
        """
        Get listing for a given location/checkin/checkout/offset
        """
        raise NotImplementedError

    def get_total_count(
        self, location: Dict[str, Any], checkin: str, checkout: str
    ) -> int:
        """
        Get total count of listings for a given location/checkin/checkout
        """
        raise NotImplementedError

    def get_listing_data(self, id: int, checkin: str, checkout: str) -> Dict:
        """
        Get listing data for a given listing id/checkin/checkout
        """
        raise NotImplementedError

    def get_location_data(
        self,
        query: str,
        type: Optional[str],
    ) -> Dict:
        """
        Get location data for a given location/type
        """
        try:
            if type == "city":
                return self.get_city_data(query)
            elif type == "country":
                return self.get_country_data(query)
            elif type == "region":
                return self.get_region_data(query)

            raise LocationError("Invalid location type")
        except NotImplementedError:
            raise LocationError("Invalid location type")

    def get_city_data(self, query: str) -> Dict:
        """
        Get city data for a given city
        """
        raise NotImplementedError

    def get_country_data(self, query: str) -> Dict:
        """
        Get country data for a given country
        """
        raise NotImplementedError

    def get_region_data(self, query: str) -> Dict:
        """
        Get region data for a given region
        """
        raise NotImplementedError

    def test_connection(self, proxy: Dict, timeout: int) -> Tuple[bool, Optional[Dict]]:
        """
        Test connection for a given proxy, and return bool and credentials
        """
        raise NotImplementedError

    def send_request(self, **kwargs):
        """
        Send request, use kwargs to overwrite parameters
        """

        return utils.send_request(
            url=kwargs["url"],
            method=kwargs.get("method", "get"),
            params=kwargs.get("params"),
            data=kwargs.get("data"),
            json=kwargs.get("json"),
            transform=kwargs.get("transform"),
            set_credentials=kwargs.get("set_credentials"),
            proxies=kwargs["proxies"] if kwargs.get("proxies") else self.proxies,
            timeout=kwargs["timeout"] if kwargs.get("timeout") else self.timeout,
            max_retries=kwargs["max_retries"]
            if kwargs.get("max_retries")
            else self.max_retries,
            headers=kwargs["headers"] if kwargs.get("headers") else self.headers,
        )
