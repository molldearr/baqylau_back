from fastapi import APIRouter
from . import notifications_router

router = APIRouter(
    prefix="/notifications",
)
router.include_router(
    notifications_router.router,
    tags=["notifications"]
)
