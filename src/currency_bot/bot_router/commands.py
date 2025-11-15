from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dishka import FromDishka
from dishka.integrations.aiogram import inject

from currency_bot.core.settings import settings
from currency_bot.domain.use_cases.get_current_rates import GetCurrentRates

router = Router()


@router.message(Command("rates"))
@inject
async def start_handler(
    message: Message,
    use_case: FromDishka[GetCurrentRates],
) -> None:
    if message.from_user.id == settings.TELEGRAM_BOT_ADMIN_ID:
        current_rates = await use_case.execute()
        await message.answer(current_rates)