from fastapi import HTTPException
from api.dishes.dish_schemas import DishAllRead, DishCreate, DishImageRead, DishNewRead, DishRead
from data_access.db.models.dish import Dish
from data_access.dish.dish_repository import DishRepository
from sqlalchemy.ext.asyncio import AsyncSession

from uuid import UUID


class DishService:
    def __init__(self, db: AsyncSession):
        self.repo = DishRepository(db)

    async def get_all_dishes(self):
        rows = await self.repo.get_all_dishes()

        dishes = []

        for row in rows:
            dish = DishAllRead(
                id=row.id,
                name=row.name,
                description=row.description,
                value=float(row.avg_rating) if row.avg_rating else 0,
                images=[
                    DishImageRead(
                        image_path=row.image_path
                    )
                ]
            )
            dishes.append(dish)

        return dishes

    async def get_by_id(self, dish_id: UUID):
        dish = await self.repo.get_by_id(dish_id)

        if not dish:
            raise HTTPException(status_code=404, detail="Dish not found")

        return DishRead.model_validate(dish)
    
    async def create_dishes(self, data: DishCreate):
        dish = Dish(
            name= data.name,
            description = data.description
        )
        created_dish = await self.repo.create_dishes(dish=dish)

        return DishNewRead(
            id=created_dish.id,
            name=created_dish.name,
            description=created_dish.description
        )
        
        
