import asyncio
import os
import uvicorn
from fastapi import FastAPI
from aiogram import Bot, Dispatcher
from app.config import settings
from app.search_menu.handlers import router
# ============================================================
# FASTAPI
# ============================================================
app = FastAPI(
    title="TEYZUS Bot",
    version="1.0.0",
)
@app.get("/")
async def health_check():
    return {
        "status": "ok",
        "service": "TEYZUS Bot",
    }
@app.get("/health")
async def health():
    return {
        "status": "healthy",
    }
# ============================================================
# BOT
# ============================================================
async def run_bot():
    bot = Bot(
        token=settings.BOT_TOKEN
    )
    dp = Dispatcher()
    # Подключаем существующий роутер.
    # Ничего из текущей логики бота не удаляем.
    dp.include_router(router)
    print("🚀 TEYZUS Bot started")
    try:
        await dp.start_polling(
            bot
        )
    finally:
        await bot.session.close()
# ============================================================
# MAIN
# ============================================================
async def main():
    port = int(
        os.getenv(
            "PORT",
            "10000"
        )
    )
    config = uvicorn.Config(
        app=app,
        host="0.0.0.0",
        port=port,
        log_level="info",
    )
    server = uvicorn.Server(config)
    bot_task = asyncio.create_task(
        run_bot()
    )
    server_task = asyncio.create_task(
        server.serve()
    )
    done, pending = await asyncio.wait(
        {
            bot_task,
            server_task,
        },
        return_when=asyncio.FIRST_COMPLETED,
    )
    for task in pending:
        task.cancel()
    await asyncio.gather(
        *pending,
        return_exceptions=True,
    )
    for task in done:
        if not task.cancelled():
            exception = task.exception()
            if exception:
                raise exception
if __name__ == "__main__":
    asyncio.run(
        main()
    )
