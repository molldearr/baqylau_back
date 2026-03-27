from typing import List, Optional

from pydantic import BaseModel
from uuid import UUID


class DishImageRead(BaseModel):
    id: UUID
    image_path: str

    class Config:
        from_attributes = True


class DishAllRead(BaseModel):
    id: UUID
    name: str
    description: str

    images: List[DishImageRead] = []

    class Config:
        from_attributes = True



class ReceiptRead(BaseModel):
    id: UUID
    title: str
    instructions: str
    cooking_time: Optional[int]
    difficulty: Optional[str]

    model_config = {"from_attributes": True}


class DishRead(BaseModel):
    id: UUID
    name: str
    description: str
    # receipt: Optional[ReceiptRead] = None

    model_config = {"from_attributes": True}

    
class DishCreate(BaseModel):
    name: str
    description: str
    
    model_config = {"from_attributes": True}


class DishNewRead(BaseModel):
    name: str
    description: str

    model_config = {"from_attributes": True}
