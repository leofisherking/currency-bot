from typing import AsyncIterator

from dishka import Provider, Scope, provide

from currency_bot.core.settings import settings
from currency_bot.resources.urls import BINANCE_TICKER_URL, EXCHANGE_RATE_BASE_URL
from currency_bot.services.binance_listener import BinanceListener
from currency_bot.services.exchange_rate_listener import ExchangeRateListener
from currency_bot.services.telegram_message_builder import TelegramMessageBuilder


class ServicesProvider(Provider):
    @provide(scope=Scope.APP)
    async def exchange_rate_listener(
        self,
    ) -> AsyncIterator[ExchangeRateListener]:
        exc_listener = ExchangeRateListener(
            url=EXCHANGE_RATE_BASE_URL,
            api_key=settings.EXCHANGE_RATE_API_KEY.get_secret_value(),
        )
        yield exc_listener
        await exc_listener.close()

    @provide(scope=Scope.APP)
    async def binance_listener(
        self,
    ) -> BinanceListener:
        return BinanceListener(url=BINANCE_TICKER_URL)

    @provide(scope=Scope.REQUEST)
    async def telegram_message_builder(self) -> TelegramMessageBuilder:
        return TelegramMessageBuilder()
