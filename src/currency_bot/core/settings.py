from pydantic_settings import BaseSettings
from pydantic import SecretStr


class Settings(BaseSettings):
    APP_HOST: str

    APP_TELEGRAM_WEBHOOK_PATH: str
    APP_WEBHOOK_SECRET_POSTFIX: SecretStr

    TELEGRAM_BOT_TOKEN: SecretStr

    TELEGRAM_BOT_ADMIN_ID: int

    EXCHANGE_RATE_API_KEY: SecretStr

    @property
    def webhook_url(self) -> str:
        return f"{self.APP_HOST}/{self.APP_TELEGRAM_WEBHOOK_PATH}/{self.APP_WEBHOOK_SECRET_POSTFIX.get_secret_value()}"


settings = Settings()
