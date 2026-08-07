from fastapi import FastAPI

from app.config import settings
from app.database import Base, engine

from app.users.router import router as users_router


Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)


app.include_router(
    users_router
)


@app.get("/")
def home():

    return {
        "project": "TEYZUS",
        "status": "online",
        "version": settings.VERSION
    }
