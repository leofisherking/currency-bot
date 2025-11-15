from contextlib import asynccontextmanager
from typing import Any, AsyncIterator
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from currency_bot.bot import bot
from currency_bot.core.providers.setup import app_container
from currency_bot.core.settings import settings
from currency_bot.services.binance_listener import BinanceListener


@asynccontextmanager
async def lifespan_app(app: FastAPI) -> AsyncIterator[Any]:
    binance_listener = await app_container.get(BinanceListener)
    await binance_listener.start()

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(url=settings.webhook_url)

    yield

    await binance_listener.stop()

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.session.close()


def create_app() -> FastAPI:
    app_options = {
        "docs_url": None,
        "redoc_url": None,
        "openapi_url": None,
    }

    app = FastAPI(
        title="Currency Bot Webhook",
        **app_options,
        lifespan=lifespan_app,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    return app
