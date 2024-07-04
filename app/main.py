from fastapi import FastAPI

from services.database import lifespan
from routes import routers
from services.config import settings

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def health():
    print("HELLOOOOOOOO!!!!!!!!!")
    print(settings.DATABASE_URL, settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    return {"Server Status": "Running!!"}


app.include_router(routers)

