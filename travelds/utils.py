from typing import Callable, List, Dict, Optional, Tuple, Union
from datetime import date, timedelta
from dateutil import relativedelta
from dateutil._common import weekday
from itertools import cycle
from travelds.exceptions import *

import concurrent.futures
import collections.abc
import requests
import random


def split_list(l: List, n: int) -> List[List]:
    """
    Split List into n chunks
    """

    avg = len(l) / float(n)
    new_list = []
    last = 0.0

    while last < len(l):
        new_list.append(l[int(last) : int(last + avg)])
        last += avg

    return new_list


def update(d: Optional[Dict], u: Dict):
    """
    Nested dict update
    """
    if d is None:
        d = {}

    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = update(d.get(k, {}), v)  # type: ignore
        else:
            d[k] = v
    return d


def get_next_weekday(startdate: date, weekday: weekday, weeks: int = None) -> date:
    """
    Get next weekday for date object
    """

    rd = relativedelta.relativedelta(days=1, weekday=weekday, weeks=weeks)

    next_day = startdate + rd

    return next_day


def get_dates() -> List[Tuple[date, date]]:
    """
    Get dates for FRIDAY/SUNDAY, MONDAY/WENSDAY for current/next week/3 weeks
    """

    dates = [
        (
            date.today() + timedelta(days=1),
            date.today() + timedelta(days=2),
        )
    ]
    for i in [1, 3]:
        dates.append(
            (
                get_next_weekday(date.today(), relativedelta.FR, i),
                get_next_weekday(
                    get_next_weekday(date.today(), relativedelta.FR, i),
                    relativedelta.SU,
                    0,
                ),
            )
        )
        dates.append(
            (
                get_next_weekday(date.today(), relativedelta.MO, i),
                get_next_weekday(
                    get_next_weekday(date.today(), relativedelta.MO, i),
                    relativedelta.WE,
                    0,
                ),
            )
        )

    return dates


def test_proxy(
    proxy: Dict, func: Callable, max_retries: int, timeout: int = 5
) -> Tuple[bool, Optional[Dict]]:
    """
    Test proxy using provided function
    """

    retries = 0
    while retries < max_retries:
        try:
            works, creds = func(None, proxy=proxy, timeout=timeout)
        except Exception:
            retries += 1
        else:
            return works, creds

    return False, None


def filter_proxies(
    proxies: List[Dict],
    func: Callable,
    threads: int = 1,
    max_retries: int = 1,
    timeout: int = 5,
) -> List[Tuple[Dict, Optional[Dict]]]:
    """
    Filter proxies using provided function
    """

    working_proxies: List[Tuple[Dict, Optional[Dict]]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        future_to_proxy = {
            executor.submit(test_proxy, proxy, func, max_retries, timeout): proxy
            for proxy in proxies
        }

        for future in concurrent.futures.as_completed(future_to_proxy):
            proxy = future_to_proxy[future]
            working_proxy, creds = future.result()
            if working_proxy is True:
                working_proxies.append((proxy, creds))

    return working_proxies


def send_request(
    url: str,
    method: str = "get",
    proxies: List[Tuple[Dict, Optional[Dict]]] = None,
    params: Dict = None,
    headers: Dict = None,
    data: str = None,
    json: Dict = None,
    timeout: int = None,
    max_retries: int = 1,
    cookies: Dict = None,
    transform: Callable = None,
    set_credentials: Callable = None,
):
    """
    Send request to url, will fail if we ran out of proxies
    """

    if proxies and len(proxies) > 0:
        random.shuffle(proxies)
        proxy_cycle = cycle(proxies)
        proxy = next(proxy_cycle)
        start_proxy = proxy
        retries = 0

        while True:
            try:
                if proxy[1] and set_credentials:
                    set_credentials(proxy[1], headers, json, params, cookies)
                response = requests.request(
                    method=method,
                    url=url,
                    params=params,
                    headers=headers,
                    json=json,
                    data=data,
                    cookies=cookies,
                    timeout=timeout,
                    proxies=proxy[0],
                )

                return transform(response) if transform else response
            except:
                proxy = next(proxy_cycle)
                if start_proxy == proxy:
                    if retries == max_retries:
                        raise ProxiesError("Proxy cycle finished")
    else:
        response = requests.request(
            method=method,
            url=url,
            params=params,
            headers=headers,
            data=data,
            cookies=cookies,
            json=json,
            timeout=timeout,
        )

        return transform(response) if transform else response
