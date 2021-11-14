SEARCH_URL = "https://www.booking.com/searchresults.html"
LOCATION_URL = "https://www.booking.com/autocomplete_csrf"

LOCATION_PARAMS = {
    "lang": "en",
}

CITY_PARAMS = {
    "lang": "en-gb",
            "sb": 1,
            "sb_lp": 1,
            "src": "index",
            "src_elem": "sb",
            "top_ufis": 0,
            "theme_id": 1,
            "theme_source": "index",
            "is_ski_area": 0,
            "dest_type": "city",
            "group_adults": 1,
            "group_children": 0,
            "no_rooms": 0,
            "b_h4u_keep_filters": "",
            "from_sf": "",
            "offset": 0,
            "row": 25,
}

COUNTRY_PARAMS = {
    'dest_type': 'country',
    'dtdisc': ['0'],
    'group_adults': 1,
    'group_children': 0,
    'inac': 0,
    'index_postcard': 0,
    'label_click': ['undef'],
    'lang': 'en-gb',
    'no_rooms': 0,
    'offset': 0,
    'postcard': ['0'],
    'raw_dest_type': 'country',
    'room1': ['A,A'],
    'rows': ['25'],
    'sb_price_type': ['total'],
    'shw_aparth': ['1'],
    'slp_r_match': ['0'],
    'sr_ajax': ['1'],
    'ss_all': ['0'],
    'ssb': ['empty'],
    'b_gtt': 'dLYAeZFVJfNTBBSLFYdRBSHUIfVNVWPCSbBXNET',
    'srpvid': '87687d3a31d50089',
    'top_ufis': 1
}

HEADERS = {
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    "DNT": "1",
    "X-Booking-Language-Code": "en",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
    "Accept": "*/*",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Accept-Language": "en-US;q=0.8,en;q=0.7",
}
