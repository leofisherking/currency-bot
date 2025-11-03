from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from dishka.integrations.aiogram import setup_dishka

from currency_bot.core.providers.setup import app_container
from currency_bot.core.settings import settings
from currency_bot.bot_router.commands import router as commands_router

bot = Bot(
    token=settings.TELEGRAM_BOT_TOKEN.get_secret_value(),
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
dispatcher = Dispatcher(storage=MemoryStorage())
dispatcher.include_router(commands_router)
setup_dishka(
    container=app_container,
    router=dispatcher,
)
