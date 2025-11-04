import json

from fastapi import FastAPI
import uvicorn
import websockets

from currency_bot.app import create_app
from currency_bot.bot import bot, dispatcher
from currency_bot.core.settings import settings
from aiogram.types import Update

# app = FastAPI()
#
# @app.get("/")
# async def read_root():
#     msg_arr = []
#     async with websockets.connect("wss://fstream.binance.com/ws/btcusdt@miniTicker") as ws:
#         count = 3
#         async for msg in ws:
#             msg_arr.append(json.loads(msg))
#             count -= 1
#             if count == 0:
#                 break
#
#     return {"Hello": msg_arr}





app = create_app()

@app.post(f"/{settings.APP_TELEGRAM_WEBHOOK_PATH}/{settings.APP_WEBHOOK_SECRET_POSTFIX.get_secret_value()}")
async def bot_webhook(update: dict):
    await dispatcher.feed_update(bot=bot, update=Update(**update))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8004)