from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from data_access.db.models.dish_image import DishImage
from data_access.db.models.dish import Dish

async def seed_dishes(db: AsyncSession):
    dishes_data = [
        {
            "name": "Pizza",
            "description": "Classic Italian pizza",
            "images": [
                "https://images.unsplash.com/photo-1711539137930-3fa2ae6cec60?crop=entropy&cs=tinysrgb&fit=max&fm=jpg",
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRe94bKxLZsXIgSPiMYjxrU7sMYIanfTclqyw&s"
            ]
        },
        {
            "name": "Burger",
            "description": "Juicy beef burger",
            "images": [
                "https://images.unsplash.com/photo-1605034298551-baacf17591d1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg"
            ]
        },
        {
            "name": "Sushi",
            "description": "Fresh salmon sushi",
            "images": [
                "https://images.unsplash.com/photo-1693422660544-014dd9f3ef73?crop=entropy&cs=tinysrgb&fit=max&fm=jpg"
            ]
        }
    ]

    for d in dishes_data:
        result = await db.execute(select(Dish).where(Dish.name == d["name"]))
        exists = result.scalar_one_or_none()
        if not exists:
            dish = Dish(
                name=d["name"],
                description=d["description"],
                images=[DishImage(image_path=img) for img in d["images"]]
            )
            db.add(dish)

    await db.commit()
    print("Dishes seeded!")
