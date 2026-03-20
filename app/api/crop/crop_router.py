from fastapi import APIRouter
from . import crop_router

router = APIRouter(
    prefix="/crops",
)
router.include_router(
    crop_router.router,
    tags=["crops"]
)