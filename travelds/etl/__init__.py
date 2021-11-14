import logging

from typing import Callable, List, Dict, Optional, Tuple
from travelds import utils

import concurrent.futures
import datetime


class ETL:
    def __init__(
        self,
        scraper: Callable,
        currency: str = "USD",
        threads: int = 1,
        proxies: List[Tuple[Dict, Optional[Dict]]] = None,
        timeout: int = 5,
        max_retries: int = 1,
    ) -> None:
        self.scraper = scraper(
            currency=currency,
            threads=threads,
            proxies=proxies,
            timeout=timeout,
            max_retries=max_retries,
        )
        self.currency = currency
        self.threads = threads
        self.proxies = proxies
        self.timeout = timeout
        self.max_retries = max_retries

    def fetch_listings(self, locations, type):
        dates_matrix = []
        for city in locations:
            for checkin, checkout in utils.get_dates():
                dates_matrix.append(
                    (city, checkin.strftime("%Y-%m-%d"), checkout.strftime("%Y-%m-%d"))
                )

        with concurrent.futures.ThreadPoolExecutor(
            max_workers=self.threads
        ) as executor:
            future_to_date_data = {
                executor.submit(
                    self.scraper.get_all_listings,
                    date_data[0],
                    date_data[1],
                    date_data[2],
                    type,
                ): date_data
                for date_data in dates_matrix
            }
            for future in concurrent.futures.as_completed(future_to_date_data):
                date_data = future_to_date_data[future]
                try:
                    results = future.result()
                except Exception as exc:
                    logging.error(
                        f"{date_data[0]} {date_data[1]}/{date_data[2]} generated an exception"
                    )
                    logging.error(exc)
                else:
                    logging.info(
                        f"Finished {date_data[0]} {date_data[1]}/{date_data[2]} - {len(results)} results"
                    )
                    for result in results:
                        try:
                            self.add_listing(result)
                        except Exception as e:
                            logging.error(f"Error adding listing {result['id']}")
                            logging.error(e)

    def add_price(self, listing, checkin, checkout):
        price_data = self.scraper.get_listing_data(
            listing.code,
            checkin.strftime("%Y-%m-%d"),
            checkout.strftime("%Y-%m-%d"),
        )
        self.scraper.Price.objects.create(
            listing=listing,
            start_date=checkin,
            end_date=checkout,
            ref_period=datetime.date.today(),
            rate_with_service_fee=price_data.get("rate_with_service_fee", None),
            currency=price_data.get("currency", None),
            available=price_data.get("available", None),
            room_count=price_data.get("room_count", None),
        )

    def update_listings(self, cities):
        dates_matrix = []
        for city in cities:
            listings = self.scraper.Listing.objects.filter(city=city)
            if listings.count() == 0:
                continue

            for listing in listings:
                if (
                    self.scraper.Price.objects.filter(
                        listing=listing, ref_period=datetime.date.today()
                    ).count()
                    > 0
                ):
                    continue

                for checkin, checkout in utils.get_dates():
                    dates_matrix.append((listing, checkin, checkout))

        with concurrent.futures.ThreadPoolExecutor(
            max_workers=self.threads
        ) as executor:
            for listing, checkin, checkout in dates_matrix:
                for listing, checkin, checkout in dates_matrix:
                    executor.submit(self.add_price, listing, checkin, checkout)

    def add_listing(self, result):
        listing, created = self.scraper.Listing.objects.get_or_create(code=result["id"])

        is_tracked = int(result["id"]) % 16 <= 1
        listing.is_tracked = is_tracked
        listing.first_seen = listing.first_seen or datetime.date.today()
        listing.last_seen = datetime.date.today()
        listing.save()

        if created is True:
            self.scraper.Listing.objects.filter(id=listing.id).update(
                name=result.get("name", None),
                city=result.get("city", None),
                lat=result.get("lat", None),
                lon=result.get("lon", None),
                room_and_property_type=result.get("room_and_property_type", None),
                url=result.get("url", None),
                hotel_chain=result.get("hotel_chain", None),
                wiki_entity=result.get("wiki_entity", None),
                num_rooms=result.get("num_rooms", None),
                country_name=result.get("country_name", None),
                hotel_stars=result.get("hotel_stars", None),
                is_multiple=result.get("is_multiple", None),
            )
