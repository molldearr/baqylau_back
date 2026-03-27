from fastapi import HTTPException
from data_access.crop.crop_repository import Crop, CropRepository
from data_access.db.models.crop import Crop
from api.crop.crop_schemas import CropRead, CropCreate

from uuid import UUID

class ReceiptService:
    def __init__(self, repo: CropRepository):
        self.repo: CropRepository = repo

    async def get_crop(self):
        print("FFFFF")
        asd = await self.repo.get_all()
        print("asdasd", asd)
        return asd
    
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