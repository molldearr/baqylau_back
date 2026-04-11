from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from data_access.db.models.difficulty import Difficulty


class LevelRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_levels(self):
        result = await self.db.execute(
            select(Difficulty)
        )
        return result.scalars().all()

    async def create_level(self, level: Difficulty) -> Difficulty:
        self.db.add(level)
        await self.db.commit()
        await self.db.refresh(level)
        return level