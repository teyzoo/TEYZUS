import asyncio

from aiogram import Bot, Dispatcher

from app.config import settings


bot = Bot(
    token=settings.BOT_TOKEN
)

dp = Dispatcher()


async def main():
    print("TEYZUS Bot started")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
