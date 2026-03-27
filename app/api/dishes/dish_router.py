from fastapi import APIRouter
from . import dish_router

router = APIRouter(
    prefix="/dishes",
)
router.include_router(
    dish_router.router,
    tags=["dishes"]
)
