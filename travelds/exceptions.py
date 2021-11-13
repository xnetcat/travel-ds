class ProxiesError(Exception):
    """
    Raised when there is an error with the proxies.
    """

    pass


class LocationError(Exception):
    """
    Raised when there is an error with the location.
    """

    pass


class ScraperError(Exception):
    """
    Raised when there is an error with the scraper.
    """

    pass


class ETLError(Exception):
    """
    Raised when there is an error with the ETL.
    """

    pass


class ListingError(Exception):
    """
    Raised when there is an error with the listing.
    """

    pass

class CredentialsError(Exception):
    """
    Raised when there is an error with the credentials.
    """

    pass