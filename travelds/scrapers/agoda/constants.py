from typing import Any, Dict


BASE_URL = "https://www.agoda.com/"
CITY_URL = (
    "https://www.agoda.com/api/cronos/search/GetUnifiedSuggestResult/3/1/1/0/en-us/"
)
SEARCH_URL = "https://www.agoda.com/graphql/search"
LISTING_URL = (
    "https://www.agoda.com/api/cronos/property/BelowFoldParams/GetSecondaryData"
)

HEADERS = {
    "authority": "www.agoda.com",
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "ag-page-type-id": "103",
    "ag-debug-override-origin": "PL",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "access-control-max-age": "7200",
    "ag-retry-attempt": "0",
    "content-type": "application/json",
    "accept": "*/*",
    "ag-language-locale": "en-us",
    "ag-request-attempt": "1",
    "dnt": "1",
    "sec-ch-ua": '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    "sec-ch-ua-platform": '"Windows"',
    "origin": "https://www.agoda.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "accept-language": "en-US,en;q=0.9,pl;q=0.8",
}

CITY_PARAMS = {
    "origin": "PL",
    "cid": "-1",
    "pageTypeId": "1",
    "logTypeId": "1",
    "isHotelLandSearch": "true",
}

SEARCH_VARIABLES = {
    "CitySearchRequest": {
        "cityId": None,
        "searchRequest": {
            "searchCriteria": {
                "bookingDate": None,
                "checkInDate": None,
                "localCheckInDate": None,
                "los": 3,
                "rooms": 1,
                "adults": 1,
                "children": 0,
                "childAges": [],
                "ratePlans": [],
                "featureFlagRequest": {
                    "fetchNamesForTealium": True,
                    "fiveStarDealOfTheDay": True,
                    "isAllowBookOnRequest": False,
                    "showUnAvailable": True,
                    "showRemainingProperties": True,
                    "isMultiHotelSearch": False,
                    "enableAgencySupplyForPackages": True,
                    "flags": [
                        {"feature": "FamilyChildFriendlyPopularFilter", "enable": True},
                        {
                            "feature": "FamilyChildFriendlyPropertyTypeFilter",
                            "enable": True,
                        },
                        {"feature": "FamilyMode", "enable": False},
                    ],
                    "enablePriceBreaker": False,
                },
                "isUserLoggedIn": False,
                "currency": None,
                "travellerType": "Couple",
                "isAPSPeek": False,
                "enableOpaqueChannel": False,
                "isEnabledPartnerChannelSelection": None,
                "sorting": {
                    "sortField": "Ranking",
                    "sortOrder": "Desc",
                    "sortParams": None,
                },
                "requiredBasis": "PRPN",
                "requiredPrice": "AllInclusive",
                "suggestionLimit": 0,
                "synchronous": False,
                "supplierPullMetadataRequest": None,
                "isRoomSuggestionRequested": False,
                "isAPORequest": False,
                "hasAPOFilter": False,
                "isAllowBookOnRequest": True,
            },
            "searchContext": {
                "userId": None,
                "memberId": 0,
                "locale": "en-us",
                "cid": 1,
                "origin": "PL",
                "platform": 1,
                "deviceTypeId": 1,
                "experiments": {
                    "forceByVariant": None,
                    "forceByExperiment": [
                        {"id": "FAM-366", "variant": "B"},
                        {"id": "CP-4081", "variant": "B"},
                        {"id": "DRAGON-2308", "variant": "B"},
                        {"id": "MIN-13903-2", "variant": "B"},
                        {"id": "MIN-14036", "variant": "B"},
                        {"id": "UMRAH-B2B", "variant": "B"},
                        {"id": "UMRAH-B2C-REGIONAL", "variant": "B"},
                        {"id": "UMRAH-B2C", "variant": "Z"},
                        {"id": "JGCW-202", "variant": "B"},
                        {"id": "JGCW-204", "variant": "B"},
                        {"id": "JGCW-264", "variant": "B"},
                        {"id": "JGCW-299", "variant": "B"},
                        {"id": "JGCW-159", "variant": "B"},
                        {"id": "FD-3936", "variant": "B"},
                    ],
                },
                "isRetry": False,
                "showCMS": False,
                "storeFrontId": 3,
                "pageTypeId": 103,
                "whiteLabelKey": None,
                "ipAddress": "1",
                "endpointSearchType": "CitySearch",
                "trackSteps": None,
            },
            "matrix": None,
            "matrixGroup": [
                {"matrixGroup": "NumberOfBedrooms", "size": 100},
                {"matrixGroup": "LandmarkIds", "size": 10},
                {"matrixGroup": "AllGuestReviewBreakdown", "size": 100},
                {"matrixGroup": "BusStationLandmarkIds", "size": 20},
                {"matrixGroup": "GroupedBedTypes", "size": 100},
                {"matrixGroup": "RoomBenefits", "size": 100},
                {"matrixGroup": "AtmosphereIds", "size": 100},
                {"matrixGroup": "RoomAmenities", "size": 100},
                {"matrixGroup": "AffordableCategory", "size": 100},
                {"matrixGroup": "HotelFacilities", "size": 100},
                {"matrixGroup": "BeachAccessTypeIds", "size": 100},
                {"matrixGroup": "StarRating", "size": 20},
                {"matrixGroup": "MetroSubwayStationLandmarkIds", "size": 20},
                {"matrixGroup": "CityCenterDistance", "size": 100},
                {"matrixGroup": "ProductType", "size": 100},
                {"matrixGroup": "ThingsToDo", "size": 20},
                {"matrixGroup": "ReviewLocationScore", "size": 3},
                {"matrixGroup": "LandmarkSubTypeCategoryIds", "size": 20},
                {"matrixGroup": "ReviewScore", "size": 100},
                {"matrixGroup": "IsStaycation", "size": 5},
                {"matrixGroup": "AccommodationType", "size": 100},
                {"matrixGroup": "PaymentOptions", "size": 100},
                {"matrixGroup": "TrainStationLandmarkIds", "size": 20},
                {"matrixGroup": "HotelAreaId", "size": 100},
                {"matrixGroup": "HotelChainId", "size": 10},
                {"matrixGroup": "Deals", "size": 100},
            ],
            "filterRequest": {"idsFilters": [], "rangeFilters": [], "textFilters": []},
            "page": {"pageSize": 100, "pageNumber": 1},
            "apoRequest": {"apoPageSize": 10},
            "searchHistory": None,
            "searchDetailRequest": {"priceHistogramBins": 50},
            "isTrimmedResponseRequested": False,
            "featuredAgodaHomesRequest": None,
            "featuredLuxuryHotelsRequest": None,
            "highlyRatedAgodaHomesRequest": {
                "numberOfAgodaHomes": 30,
                "minimumReviewScore": 7.5,
                "minimumReviewCount": 3,
                "accommodationTypes": [
                    28,
                    29,
                    30,
                    102,
                    103,
                    106,
                    107,
                    108,
                    109,
                    110,
                    114,
                    115,
                    120,
                    131,
                ],
                "sortVersion": 0,
            },
            "extraAgodaHomesRequest": None,
            "extraHotels": {"extraHotelIds": [], "enableFiltersForExtraHotels": False},
            "packaging": None,
            "flexibleSearchRequest": None,
        },
    },
    "ContentSummaryRequest": {
        "context": {
            "rawUserId": None,
            "memberId": 0,
            "userOrigin": "PL",
            "locale": "en-us",
            "forceExperimentsByIdNew": [
                {"key": "FAM-366", "value": "B"},
                {"key": "CP-4081", "value": "B"},
                {"key": "DRAGON-2308", "value": "B"},
                {"key": "MIN-13903-2", "value": "B"},
                {"key": "MIN-14036", "value": "B"},
                {"key": "UMRAH-B2B", "value": "B"},
                {"key": "UMRAH-B2C-REGIONAL", "value": "B"},
                {"key": "UMRAH-B2C", "value": "Z"},
                {"key": "JGCW-202", "value": "B"},
                {"key": "JGCW-204", "value": "B"},
                {"key": "JGCW-264", "value": "B"},
                {"key": "JGCW-299", "value": "B"},
                {"key": "JGCW-159", "value": "B"},
                {"key": "FD-3936", "value": "B"},
            ],
            "apo": False,
            "searchCriteria": {"cityId": None},
            "platform": {"id": 1},
            "storeFrontId": 3,
            "cid": "1",
            "occupancy": {
                "numberOfAdults": 1,
                "numberOfChildren": 0,
                "travelerType": 0,
            },
            "deviceTypeId": 1,
            "whiteLabelKey": "",
            "correlationId": "",
        },
        "summary": {"highlightedFeaturesOrderPriority": None, "description": False},
        "reviews": {
            "commentary": None,
            "demographics": {
                "providerIds": None,
                "filter": {"defaultProviderOnly": True},
            },
            "summaries": {
                "providerIds": None,
                "apo": True,
                "limit": 1,
                "travellerType": 3,
            },
            "cumulative": {"providerIds": None},
            "filters": None,
        },
        "images": {
            "page": None,
            "maxWidth": 0,
            "maxHeight": 0,
            "imageSizes": None,
            "indexOffset": None,
        },
        "rooms": {
            "images": None,
            "featureLimit": 0,
            "filterCriteria": None,
            "includeMissing": False,
            "includeSoldOut": False,
            "includeDmcRoomId": False,
            "soldOutRoomCriteria": None,
            "showRoomSize": True,
            "showRoomFacilities": True,
        },
        "nonHotelAccommodation": True,
        "engagement": True,
        "highlights": {
            "maxNumberOfItems": 0,
            "images": {
                "imageSizes": [{"key": "full", "size": {"width": 0, "height": 0}}]
            },
        },
        "personalizedInformation": False,
        "localInformation": {"images": None},
        "features": None,
        "rateCategories": True,
        "contentRateCategories": {"escapeRateCategories": {}},
        "synopsis": True,
    },
    "PricingSummaryRequest": {
        "cheapestOnly": True,
        "context": {
            "abTests": [
                {"testId": 9021, "abUser": "B"},
                {"testId": 9023, "abUser": "B"},
                {"testId": 9024, "abUser": "B"},
                {"testId": 9025, "abUser": "B"},
                {"testId": 9027, "abUser": "B"},
                {"testId": 9029, "abUser": "B"},
            ],
            "clientInfo": {
                "cid": 1,
                "languageId": 1,
                "languageUse": 1,
                "origin": "PL",
                "platform": 1,
                "searchId": "",
                "storefront": 3,
                "userId": None,
                "ipAddress": "1",
            },
            "experiment": [
                {"name": "FAM-366", "variant": "B"},
                {"name": "CP-4081", "variant": "B"},
                {"name": "DRAGON-2308", "variant": "B"},
                {"name": "MIN-13903-2", "variant": "B"},
                {"name": "MIN-14036", "variant": "B"},
                {"name": "UMRAH-B2B", "variant": "B"},
                {"name": "UMRAH-B2C-REGIONAL", "variant": "B"},
                {"name": "UMRAH-B2C", "variant": "Z"},
                {"name": "JGCW-202", "variant": "B"},
                {"name": "JGCW-204", "variant": "B"},
                {"name": "JGCW-264", "variant": "B"},
                {"name": "JGCW-299", "variant": "B"},
                {"name": "JGCW-159", "variant": "B"},
                {"name": "FD-3936", "variant": "B"},
            ],
            "isAllowBookOnRequest": True,
            "isDebug": False,
            "sessionInfo": {"isLogin": False, "memberId": 0, "sessionId": 1},
            "packaging": None,
        },
        "isSSR": True,
        "pricing": {
            "bookingDate": None,
            "checkIn": None,
            "checkout": None,
            "localCheckInDate": None,
            "localCheckoutDate": None,
            "currency": None,
            "details": {
                "cheapestPriceOnly": False,
                "itemBreakdown": False,
                "priceBreakdown": False,
            },
            "featureFlag": [
                "ClientDiscount",
                "PriceHistory",
                "VipPlatinum",
                "CouponSellEx",
                "MixAndSave",
                "APSPeek",
                "StackChannelDiscount",
                "AutoApplyPromos",
                "EnableAgencySupplyForPackages",
                "CreditCardPromotionPeek",
            ],
            "features": {
                "crossOutRate": False,
                "isAPSPeek": False,
                "isAllOcc": False,
                "isApsEnabled": False,
                "isIncludeUsdAndLocalCurrency": False,
                "isMSE": True,
                "isRPM2Included": True,
                "maxSuggestions": 0,
                "newRateModel": False,
                "overrideOccupancy": False,
                "filterCheapestRoomEscapesPackage": False,
                "priusId": 0,
                "synchronous": False,
                "enableEscapesPackage": True,
                "enableRichContentOffer": True,
                "showCouponAmountInUserCurrency": False,
                "calculateRareRoomBadge": False,
            },
            "filters": {
                "cheapestRoomFilters": [],
                "filterAPO": False,
                "ratePlans": [1],
                "secretDealOnly": False,
                "suppliers": [],
                "nosOfBedrooms": [],
            },
            "includedPriceInfo": False,
            "occupancy": {
                "adults": 1,
                "children": 0,
                "childAges": [],
                "rooms": 1,
                "childrenTypes": [],
            },
            "supplierPullMetadata": {"requiredPrecheckAccuracyLevel": 0},
            "mseHotelIds": [],
            "ppLandingHotelIds": [],
            "searchedHotelIds": [],
            "paymentId": -1,
        },
        "suggestedPrice": "AllInclusive",
    },
    "PriceStreamMetaLabRequest": {"attributesId": [8, 1, 18, 7, 11, 2, 3]},
}

LISTING_PARAMS: Dict[str, Any] = {
    "finalPriceView": "2",
    "isShowMobileAppPrice": "false",
    "cid": "-1",
    "numberOfBedrooms": "",
    "familyMode": "false",
    "adults": "1",
    "children": "0",
    "rooms": "1",
    "maxRooms": "0",
    "isCalendarCallout": "false",
    "childAges": "",
    "numberOfGuest": "0",
    "missingChildAges": "false",
    "travellerType": "0",
    "showReviewSubmissionEntry": "false",
    "isFreeOccSearch": "false",
    "isCityHaveAsq": "false",
    "tspTypes": "16",
    "all": "true",
    "price_view": "2",
    "pagetypeid": "7",
}
