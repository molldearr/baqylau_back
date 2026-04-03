from fastapi import APIRouter
from api.farm.farm_api import router as farm_router
from api.crop.crop_api import router as crop_router
from api.receipts.receipt_api import router as receipts_router
from api.dishes.dish_api import router as dishes_router
from api.users.user_api import router as users_router

api_router = APIRouter()

api_router.include_router(
    farm_router,
    prefix="/farm",
    tags=["FARM"]
)

api_router.include_router(
    crop_router,
    prefix="/crop",
    tags=["CROP"]
)

# api_router.include_router(
#     receipts_router,
#     prefix="/receipts",
#     tags=["RECEIPT"]
# )

api_router.include_router(
    dishes_router,
    prefix="/dishes",
    tags=["DISH"]
)

api_router.include_router(
    users_router,
    prefix="/users",
    tags=["USER"]
)
