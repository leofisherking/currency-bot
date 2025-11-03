from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    # model_config = SettingsConfigDict(env_file="env/app.env")

    APP_HOST: str
    APP_PORT: int = 8000

    APP_TELEGRAM_WEBHOOK_PATH: str
    APP_WEBHOOK_SECRET_POSTFIX: SecretStr

    TELEGRAM_BOT_TOKEN: SecretStr
    TELEGRAM_BOT_PASSWORD: SecretStr

    TELEGRAM_BOT_ADMIN_ID: int

    EXCHANGE_RATE_API_KEY: SecretStr

    @property
    def webhook_url(self) -> str:
        return f"{self.APP_HOST}/{self.APP_TELEGRAM_WEBHOOK_PATH}/{self.APP_WEBHOOK_SECRET_POSTFIX.get_secret_value()}"


settings = Settings()
