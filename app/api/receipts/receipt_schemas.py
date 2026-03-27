from typing import Optional

from pydantic import BaseModel
from uuid import UUID


class ReceiptRead(BaseModel):
    id: UUID
    title: str
    instructions: str
    cooking_time: Optional[int]
    difficulty: Optional[str]

    class Config:
        from_attributes = True


class ReceiptCreate(BaseModel):
    title: str
    instructions: str
    cooking_time: Optional[int]
    difficulty: Optional[str]
    
    class Config:
        from_attributes = True
