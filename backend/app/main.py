from fastapi import FastAPI

from app.config import settings


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)


@app.get("/")
def home():
    return {
        "project": "TEYZUS",
        "status": "online",
        "version": settings.VERSION
    }
