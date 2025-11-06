from aiogram.types import Update
from fastapi import status
import uvicorn

from currency_bot.app import create_app
from currency_bot.bot import bot, dispatcher
from currency_bot.core.settings import settings

app = create_app()


@app.post(
    f"/{settings.APP_TELEGRAM_WEBHOOK_PATH}/{settings.APP_WEBHOOK_SECRET_POSTFIX.get_secret_value()}"
)
async def bot_webhook(update: dict):
    await dispatcher.feed_update(bot=bot, update=Update(**update))


@app.get(
    "/healthcheck",
    status_code=status.HTTP_200_OK,
)
async def health_check() -> None:
    return


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
