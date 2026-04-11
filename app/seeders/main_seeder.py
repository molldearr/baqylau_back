import asyncio, sys
from pathlib import Path

# Добавляем корень проекта в sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from data_access.db.session import AsyncSessionLocal
from kitchen_seeder import seed_kitchens
from difficulty_seeder import seed_difficulties
from dish_seeder import seed_dishes
from rating_seeder import seed_ratings
from receipt_seeder import seed_receipts
from role_seeder import seed_roles
from user_seeder import seed_users
from ingredient_seeder import seed_ingredients
from receipt_ingredient_seeder import seed_receipt_ingredients


async def main():
    async with AsyncSessionLocal() as db:
        await seed_kitchens(db)
        await seed_difficulties(db)
        await seed_dishes(db)
        await seed_ingredients(db)
        await seed_receipts(db)
        await seed_receipt_ingredients(db)
        await seed_roles(db)
        await seed_users(db)
        await seed_ratings(db)


if __name__ == "__main__":
    asyncio.run(main())
