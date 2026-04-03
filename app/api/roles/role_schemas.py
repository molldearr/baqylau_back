from typing import List, Optional
from pydantic import BaseModel, EmailStr
from uuid import UUID

class RoleRead(BaseModel):
    id: UUID
    name: str

    model_config = {"from_attributes": True}
