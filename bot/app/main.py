import asyncio

from aiogram import Bot, Dispatcher

from app.config import settings

from app.handlers.start import router as start_router
from app.handlers.menu import router as menu_router

from app.handlers.search_start import router as search_start_router
from app.handlers.search_process import router as search_process_router

from app.search_menu.handlers import router as search_menu_router


bot = Bot(
    token=settings.BOT_TOKEN
)


dp = Dispatcher()


# Старт
dp.include_router(
    start_router
)


# Меню поиска 🔎
dp.include_router(
    search_menu_router
)


# Старый поиск
dp.include_router(
    search_start_router
)


dp.include_router(
    search_process_router
)


# Главное меню
dp.include_router(
    menu_router
)


async def main():

    print(
        "🚀 TEYZUS Bot started"
    )

    await dp.start_polling(
        bot
    )


if __name__ == "__main__":

    asyncio.run(
        main()
    )
