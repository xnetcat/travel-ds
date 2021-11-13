import re
import requests

from travelds.proxies.proxy import ProxyProvider

class SpysMe(ProxyProvider):
    def load_proxies(self) -> None:
        text = requests.get("https://www.spys.me/proxy.txt").text
        matches = re.findall(r"[0-9]+(?:\.[0-9]+){3}\:[0-9]+", text)

        self._proxies = matches
