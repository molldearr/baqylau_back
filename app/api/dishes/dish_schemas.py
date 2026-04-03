from typing import List, Optional

from pydantic import BaseModel
from uuid import UUID


class DishImageRead(BaseModel):
    id: UUID = None
    image_path: Optional[str]

    class Config:
        from_attributes = True


class DishAllRead(BaseModel):
    id: UUID
    name: str
    description: str
    value: float

    images: List[DishImageRead] = []

    class Config:
        from_attributes = True



class ReceiptRead(BaseModel):
    id: UUID
    title: str
    instructions: str
    cooking_time: Optional[int]
    difficulty: Optional[str]
    calorie: Optional[int]

    model_config = {"from_attributes": True}


class KitchenRead(BaseModel):
    id: UUID
    name: str

    model_config = {"from_attributes": True}


class CommentRead(BaseModel):
    id: UUID
    text: str

    model_config = {"from_attributes": True}


class DishRead(BaseModel):
    id: UUID
    name: str
    description: str
    receipt: Optional[ReceiptRead] = None
    images: List[DishImageRead] = []
    comments: List[CommentRead] = []
    kitchen: Optional[KitchenRead] = None

    model_config = {"from_attributes": True}


class DishCreate(BaseModel):
    name: str
    description: str
    
    model_config = {"from_attributes": True}


class DishNewRead(BaseModel):
    name: str
    description: str

    model_config = {"from_attributes": True}
