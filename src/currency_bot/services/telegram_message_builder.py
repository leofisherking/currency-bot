class TelegramMessageBuilder:
    @staticmethod
    def build_current_rates_message(usd_data: dict, btc_data: dict) -> str:
        message = (
            f"<b>USD/RUB:</b>\t{usd_data.get('conversion_rate')}\n"
            f"<b>BTC/USD:</b>\t{btc_data.get('price')}"
        )

        return message
