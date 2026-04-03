from fastapi import APIRouter
from api.receipts.receipt_api import router as receipts_router
from api.dishes.dish_api import router as dishes_router
from api.users.user_api import router as users_router
from api.roles.role_api import router as roles_router

api_router = APIRouter()

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

api_router.include_router(
    roles_router,
    prefix="/roles",
    tags=["ROLE"]
)
