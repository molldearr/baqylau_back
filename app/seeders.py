import asyncio
from sqlalchemy import UUID, select
from sqlalchemy.ext.asyncio import AsyncSession
from data_access.db.models.role import Role
from data_access.db.models.receipt import Receipt
from data_access.db.models.dish import Dish
from data_access.db.models.dish_image import DishImage
from data_access.db.models.user import User
from data_access.db.session import AsyncSessionLocal
import hashlib


async def seed_dishes(db: AsyncSession):
    dishes_data = [
        {
            "name": "Pizza",
            "description": "Classic Italian pizza",
            "images": [
                "https://images.unsplash.com/photo-1711539137930-3fa2ae6cec60?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxkZWxpY2lvdXMlMjBwYXN0YSUyMGRpc2glMjBmb29kfGVufDF8fHx8MTc3MTk5NzI2N3ww&ixlib=rb-4.1.0&q=80&w=1080&utm_source=figma&utm_medium=referral", 
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRe94bKxLZsXIgSPiMYjxrU7sMYIanfTclqyw&s"
            ]
        },
        {
            "name": "Burger",
            "description": "Juicy beef burger",
            "images": [
                "https://images.unsplash.com/photo-1605034298551-baacf17591d1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxmcmVzaCUyMHNhbGFkJTIwYm93bCUyMGhlYWx0aHl8ZW58MXx8fHwxNzcxOTgwOTg0fDA&ixlib=rb-4.1.0&q=80&w=1080&utm_source=figma&utm_medium=referral", 
            ]
        },
        {
            "name": "Sushi",
            "description": "Fresh salmon sushi",
            "images": ["https://images.unsplash.com/photo-1693422660544-014dd9f3ef73?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxncmlsbGVkJTIwc3RlYWslMjBkaW5uZXJ8ZW58MXx8fHwxNzcxOTU1MzU2fDA&ixlib=rb-4.1.0&q=80&w=1080&utm_source=figma&utm_medium=referral",]
        },
        {
            "name": "Pasta",
            "description": "Creamy pasta",
            "images": ["https://images.unsplash.com/photo-1693422660544-014dd9f3ef73?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxncmlsbGVkJTIwc3RlYWslMjBkaW5uZXJ8ZW58MXx8fHwxNzcxOTU1MzU2fDA&ixlib=rb-4.1.0&q=80&w=1080&utm_source=figma&utm_medium=referral"]
        },
        {
            "name": "Steak",
            "description": "Grilled beef steak",
            "images": ["https://images.unsplash.com/photo-1607257882338-70f7dd2ae344?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxjaG9jb2xhdGUlMjBjYWtlJTIwZGVzc2VydHxlbnwxfHx8fDE3NzE5NTQ5Mzd8MA&ixlib=rb-4.1.0&q=80&w=1080&utm_source=figma&utm_medium=referral"]
        },
    ]

    for d in dishes_data:
        result = await db.execute(select(Dish).where(Dish.name == d["name"]))
        exists = result.scalar_one_or_none()

        if not exists:
            dish = Dish(
                name=d["name"],
                description=d["description"],
                images=[
                    DishImage(image_path=img) for img in d["images"]
                ]
            )
            db.add(dish)

    await db.commit()


async def seed_receipt_for_dish(db: AsyncSession):
    # UUID существующего блюда
    dish_id = "7960bff0-2200-4989-ad28-9ef0d01e3d8a"

    # Проверяем, есть ли уже блюдо
    result = await db.execute(select(Dish).where(Dish.id == dish_id))
    dish = result.scalar_one_or_none()

    if dish:
        # Создаём моковый рецепт
        receipt = Receipt(
            title="Classic Italian Pizza Recipe",
            instructions=(
                "1. Prepare the dough.\n"
                "2. Spread tomato sauce.\n"
                "3. Add mozzarella and toppings.\n"
                "4. Bake in the oven at 220°C for 12-15 minutes.\n"
                "5. Serve hot."
            ),
            cooking_time=20,
            difficulty="easy"
        )

        # Привязываем рецепт к блюду
        dish.receipt = receipt

        db.add(receipt)  # Добавляем рецепт в сессию
        await db.commit()
        print("Mock recipe added to dish!")
    else:
        print("Dish not found!")

async def seed_roles(db: AsyncSession):
    roles_data = [
        {"name": "admin",},
        {"name": "user",},
        {"name": "conditer",},
    ]

    for rd in roles_data:
        result = await db.execute(
            select(Role).where(
                (Role.name == rd["name"])
            )
        )
        exists = result.scalar_one_or_none()
        if not exists:
            role = Role(
                name=rd["name"],
            )
            db.add(role)

    await db.commit()

def hash_password(password: str) -> str:
    return hashlib.md5(password.encode('utf-8')).hexdigest()

async def run_seeders(db: AsyncSession):
    # await seed_dishes(db)
    # await seed_receipt_for_dish(db)
    # await seed_roles(db)
    ...

async def main():
    async with AsyncSessionLocal() as db:
        await run_seeders(db)


if __name__ == "__main__":
    asyncio.run(main())
