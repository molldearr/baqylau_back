from pydantic import BaseModel
from uuid import UUID


class FarmRead(BaseModel):
    id: UUID
    name: str
    region: str
    area_hectares: float

    class Config:
        from_attributes = True


class FarmCreate(BaseModel):
    name: str
    region: str
    area_hectares: float

    class Config:
        from_attributes = True