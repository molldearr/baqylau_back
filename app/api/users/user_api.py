from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from api.users.user_schemas import UserCreate, UserLogin, UserLoginResponse, UserRead
from data_access.user.user_repository import UserRepository
from business_logic.users.user_service import UserService
from data_access.db.session import get_db

router = APIRouter()


def get_user_service(db: AsyncSession = Depends(get_db)) -> UserService:
    return UserService(db)


@router.post("/register", response_model=UserRead)
async def user_register(
    user: UserCreate,
    service: UserService = Depends(get_user_service),
):
    return await service.register_user(user.first_name, user.last_name, user.email, user.password)


@router.post("/login")
async def user_login(
    user: UserLogin,
    service: UserService = Depends(get_user_service),
):
    result = await service.login_user(user.email, user.password)

    if not result:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return result
