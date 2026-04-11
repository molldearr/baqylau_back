from sqlalchemy.ext.asyncio import AsyncSession
from data_access.db.models.ingredient import Ingredient

async def seed_ingredients(db: AsyncSession):
    ingredients = [
        "Cheese",
        "Tomato",
        "Flour",
        "Chicken",
        "Beef",
        "Salt",
        "Pepper",
        "Onion",
        "Garlic",
        "Olive oil"
    ]

    for title in ingredients:
        db.add(Ingredient(title=title))

    await db.commit()
    print("Ingredients seeded!")
