from fastapi import HTTPException
from data_access.farm.farm_repository import Farm
from data_access.db.models.farm import Farm
from api.farm.farm_schemas import FarmRead, FarmCreate

from uuid import UUID

class FarmService:
    def __init__(self, repo: Farm):
        self.repo = repo

    async def get_crop(self):
        return await self.repo.get_all()
    
    async def get_by_id(self, farm_id: UUID):
        farm = await self.repo.get_by_id(farm_id)

        if not farm:
            raise HTTPException(status_code=404, detail="Farm not found")
        return farm
    
    async def create(self, data: FarmCreate
    ):
        farm = Farm(
            name=data.name,
            country=data.country,
            iata_code=data.iata_code
        )

        return await self.repo.create(farm)