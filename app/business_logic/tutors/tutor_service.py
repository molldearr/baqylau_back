from fastapi import Depends, HTTPException
from api.tutors.tutor_schemas import TutorRead
from data_access.tutor.tutor_repository import TutorRepository
from sqlalchemy.ext.asyncio import AsyncSession


class TutorService:
    def __init__(self, db: AsyncSession):
        self.repo = TutorRepository(db)

    async def get_all_tutors(self):
        tutors = await self.repo.get_all_tutors()

        return [
            TutorRead.model_validate(tutor)
            for tutor in tutors
        ]
