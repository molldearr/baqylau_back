from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func, select
from uuid import UUID

from sqlalchemy.orm import selectinload
from data_access.db.models.rating import Rating
from data_access.db.models.dish_image import DishImage
from data_access.db.models.dish import Dish


class DishRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_dishes(self):
        result = await self.db.execute(
            select(
                Dish.id,
                Dish.name,
                Dish.description,
                DishImage.image_path,
                func.avg(Rating.value).label("avg_rating")
            )
            .outerjoin(DishImage, DishImage.dish_id == Dish.id)
            .outerjoin(Rating, Rating.dish_id == Dish.id)
            .group_by(Dish.id, Dish.name, Dish.description, DishImage.image_path)
        )

        return result.all()
    
    async def get_by_id(self, dish_id: UUID) -> Dish | None:
        result = await self.db.execute(
            select(Dish)
            .options(
                selectinload(Dish.images),
                selectinload(Dish.receipt),
                selectinload(Dish.kitchen),
                selectinload(Dish.comments),
            )
            .where(Dish.id == dish_id)
        )
        return result.scalar_one_or_none()

    async def create_dishes(self, dish: Dish) -> Dish:
        db_dish = self.db.add(dish)
        await self.db.commit()
        await self.db.refresh(db_dish)  
        
        return db_dish