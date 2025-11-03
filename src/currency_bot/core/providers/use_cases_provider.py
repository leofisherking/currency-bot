from dishka import Provider, Scope, provide

from currency_bot.domain.use_cases.get_current_rates import GetCurrentRates
from currency_bot.services.binance_listener import BinanceListener
from currency_bot.services.exchange_rate_listener import ExchangeRateListener
from currency_bot.services.telegram_message_builder import TelegramMessageBuilder


class UseCasesProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_current_rates(
        self,
        exc_listener: ExchangeRateListener,
        binance_listener: BinanceListener,
        telegram_message_builder: TelegramMessageBuilder,
    ) -> GetCurrentRates:
        return GetCurrentRates(
            exc_listener=exc_listener,
            binance_listener=binance_listener,
            telegram_message_builder=telegram_message_builder,
        )
