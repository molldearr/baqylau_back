from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from api.dishes.dish_schemas import DishAllRead, DishCreate, DishRead
from business_logic.dishes.dish_service import DishService
from data_access.dish.dish_repository import DishRepository
from data_access.db.session import get_db

router = APIRouter()


def get_dish_service(db: AsyncSession = Depends(get_db)) -> DishService:
    repo = DishService(db)
    return (repo)


@router.get("/all", response_model=list[DishAllRead])
async def get_all_receipts(
    service: DishService = Depends(get_dish_service),
):
    return await service.get_all_dishes()


@router.get("/{id}", response_model=DishRead)
async def get_dish_by_id(
    id,
    service: DishService = Depends(get_dish_service),
):
    return await service.get_by_id(id)

@router.post("/new", response_model=DishRead)
async def create_new_dish(
    dish: DishCreate,
    service: DishService = Depends(get_dish_service),
):
    return await service.create_dishes(dish)