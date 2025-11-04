from currency_bot.services.abc.i_listener import BaseListener
from currency_bot.services.telegram_message_builder import TelegramMessageBuilder


class GetCurrentRates:
    def __init__(
        self,
        exc_listener: BaseListener,
        binance_listener: BaseListener,
        telegram_message_builder: TelegramMessageBuilder,
    ) -> None:
        self._exc_listener = exc_listener
        self._binance_listener = binance_listener
        self._telegram_message_builder = telegram_message_builder

    async def execute(self) -> str:
        usd_data = await self._exc_listener.get_last_ticker()
        btc_data = await self._binance_listener.get_last_ticker()

        return self._telegram_message_builder.build_current_rates_message(
            usd_data=usd_data,
            btc_data=btc_data,
        )
