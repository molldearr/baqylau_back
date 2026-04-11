from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func, select
from uuid import UUID

from sqlalchemy.orm import selectinload
from data_access.db.models.receipt import Receipt
from data_access.db.models.receipt_ingredient import ReceiptIngredient
from data_access.db.models.rating import Rating
from data_access.db.models.dish_image import DishImage
from data_access.db.models.dish import Dish
from sqlalchemy import or_


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
            .join(DishImage, DishImage.dish_id == Dish.id)
            .join(Rating, Rating.dish_id == Dish.id)
            .group_by(Dish.id, Dish.name, Dish.description, DishImage.image_path)
        )

        return result.all()
    
    async def get_by_id(self, dish_id: UUID) -> Dish | None:
        result = await self.db.execute(
            select(Dish)
            .options(
                selectinload(Dish.images),
                selectinload(Dish.kitchen),
                selectinload(Dish.comments),
                selectinload(Dish.difficulties),
                
                selectinload(Dish.receipt)
                .selectinload(Receipt.receipt_ingredients)
                .selectinload(ReceiptIngredient.ingredient),
            )
            .where(Dish.id == dish_id)
        )
        return result.scalar_one_or_none()

    async def create_dishes(self, dish: Dish) -> Dish:
        db_dish = self.db.add(dish)
        await self.db.commit()
        await self.db.refresh(db_dish)  
        
        return db_dish

    async def search_dish(self, search_word: str):
        ts_query = func.plainto_tsquery("russian", search_word)

        base_query = (
            select(Dish)
            .options(
                selectinload(Dish.images),
                selectinload(Dish.ratings)
            )
        )

        fts_query = base_query.where(
            Dish.search_vector.op("@@")(ts_query)
        )

        like_query = base_query.where(
            Dish.name.ilike(f"%{search_word}%")
        )

        result = await self.db.execute(fts_query)
        rows = result.scalars().all()

        if rows:
            return rows

        result = await self.db.execute(like_query)
        return result.scalars().all()
