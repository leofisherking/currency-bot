from datetime import datetime, timezone
from typing import Final

from tenacity import retry, stop_after_attempt, wait_fixed

from currency_bot.services.abc.i_listener import BaseListener

from httpx import AsyncClient


class ExchangeRateListener(BaseListener):
    _RESPONSE_KEYS: Final[set[str]] = {
        "base_code",
        "target_code",
        "conversion_rate",
        "next_update",
    }

    def __init__(self, url: str, api_key: str) -> None:
        super().__init__(url)
        self._api_key = api_key
        self._cached_rate: dict = {}
        self._client = AsyncClient(base_url=self._url)

    async def get_last_ticker(self) -> dict:
        if not self._cached_rate or self._cache_expired():
            try:
                await self._request_last_ticker()
            except Exception as e:
                self._cached_rate["update_error"] = str(e)
        return self._cached_rate

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(1), reraise=True)
    async def _request_last_ticker(self) -> None:
        res = await self._client.get(f"/{self._api_key}/pair/USD/RUB")

        res.raise_for_status()

        serialized = res.json()

        serialized["next_update"] = datetime.fromtimestamp(
            serialized.get("time_next_update_unix"),
            tz=timezone.utc,
        )
        self._cached_rate = {
            k: v for k, v in serialized.items() if k in self._RESPONSE_KEYS
        }

    def _cache_expired(self) -> bool:
        if datetime.now(tz=timezone.utc) > self._cached_rate.get("next_update"):
            return True
        return False

    async def close(self) -> None:
        await self._client.aclose()
