import asyncio
import os

import uvicorn
from fastapi import FastAPI

from app.checker.session_router import (
    router as session_router
)


# ============================================================
# FASTAPI
# ============================================================

app = FastAPI(
    title="TEYZUS",
    version="1.0.0"
)


# ============================================================
# ROUTERS
# ============================================================

app.include_router(
    session_router
)


# ============================================================
# HEALTH
# ============================================================

@app.get("/")
async def root():
    return {
        "status": "ok",
        "service": "TEYZUS"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }


# ============================================================
# SERVER
# ============================================================

async def main():

    port = int(
        os.getenv(
            "PORT",
            "8000"
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

    await server.serve()


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    asyncio.run(
        main()
    )
