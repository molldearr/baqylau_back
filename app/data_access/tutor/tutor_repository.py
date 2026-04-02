from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from data_access.db.models.tutor import Tutor


class TutorRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_tutors(self):
        result = await self.db.execute(
            select(Tutor).options(
                selectinload(Tutor.user)
            )
        )

        tutors = result.scalars().all()

        return tutors

