from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from utils.auth_middleware import get_current_user
from business_logic.tutors.tutor_service import TutorService
from data_access.db.session import get_db

router = APIRouter()


def get_tutor_service(db: AsyncSession = Depends(get_db)) -> TutorService:
    return TutorService(db)


@router.get("/all")
async def get_all_tutors(
    service: TutorService = Depends(get_tutor_service),
    user=Depends(get_current_user),  # 🔐 ВОТ ОНО
):
    result = await service.get_all_tutors()

    return result
