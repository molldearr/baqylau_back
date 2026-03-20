from fastapi import APIRouter
from . import farm_router

router = APIRouter(
    prefix="/farms",
)
router.include_router(
    farm_router.router,
    tags=["farms"]
)