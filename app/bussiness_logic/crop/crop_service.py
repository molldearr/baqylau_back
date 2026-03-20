from fastapi import HTTPException
from data_access.crop.crop_repository import Crop
from data_access.db.models.crop import Crop
from api.crop.crop_schemas import CropRead, CropCreate

from uuid import UUID

class CropService:
    def __init__(self, repo: Crop):
        self.repo = repo

    async def get_crop(self):
        return await self.repo.get_all()
    
    async def get_by_id(self, farm_id: UUID):
        crop = await self.repo.get_by_id(farm_id)

        if not crop:
            raise HTTPException(status_code=404, detail="Crop not found")
        return crop
    
    async def create(self, data: CropCreate
    ):
        crop = Crop(
            name=data.name,
            country=data.country,
            iata_code=data.iata_code
        )

        return await self.repo.create(crop)