from typing import List, Optional
from pydantic import BaseModel, EmailStr
from uuid import UUID


class UserRead(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: str
    
    model_config = {"from_attributes": True}


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserLoginResponse(BaseModel):
    user: UserRead
    access_token: str
    token_type: str
