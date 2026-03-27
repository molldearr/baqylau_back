from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.crop.crop_schemas import CropCreate, CropRead
from business_logic.crop.crop_service import CropService
from data_access.crop.crop_repository import CropRepository
from data_access.db.session import get_db

router = APIRouter()


def get_crop_service(db: AsyncSession = Depends(get_db)) -> CropService:
    repo = CropRepository(db)
    return CropService(repo)

@router.get("/all"
            # response_model=list[CropRead]
            )
async def get_crops(
    service: CropService = Depends(get_crop_service),
):
    print("GGGGGg")
    return await service.get_crop()


@router.post("/create", response_model=CropRead)
async def create_crop(
    crop: CropCreate,
    service: CropService = Depends(get_crop_service),
):
    try:
        return await service.create(crop)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))