BASE_URL = "https://www.expedia.co.uk/graphql"
CITY_URL = "https://www.expedia.co.uk/api/v4/typeahead/"

HEADERS = {
    "cookie": "tpid=v.1,3; currency=GBP;",
    "authority": "www.expedia.co.uk",
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "sec-ch-ua": '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    "device-user-agent-id": "3220767a-e5d9-4493-be32-8ac222e3805e",
    "dnt": "1",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "credentials": "same-origin",
    "client-info": "shopping-pwa,unknown,unknown",
    "content-type": "application/json",
    "sec-ch-ua-platform": '"Windows"',
    "x-page-id": "page.Hotel-Search,H,20",
    "accept": "*/*",
    "origin": "https://www.expedia.co.uk",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.expedia.co.uk/Hotel-Search?adults=2&d1=2021-10-01&d2=2021-10-02&destination=Paris%2C%20France&endDate=2021-10-02&latLong=48.86272%2C2.34375&regionId=2734&rooms=1&semdtl=&sort=RECOMMENDED&startDate=2021-10-01&theme=&useRewards=false&userIntent=",
    "accept-language": "en-US,en;q=0.9,pl;q=0.8",
}

CITY_PARAMS = {
    "browser": "Chrome",
    "client": "Homepage",
    "dest": "true",
    "device": "Desktop",
    "expuserid": "-1",
    "features": "ta_hierarchy|postal_code|google|consistent_display",
    "format": "json",
    "guid": "3220767a-e5d9-4493-be32-8ac222e3805e",
    "lob": "HOTELS",
    "locale": "en_GB",
    "maxresults": "8",
    "personalize": "true",
    "regiontype": "2047",
    "siteid": "3",
}

SEARCH_VARIABLES = {
    "context": {
        "siteId": 3,
        "locale": "en_GB",
        "eapid": 0,
        "device": {"type": "DESKTOP"},
        "identity": {
            "expUserId": "-1",
            "tuid": "-1",
            "authState": "ANONYMOUS",
        },
        "privacyTrackingState": "CAN_TRACK",
        "debugContext": {"abacusOverrides": [], "alterMode": "RELEASED"},
    },
    "destination": {
        "coordinates": {
        },
        "pinnedPropertyId": None,
        "propertyIds": None,
        "mapBounds": None,
    },
    "filters": {
        "starList": None,
        "structureTypes": None,
        "propertyName": None,
        "neighborhood": None,
        "mealPlan": None,
        "amenities": None,
        "accessibility": None,
        "travelerType": None,
        "reviewScore": None,
        "poi": None,
        "paymentType": None,
        "cleaningAndSafetyPractices": None,
        "deals": None,
        "propertyStyles": None,
        "rewards": None,
        "bedroomFilter": [],
        "commissionTiers": None,
        "agencyBusinessModels": None,
        "chain": None,
    },
    "legacyCriteria": {
        "sort": "RECOMMENDED",
        "stars": "",
        "priceBuckets": None,
        "amenities": [],
        "structureTypes": [],
        "guestRating": "",
        "paymentType": [],
        "privacyTrackingState": "CAN_TRACK",
    },
    "marketing": {"marketingChannels": [], "marketingPrices": []},
    "rooms": [{"adults": 1, "children": []}],
    "propertyShopOptions": {"points": "SHOP_WITHOUT_POINTS"},
    "shoppingContext": {"multiItem": None},
    "sort": "RECOMMENDED",
    "dateRange": {
        "checkInDate": {},
        "checkOutDate": {},
    },
    "searchPagination": {
        "size": 500,
    },
    "searchIntent": {"semdtl": None, "theme": None, "userIntent": None},
    "shouldFetchSortAndFilter": True,
}

LISTING_VARIABLES = {
    "context": {
        "siteId": 3,
        "locale": "en_GB",
        "eapid": 0,
        "device": {"type": "DESKTOP"},
        "identity": {
            "expUserId": "-1",
            "tuid": "-1",
            "authState": "ANONYMOUS",
        },
        "privacyTrackingState": "CAN_TRACK",
        "debugContext": {
            "abacusOverrides": [],
            "alterMode": "RELEASED",
        },
    },
    "searchCriteria": {
        "primary": {
            "dateRange": {
                "checkInDate": {
                },
                "checkOutDate": {
                },
            },
            "destination": {},
            "rooms": [{"adults": 1, "children": []}],
        },
        "secondary": {
            "counts": [],
            "booleans": [],
            "selections": [
                {"id": "sort", "value": "RECOMMENDED"},
                {"id": "privacyTrackingState", "value": "CAN_TRACK"},
                {"id": "useRewards", "value": "SHOP_WITHOUT_POINTS"},
            ],
        },
    },
    "shoppingContext": {"multiItem": None},
    "referrer": "HSR",
}
