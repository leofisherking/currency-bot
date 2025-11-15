class TelegramMessageBuilder:
    @staticmethod
    def build_current_rates_message(usd_data: dict, btc_data: dict) -> str:
        message = (
            f"<b>USD/RUB:</b>\t{usd_data.get('conversion_rate')}\n"
            f"updated: {usd_data.get('last_update')} utc\n"
            "\n"
            f"<b>BTC/USD:</b>\t{btc_data.get('price')}\n"
            f"updated: {btc_data.get('price_time')} utc"
        )

        return message
