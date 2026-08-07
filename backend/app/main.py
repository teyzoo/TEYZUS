from fastapi import FastAPI

from app.config import settings
from app.database import Base, engine

from app.users.router import router as users_router
from app.referrals.router import router as referrals_router
from app.premium.router import router as premium_router
from app.search.router import router as search_router
from app.limits.router import router as limits_router
from app.ai.router import router as ai_router
from app.pricing.router import router as pricing_router
from app.results.router import router as results_router


Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)


app.include_router(users_router)

app.include_router(referrals_router)

app.include_router(premium_router)

app.include_router(search_router)

app.include_router(limits_router)

app.include_router(ai_router)

app.include_router(pricing_router)

app.include_router(results_router)


@app.get("/")
def home():

    return {
        "project": "TEYZUS",
        "status": "online",
        "version": settings.VERSION,
        "modules": [
            "users",
            "referrals",
            "premium",
            "search",
            "limits",
            "ai",
            "pricing",
            "results"
        ]
    }
