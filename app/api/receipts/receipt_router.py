from fastapi import APIRouter
from . import receipt_router

router = APIRouter(
    prefix="/receipts",
)
router.include_router(
    receipt_router.router,
    tags=["receipts"]
)