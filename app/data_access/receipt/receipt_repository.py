from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID

# from data_access.db.models.crop import Crop

class ReceiptRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    # async def get_all(self):
    #     result = await self.db.execute(
    #         select(Crop)
    #     )
    #     return result.scalars().all()
    
    # async def get_by_id(self, crop_id: UUID) -> Crop | None:
    #     result = await self.db.execute(select(Crop).where(Crop.id == crop_id))
    #     return result.scalar_one_or_none()
    
    # async def create(self, crop: Crop):
    #     self.db.add(crop)
    #     await self.db.commit()
    #     await self.db.refresh(crop)  

    #     return crop