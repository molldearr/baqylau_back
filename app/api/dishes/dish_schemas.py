from typing import List, Optional

from pydantic import BaseModel
from uuid import UUID


class DishImageRead(BaseModel):
    id: UUID = None
    image_path: Optional[str]

    model_config = {"from_attributes": True}


class DifficultyRead(BaseModel):
    id: UUID = None
    name: str

    model_config = {"from_attributes": True}
    

class DishAllRead(BaseModel):
    id: UUID
    name: str
    description: str
    value: float

    images: List[DishImageRead] = []

    class Config:
        from_attributes = True


class IngredientRead(BaseModel):
    id: UUID
    title: str

    model_config = {"from_attributes": True}


class ReceiptIngredientRead(BaseModel):
    id: UUID
    quantity: str
    ingredient: IngredientRead

    model_config = {"from_attributes": True}


class ReceiptRead(BaseModel):
    id: UUID
    title: str
    instructions: str
    cooking_time: Optional[int]
    calorie: Optional[int]
    
    receipt_ingredients: list[ReceiptIngredientRead] = []

    model_config = {"from_attributes": True}


class KitchenRead(BaseModel):
    id: UUID
    title: str

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
    difficulty: DifficultyRead | None = None
    kitchen: KitchenRead | None = None

    model_config = {"from_attributes": True}


class DishCreate(BaseModel):
    name: str
    description: str
    difficulty_id: Optional[str] = None
    
    model_config = {"from_attributes": True}


class DishNewRead(BaseModel):
    name: str
    description: str

    model_config = {"from_attributes": True}
    
class DishUpdate(BaseModel):
    difficulty_id: Optional[str] = None

    model_config = {"from_attributes": True}


class DishSearch(BaseModel):
    id: UUID
    name: str
    description: str
    images: List[DishImageRead] = []

    class Config:
        from_attributes = True
