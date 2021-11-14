from travelds.parsers import parse_arguments
from travelds.constants import *
from travelds.exceptions import *
from travelds import utils
from travelds.etl import ETL
from typing import Any, Dict, List, Optional, Tuple, Union

import logging


def console_entry_point():
    """
    Console entry point for the ETL process.
    """

    # Parse the arguments
    arguments = parse_arguments()

    # Set up logging
    logging.basicConfig(
        level=logging.DEBUG if arguments.verbose else logging.INFO,
        format="%(asctime)s :: %(module)s :: [%(levelname)s] %(message)s"
        if arguments.verbose
        else "[%(levelname)s] %(message)s",
    )

    # Set up the Scraper
    Scraper = SCRAPERS[arguments.scraper]

    # Fetch proxies from the provided sites
    proxies: Any = []
    for proxy_provider in arguments.proxies:
        provider = PROXIES[proxy_provider]()
        provider.load_proxies()
        proxies.extend(provider.proxies)

    if len(arguments.proxies) > 0:
        # Convert proxies to a list of dicts
        proxies = [{"https": f"http://{proxy}"} for proxy in proxies]

        # Filter out invalid proxies
        if arguments.filter_proxies is True:
            logging.info(f"Found {len(proxies)} proxies. Filtering...")
            proxies = utils.filter_proxies(
                proxies=proxies,
                func=Scraper.test_connection,
                threads=arguments.threads,
                max_retries=arguments.max_retries,
                timeout=arguments.timeout,
            )
            if len(proxies) == 0:
                raise ProxiesError("No proxies were found, aborting.")
            logging.info(f"Found {len(proxies)} working proxies.")
        else:
            if SCRAPERS[arguments.scraper].requires_credentials:
                raise CredentialsError(
                    "This scraper requires credentials, filter proxies to generate credentials."
                )
            logging.info(f"Found {len(proxies)} proxies (unfiltred)")
            proxies = [(proxy, None) for proxy in proxies]

    # Create the ETL object
    etl = ETL(
        scraper=SCRAPERS[arguments.scraper],
        currency=arguments.currency,
        threads=arguments.threads,
        proxies=None if len(proxies) == 0 else proxies,
        timeout=arguments.timeout,
        max_retries=arguments.max_retries,
    )

    # Run the ETL process
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
