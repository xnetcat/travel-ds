from argparse import ArgumentParser, Namespace
from travelds.constants import SCRAPERS, PROXIES

def parse_arguments() -> Namespace:
    # Initialize argument parser
    parser = ArgumentParser(
        prog="traveletl",
        description="TravelETL is a command line tool for extracting/transforming data from travel websites.",
    )

    # Scraper options
    parser = _parse_scraper_options(parser)

    # Requests options
    parser = _parse_requests_options(parser)

    # Proxies options
    parser = _parse_proxies_options(parser)

    return parser.parse_args()

def _parse_scraper_options(parser: ArgumentParser) -> ArgumentParser:
    # Website argument
    parser.add_argument(
        "scraper",
        type=str,
        help="The website to scrape data from.",
        choices=SCRAPERS.keys(),
    )

    # Mode
    parser.add_argument(
        "mode",
        type=str,
        help="The mode to use when scraping data.",
        choices=["fetch", "update"],
    )

    # Location
    parser.add_argument(
        "location",
        type=str,
        help="Locations to scrape",
        choices=["cities", "countries", "regions"],
    )

    # Currency argument
    parser.add_argument(
        "--currency",
        type=str,
        help="The currency used when getting price data.",
        default="USD"
    )

    # Verbose
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print verbose messages. Useful for debugging.",
    )

    return parser

def _parse_requests_options(parser: ArgumentParser) -> ArgumentParser:
    # Timeout
    parser.add_argument(
        "--timeout",
        type=int,
        help="Timeout for requests",
        default=10,
    )

    # Max retries
    parser.add_argument(
        "--max-retries",
        type=int,
        help="Max retries for requests",
        default=2,
    )

    # Threads
    parser.add_argument(
        "--threads",
        type=int,
        help="Number of threads to use for requests",
        default=1,
    )

    return parser

def _parse_proxies_options(parser: ArgumentParser) -> ArgumentParser:
    # List of proxies websites to use when scraping data
    parser.add_argument(
        "--proxies",
        type=str,
        help="List of proxies to use when scraping data.",
        nargs="+",
        choices=PROXIES.keys(),
        default=[],
    )

    # Filter proxies
    parser.add_argument(
        "--filter-proxies",
        action="store_true",
        help="Filter out not working proxies",
        default=False,
    )

    return parser

