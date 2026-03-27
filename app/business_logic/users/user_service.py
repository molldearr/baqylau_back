from fastapi import Depends, HTTPException
from api.users.user_schemas import UserLoginResponse, UserRead
from data_access.db.session import get_db
from data_access.user.user_repository import UserRepository
from uuid import UUID
import hashlib
from utils.token_creator import create_access_token
from sqlalchemy.ext.asyncio import AsyncSession


class UserService:
    def __init__(self, db: AsyncSession):
        self.repo = UserRepository(db)

    async def register_user(self, first_name, last_name, email, password):
        created_user = await self.repo.register_user(first_name, last_name, email, self.__hash_password(password))

        return UserRead(
            id=created_user.id,
            first_name=created_user.first_name,
            last_name=created_user.last_name,
            email=created_user.email,
        )

    async def login_user(self, email, password):
        hashed_password = self.__hash_password(password)
        
        logged_in_user = await self.repo.login_user(email, hashed_password)
        
        print("QWEQWEQWEQW: ")

        if not logged_in_user:
            return None  # или raise HTTPException(401)

        # создаем JWT
        token_data = {"sub": str(logged_in_user.id), "email": logged_in_user.email}
        access_token = create_access_token(token_data)

        return {
            "user": UserRead(
                id=logged_in_user.id,
                first_name=logged_in_user.first_name,
                last_name=logged_in_user.last_name,
                email=logged_in_user.email
            ),
            "access_token": access_token,
            "token_type": "bearer"
        }

    def __hash_password(self, password: str) -> str:
        return hashlib.md5(password.encode('utf-8')).hexdigest()
