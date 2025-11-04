from abc import ABC, abstractmethod


class BaseListener(ABC):
    def __init__(self, url: str) -> None:
        self._url = url

    @abstractmethod
    async def get_last_ticker(self) -> dict:
        raise NotImplementedError
