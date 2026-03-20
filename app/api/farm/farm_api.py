from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.farm.farm_schemas import FarmCreate, FarmRead
from bussiness_logic.farm.farm_service import FarmService
from data_access.farm.farm_repository import FarmRepository
from data_access.db.session import get_db

router = APIRouter()


def get_farm_service(db: AsyncSession = Depends(get_db)) -> FarmService:
    repo = FarmRepository(db)
    return FarmService(repo)


@router.get("/all", response_model=list[FarmRead])
async def get_farms(
    service: FarmService = Depends(get_farm_service),
):
    return await service.get_farms()


@router.post("/create", response_model=FarmRead)
async def create_farm(
    farm: FarmCreate,
    service: FarmService = Depends(get_farm_service),
):
    try:
        return await service.create(farm)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))