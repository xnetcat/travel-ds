from typing import List, Optional


class ProxyProvider:
    def __init__(self) -> None:
        self._proxies: Optional[List] = None

    def load_proxies(self) -> None:
        raise NotImplementedError

    @property
    def proxies(self) -> List[str]:
        if self._proxies is None:
            raise UserWarning("load_proxies function wasn't called")
        return self._proxies
