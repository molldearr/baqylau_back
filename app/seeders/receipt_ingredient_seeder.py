from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from data_access.db.models.receipt import Receipt
from data_access.db.models.ingredient import Ingredient
from data_access.db.models.receipt_ingredient import ReceiptIngredient
import random

QUANTITIES = [
    "100g",
    "200g",
    "1 tbsp",
    "2 pcs",
    "to taste"
]

async def seed_receipt_ingredients(db: AsyncSession):
    receipts_result = await db.execute(select(Receipt))
    ingredients_result = await db.execute(select(Ingredient))

    receipts = receipts_result.scalars().all()
    ingredients = ingredients_result.scalars().all()

    for receipt in receipts:
        selected_ingredients = random.sample(ingredients, k=random.randint(3, 6))

        for ingredient in selected_ingredients:
            ri = ReceiptIngredient(
                receipt=receipt,
                ingredient=ingredient,
                quantity=random.choice(QUANTITIES)
            )
            db.add(ri)

    await db.commit()
    print("Receipt-Ingredients seeded!")
