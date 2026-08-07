import asyncio

from aiogram import Bot, Dispatcher

from app.config import settings

from app.handlers.start import router as start_router
from app.handlers.menu import router as menu_router


bot = Bot(
    token=settings.BOT_TOKEN
)


dp = Dispatcher()


dp.include_router(
    start_router
)


dp.include_router(
    menu_router
)


async def main():

    print("TEYZUS Bot started")

    await dp.start_polling(
        bot
    )


if __name__ == "__main__":
    asyncio.run(main())
