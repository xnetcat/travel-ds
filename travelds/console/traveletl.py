from travelds.parsers import parse_etl_arguments
from travelds.constants import *
from travelds.exceptions import *
from travelds import utils
from travelds.etl import ETL
from typing import List

import logging


def console_entry_point():
    
    arguments = parse_etl_arguments()

    # Set up logging
    logging.basicConfig(
        level=logging.DEBUG if arguments.verbose else logging.INFO,
        format="%(asctime)s :: %(module)s :: [%(levelname)s] %(message)s"
        if arguments.verbose
        else "[%(levelname)s] %(message)s",
    )

    Scraper = SCRAPERS[arguments.scraper]

    proxies: List = []
    if len(arguments.proxies) > 0:
        if len(proxies) == 0:
            raise ProxiesError("No proxies were found, aborting.")

        proxies = [
            {"https": f"http://{proxy}"} for proxy in proxies
        ]

        if arguments.filter_proxies is True:
            logging.info(f"Found {len(proxies)} proxies. Filtering...")
            proxies = utils.filter_proxies(
                proxies, 
                Scraper.test_connection, 
                arguments.threads,
                arguments.max_retries,
                arguments.timeout
            )
            logging.info(f"Found {len(proxies)} working proxies.")
        else:
            logging.info(f"Found {len(proxies)} proxies (unfiltred)")

    etl = ETL(
        scraper=SCRAPERS[arguments.scraper],
        currency=arguments.currency,
        threads=arguments.threads,
        proxies=proxies,
        timeout=arguments.timeout,
        max_retries=arguments.max_retries,
    )

    if arguments.mode == "fetch":
        if arguments.location == "cities":
            logging.info("Fetching cities...")
            etl.fetch_listings(CITIES, "city")
        elif arguments.location == "countries":
            logging.info("Fetching countries...")
            etl.fetch_listings(COUNTRIES, "country")
        elif arguments.location == "regions":
            logging.info("Fetching regions...")
            etl.fetch_listings(REGIONS, "region")
    elif arguments.mode == "update":
        if arguments.location == "cities":
            logging.info("Updating cities...")
            etl.update_listings(CITIES)
        elif arguments.location == "countries":
            logging.info("Updating countries...")
            etl.update_listings(COUNTRIES)
        elif arguments.location == "regions":
            logging.info("Updating regions...")
            etl.update_listings(REGIONS)
    