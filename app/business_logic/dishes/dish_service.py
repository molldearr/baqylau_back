from fastapi import HTTPException
from api.dishes.dish_schemas import CommentRead, DifficultyRead, DishAllRead, DishCreate, DishImageRead, DishNewRead, DishRead, DishSearch, IngredientRead, KitchenRead, ReceiptIngredientRead, ReceiptRead
from data_access.db.models.dish import Dish
from data_access.dish.dish_repository import DishRepository
from sqlalchemy.ext.asyncio import AsyncSession

from uuid import UUID


class DishService:
    def __init__(self, db: AsyncSession):
        self.repo = DishRepository(db)

    async def get_all_dishes(self):
        rows = await self.repo.get_all_dishes()

        dishes_map = {}

        for row in rows:

            dish_id = row.id

            if dish_id not in dishes_map:
                dishes_map[dish_id] = DishAllRead(
                    id=row.id,
                    name=row.name,
                    description=row.description,
                    value=float(row.avg_rating) if row.avg_rating else 0,
                    images=[]
                )

            if row.image_path:
                dishes_map[dish_id].images.append(
                    DishImageRead(image_path=row.image_path)
                )

        dishes = list(dishes_map.values())

        return dishes

    async def get_by_id(self, dish_id: UUID):
        dish = await self.repo.get_by_id(dish_id)

        if not dish:
            raise HTTPException(status_code=404, detail="Dish not found")

        return DishRead(
            id=dish.id,
            name=dish.name,
            description=dish.description,
            difficulty=DifficultyRead(
                id=dish.difficulties.id,
                name=dish.difficulties.name
            ) if dish.difficulties is not None else None,
            receipt=ReceiptRead(
                id=dish.receipt.id,
                title=dish.receipt.title,
                instructions=dish.receipt.instructions,
                cooking_time=dish.receipt.cooking_time,
                calorie=dish.receipt.calorie,

                receipt_ingredients=[
                    ReceiptIngredientRead(
                        id=ri.id,
                        quantity=ri.quantity,
                        ingredient=IngredientRead(
                            id=ri.ingredient.id,
                            title=ri.ingredient.title
                        )
                    )
                    for ri in dish.receipt.receipt_ingredients
                ]
            ) if dish.receipt else None,

            images=[
                DishImageRead(
                    id=image.id,
                    image_path=image.image_path
                )
                for image in dish.images
            ],

            comments=[
                CommentRead.model_validate(c)
                for c in dish.comments
            ],

            kitchen=KitchenRead.model_validate(dish.kitchen) if dish.kitchen else None,
        )
    
    async def create_dishes(self, data: DishCreate):
        dish = Dish(
            name= data.name,
            description = data.description,
            difficulty_id=data.difficulty_id
        )
        created_dish = await self.repo.create_dishes(dish=dish)

        return DishNewRead(
            id=created_dish.id,
            name=created_dish.name,
            description=created_dish.description
        )
        
    async def search_dish(self, search_word):
        found_dishes = await self.repo.search_dish(search_word)

        return [
            DishSearch(
                id=dish.id,
                name=dish.name,
                description=dish.description,
                images=[
                    DishImageRead(
                        image_path=dish_image.image_path
                    ) for dish_image in dish.images
                ]
            )
            for dish in found_dishes
        ]
