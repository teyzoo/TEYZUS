import asyncio
import os
import uvicorn
from fastapi import FastAPI
from aiogram import Bot, Dispatcher
from app.config import settings
# ============================================================
# ROUTERS
# ============================================================
# Поиск username
from app.search_menu.handlers import (
    router as search_router
)
# Главное меню с inline-кнопками
from app.keyboards.menu import (
    router as menu_router
)
# Команда /start
from app.handlers.start import (
    router as start_router
)
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
        "service": "TEYZUS Bot"
    }
@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }
# ============================================================
# BOT
# ============================================================
async def run_bot():
    bot = Bot(
        token=settings.BOT_TOKEN
    )
    dp = Dispatcher()
    # ========================================================
    # ПОРЯДОК ROUTER
    # ========================================================
    #
    # Сначала поиск.
    # Затем inline-меню.
    # Последним /start.
    #
    # В start.py НЕ должно быть:
    #
    # @router.message()
    #
    # Используем только CommandStart().
    # ========================================================
    dp.include_router(
        search_router
    )
    dp.include_router(
        menu_router
    )
    dp.include_router(
        start_router
    )
    print(
        "🚀 TEYZUS Bot started"
    )
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
        log_level="info"
    )
    server = uvicorn.Server(
        config
    )
    # Telegram bot
    bot_task = asyncio.create_task(
        run_bot()
    )
    # FastAPI / Render health server
    server_task = asyncio.create_task(
        server.serve()
    )
    done, pending = await asyncio.wait(
        {
            bot_task,
            server_task
        },
        return_when=asyncio.FIRST_COMPLETED
    )
    # Если одна задача остановилась,
    # останавливаем вторую.
    for task in pending:
        task.cancel()
    await asyncio.gather(
        *pending,
        return_exceptions=True
    )
    # Не скрываем ошибки.
    for task in done:
        if task.cancelled():
            continue
        exception = task.exception()
        if exception:
            raise exception
# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    asyncio.run(
        main()
    )
