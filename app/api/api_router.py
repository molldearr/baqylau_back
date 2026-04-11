from fastapi import APIRouter
from api.receipts.receipt_api import router as receipts_router
from api.dishes.dish_api import router as dishes_router
from api.users.user_api import router as users_router
from api.roles.role_api import router as roles_router
from api.notifications.notification_api import router as notification_router
from api.notifications.websocket_api import router as websocket_router


api_router = APIRouter()

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

api_router.include_router(
    notification_router,
    prefix="/notifications",
    tags=["NOTIFICATIONS"]
)

api_router.include_router(
    websocket_router,
    prefix="/ws",
    tags=["WEBSOCKET"]
)
