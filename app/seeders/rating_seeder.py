from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from data_access.db.models.dish import Dish
from data_access.db.models.rating import Rating
from data_access.db.models.user import User
from datetime import datetime

async def seed_ratings(db: AsyncSession):
    # Берем все блюда
    result = await db.execute(select(Dish))
    dishes = result.scalars().all()

    # Берем реальных пользователей
    result_users = await db.execute(select(User))
    users = result_users.scalars().all()

    if not users:
        print("No users found. Seed users first.")
        return

    for dish in dishes:
        for user in users:
            rating = Rating(
                dish_id=dish.id,
                user_id=user.id,
                value=5,  # по умолчанию 5 звезд
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            db.add(rating)

    await db.commit()
    print("Ratings seeded!")
