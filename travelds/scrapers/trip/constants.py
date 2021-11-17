CITY_URL = "https://www.trip.com/restapi/soa2/16709/json/gaHotelSearchEngine"
SEARCH_URL = "https://www.trip.com/restapi/soa2/16709/json/HotelSearch"

# Might have to set P
HEADERS = {
    "cookie": "ibulanguage=PL; ibulocale=pl_pl; cookiePricesDisplayed=PLN",
    "authority": "pl.trip.com",
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    "dnt": "1",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    "content-type": "application/json",
    "accept": "application/json",
    "sec-ch-ua-platform": '"Windows"',
    "origin": "https://pl.trip.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://pl.trip.com/",
    "accept-language": "en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7",
}


"""
to modify
seqid:
- seqid
- Qid
- Head.HotelExtension.Qid

currency:
- filterCondition.priceRange.curr
- Head.currency

page number:
- searchCondition.pageNo

city type:
- searchCondition.optionType

city id:
- searchCondition.optionId
- searchCondition.cityId

city name:
- searchCondition.cityName

check in:
- searchCondition.checkIn

check out:
- searchCondition.checkOut

country id:
- searchCondition.countryId

url:
replace - with / in dates
https://pl.trip.com/hotels/list?
city={cityId}&countryId={countryId}&checkin={checkin}
&checkout={checkout}&optionId={cityId}&optionType={cityType}
&directSearch=0&display={cityType}&crn=1&adult=1&children=0
&searchBoxArg=t&travelPurpose=0&ctm_ref=ix_sb_dl&domestic=0"
- searchCondition.url

client id:
- Head.ClientID
- Head.Frontend.vid

page id:
- Head.PageID

pid:
- Head.HotelExtension.PID

hotel uuid:
- Head.HotelExtension.hotelUuidKey

sessionId:
- Head.Frontend.sessionID

pvid:
- Head.Frontend.pvid

P:
- Head.Frontend.P
"""

SEARCH_JSON = {
    "seqid": None,
    "deduplication": [],
    "filterCondition": {
        "star": [],
        "rate": "",
        "priceRange": {"lowPrice": 0, "highPrice": -1, "curr": None},
        "priceType": 2,
        "breakfast": [],
        "payType": [],
        "bedType": [],
        "bookPolicy": [],
        "bookable": [1],
        "discount": [],
        "zone": [],
        "landmark": [],
        "metro": [],
        "airportTrainstation": [],
        "location": [],
        "cityId": [],
        "amenty": [],
        "category": [],
        "feature": [],
        "brand": [],
        "popularFilters": [],
        "hotArea": [],
    },
    "searchCondition": {
        "sortType": "AppointRank",
        "adult": 1,
        "child": 0,
        "age": "",
        "pageNo": None,
        "optionType": None,
        "optionId": None,
        "lat": 0,
        "destination": "",
        "keyword": "",
        "cityName": None,
        "lng": 0,
        "cityId": None,
        "checkIn": None,
        "checkOut": None,
        "roomNum": 1,
        "mapType": "gg",
        "travelPurpose": 0,
        "countryId": None,
        "url": None,
        "pageSize": 10,
        "timeOffset": 3600,
        "radius": 0,
        "directSearch": 0,
        "signInHotelId": 0,
        "signInType": 0,
    },
    "meta": {
        "fgt": "",
        "hotelId": "",
        "priceToleranceData": "",
        "priceToleranceDataValidationCode": "",
        "mpRoom": [],
        "hotelUniqueKey": "",
        "shoppingid": "",
    },
    "queryTag": "TRIP_RECOMMEND",
    "Qid": None,
    "Head": {
        "Locale": "en-US",
        "Currency": None,
        "AID": "",
        "SID": "",
        "ClientID": None,
        "OUID": "",
        "CAID": "",
        "CSID": "",
        "COUID": "",
        "TimeZone": "1",
        "PageID": None,
        "HotelExtension": {
            "WebpSupport": True,
            "Qid": None,
            "hasAidInUrl": False,
            "group": "TRIP",
            "PID": None,
            "hotelUuidKey": None,
            "hotelUuid": "",
        },
        "Frontend": {"vid": None, "sessionID": None, "pvid": None},
        "P": None,
        "Device": "PC",
        "Version": "0",
    },
}

CITY_JSON = {"searchType": "D"}
