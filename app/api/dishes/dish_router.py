from fastapi import APIRouter
from . import dish_router


router = APIRouter(
)
router.include_router(
    dish_router.router,
    tags=["dishes"]
)
