from fastapi import APIRouter, Depends

from app.config import Settings, get_settings

router = APIRouter()


@router.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "the long pong goes on and on!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
