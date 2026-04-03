from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from decimal import Decimal
from datetime import datetime


class UserShort(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: str
    avatar_url: str

    class Config:
        from_attributes = True


class TutorRead(BaseModel):
    id: UUID
    user_id: UUID

    bio: Optional[str]
    experience_years: Optional[int]
    education: Optional[str]

    price_per_hour: Decimal
    currency: str

    format: Optional[str]
    city: Optional[str]

    average_rating: Decimal
    total_reviews: int

    created_at: datetime
    updated_at: datetime

    user: Optional[UserShort]  # ✅ ВОТ ЭТО ДОБАВИТЬ

    class Config:
        from_attributes = True
