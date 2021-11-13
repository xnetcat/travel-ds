from travelds.parsers import parse_ds_arguments
from travelds.constants import PROXIES, SCRAPERS
from travelds.proxies.proxy import ProxyProvider
from travelds.exceptions import *
from travelds import utils
from argparse import Namespace
from typing import List

import logging


def console_entry_point():
    arguments: Namespace = parse_ds_arguments()

    # Set up logging
    logging.basicConfig(
        level=logging.DEBUG if arguments.verbose else logging.INFO,
        format="%(asctime)s :: %(module)s :: [%(levelname)s] %(message)s"
        if arguments.verbose
        else "[%(levelname)s] %(message)s",
    )

    Scraper = SCRAPERS[arguments.scraper]

    proxies: List = []
    for proxy_provider in arguments.proxies:
        provider: ProxyProvider = PROXIES[proxy_provider]()
        provider.load_proxies()
        proxies.extend(provider.proxies)

    if len(arguments.proxies) > 0:
        if len(proxies) == 0:
            raise ProxiesError("No proxies were found, aborting.")

        proxies = [{"https": f"http://{proxy}"} for proxy in proxies]

        if arguments.filter_proxies is True:
            logging.info(f"Found {len(proxies)} proxies. Filtering...")
            proxies = utils.filter_proxies(
                proxies,
                Scraper.test_connection,
                arguments.threads,
                arguments.max_retries,
                arguments.timeout,
            )
            logging.info(f"Found {len(proxies)} working proxies.")
        else:
            logging.info(f"Found {len(proxies)} proxies (unfiltred)")

    scraper = Scraper(
        currency=arguments.currency,
        threads=arguments.threads,
        proxies=proxies,
        timeout=arguments.timeout,
        max_retries=arguments.max_retries,
    )

    listings = scraper.get_all_listings(
        query=arguments.query,
        checkin=arguments.checkin,
        checkout=arguments.checkout,
        type=arguments.location_type,
    )

    print(f"Found {len(listings)} listings.")
