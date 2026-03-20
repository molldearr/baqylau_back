from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from data_access.db.models.farm import Farm

class FarmRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> list[Farm]:
        result = await self.db.execute(select(Farm))
        return result.scalars().all()
    
    async def get_by_id(self, farm_id: UUID) -> Farm | None:
        result = await self.db.execute(select(Farm).where(Farm.id == farm_id))
        return result.scalar_one_or_none()
    
    async def create(self, farm: Farm) -> Farm:
        self.db.add(farm)
        await self.db.commit()
        await self.db.refresh(farm)

        return farm