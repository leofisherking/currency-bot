from dishka import make_async_container
from currency_bot.core.providers.services_provider import ServicesProvider
from currency_bot.core.providers.use_cases_provider import UseCasesProvider

app_container = make_async_container(
    ServicesProvider(),
    UseCasesProvider(),
)
