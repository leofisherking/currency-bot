import asyncio
import json
from datetime import datetime, timezone

import websockets
from tenacity import stop_never, wait_exponential, retry

from currency_bot.services.abc.i_listener import BaseListener


class BinanceListener(BaseListener):
    def __init__(self, url: str) -> None:
        super().__init__(url)

        self._task: asyncio.Task | None = None
        self._running: bool = False

        self._ticker_path: str = url
        self._last_ticker: str | bytes | None = None

    async def start(self) -> None:
        self._running = True
        self._task = asyncio.create_task(self._listen())

    async def stop(self) -> None:
        self._running = False
        if self._task:
            await self._task

    @retry(
        stop=stop_never,
        wait=wait_exponential(multiplier=1, max=60),
    )
    async def _listen(self) -> None:
        async with websockets.connect(self._url) as ws:
            async for msg in ws:
                if not self._running:
                    break
                self._last_ticker = msg

    async def get_last_ticker(self) -> dict | None:
        if self._last_ticker is None:
            return None
        return self._serialize(self._last_ticker)

    @staticmethod
    def _serialize(msg: str | bytes) -> dict:
        if isinstance(msg, bytes):
            msg = msg.decode("utf-8")
        serialized = json.loads(msg)

        update_date = datetime.fromtimestamp(
            serialized.get("E") / 1000, tz=timezone.utc
        )

        return {
            "price": serialized.get("c"),
            "price_time": datetime.strftime(update_date, "%Y-%m-%d %H:%M:%S"),
        }
