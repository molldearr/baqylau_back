from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from data_access.db.models.dish import Dish
from data_access.db.models.receipt import Receipt
import random

async def seed_receipts(db: AsyncSession):
    result = await db.execute(select(Dish))
    dishes = result.scalars().all()

    for dish in dishes:
        if not dish.receipt:
            receipt = Receipt(
                title=f"{dish.name} Recipe",
                instructions="1. Prepare ingredients\n2. Cook\n3. Serve hot",
                cooking_time=random.randint(1, 60),
                calorie=random.randint(1000, 5000)
            )
            dish.receipt = receipt
            db.add(receipt)

    await db.commit()
    print("Receipts seeded!")
