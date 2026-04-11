from fastapi import APIRouter
from . import websocket_router

router = APIRouter(
    prefix="/",
)
router.include_router(
    websocket_router.router,
    tags=["WEBSOCKET"]
)
