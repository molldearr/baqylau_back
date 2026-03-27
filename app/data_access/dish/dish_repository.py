from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID

from sqlalchemy.orm import selectinload
from data_access.db.models.dish import Dish


class DishRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_dishes(self):
        result = await self.db.execute(
            select(Dish).options(selectinload(Dish.images))
        )
        return result.scalars().all()
    
    async def get_by_id(self, dish_id: UUID) -> Dish | None:
        result = await self.db.execute(
            select(Dish)
            .options(
                selectinload(Dish.images),   # подгружаем картинки сразу
                selectinload(Dish.receipt)   # подгружаем рецепт сразу
            )
            .where(Dish.id == dish_id)
        )
        print('ASDASDSD: ')
        return result.scalar_one_or_none()

    async def create_dishes(self, dish: Dish) -> Dish:
        db_dish = self.db.add(dish)
        await self.db.commit()
        await self.db.refresh(db_dish)  
        
        return db_dish
