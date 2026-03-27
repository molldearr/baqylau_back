import asyncio
from sqlalchemy import UUID, select
from sqlalchemy.ext.asyncio import AsyncSession
from data_access.db.models.role import Role
from data_access.db.models.receipt import Receipt
from data_access.db.models.dish import Dish
from data_access.db.models.dish_image import DishImage
from data_access.db.models.farm import Farm
from data_access.db.models.crop import Crop
from data_access.db.session import AsyncSessionLocal


async def seed_farms(db: AsyncSession):
    farms_data = [
        {"name": "Sunrise Farm", "region": "Almaty",   "area_hectares": 150.5},
        {"name": "Green Valley", "region": "Kostanay", "area_hectares": 320.0},
        {"name": "Steppe Gold",  "region": "Akmola",   "area_hectares": 500.0},
    ]
    for f in farms_data:
        result = await db.execute(select(Farm).where(Farm.name == f["name"]))
        exists = result.scalar_one_or_none()
        if not exists:
            farm = Farm(
                name=f["name"],
                region=f["region"],
                area_hectares=f["area_hectares"]
            )
            db.add(farm)
    await db.commit()

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


async def seed_crops(db: AsyncSession):
    """Crop кестесін толтыру, Farm Foreign Key бар екенін тексеру"""
    result = await db.execute(select(Farm).where(Farm.name == "Sunrise Farm"))
    sunrise_farm = result.scalar_one_or_none()
    if not sunrise_farm:
        sunrise_farm = Farm(name="Sunrise Farm", region="Almaty", area_hectares=150.5)
        db.add(sunrise_farm)
        await db.commit()
        await db.refresh(sunrise_farm)

    result = await db.execute(select(Farm).where(Farm.name == "Green Valley"))
    green_valley = result.scalar_one_or_none()
    if not green_valley:
        green_valley = Farm(name="Green Valley", region="Kostanay", area_hectares=320.0)
        db.add(green_valley)
        await db.commit()
        await db.refresh(green_valley)

    result = await db.execute(select(Farm).where(Farm.name == "Steppe Gold"))
    steppe_gold = result.scalar_one_or_none()
    if not steppe_gold:
        steppe_gold = Farm(name="Steppe Gold", region="Akmola", area_hectares=500.0)
        db.add(steppe_gold)
        await db.commit()
        await db.refresh(steppe_gold)

    result = await db.execute(select(Farm))
    farms_in_db = result.scalars().all()
    print("Farms in DB:", [(f.id, f.name) for f in farms_in_db])

    crops_data = [
        {"plant_name": "Wheat",     "harvest_year": 2023, "farm": sunrise_farm},
        {"plant_name": "Sunflower", "harvest_year": 2023, "farm": sunrise_farm},
        {"plant_name": "Barley",    "harvest_year": 2024, "farm": green_valley},
        {"plant_name": "Corn",      "harvest_year": 2024, "farm": green_valley},
        {"plant_name": "Rapeseed",  "harvest_year": 2023, "farm": steppe_gold},
        {"plant_name": "Wheat",     "harvest_year": 2024, "farm": steppe_gold},
    ]

    for c in crops_data:
        result = await db.execute(
            select(Crop).where(
                (Crop.plant_name == c["plant_name"]) &
                (Crop.farm_id == c["farm"].id)
            )
        )
        exists = result.scalar_one_or_none()
        if not exists:
            crop = Crop(
                plant_name=c["plant_name"],
                harvest_year=c["harvest_year"],
                farm_id=c["farm"].id
            )
            db.add(crop)
    await db.commit()


async def seed_receipt_for_dish(db: AsyncSession):
    # UUID существующего блюда
    dish_id = "7960bff0-2200-4989-ad28-9ef0d01e3d8a"

    # Проверяем, есть ли уже блюдо
    result = await db.execute(select(Dish).where(Dish.id == dish_id))
    print("dDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD", result)
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

async def run_seeders(db: AsyncSession):
    # await seed_farms(db)
    # await seed_crops(db)
    # await seed_dishes(db)
    # await seed_receipt_for_dish(db)
    await seed_roles(db)


async def main():
    async with AsyncSessionLocal() as db:
        await run_seeders(db)


if __name__ == "__main__":
    asyncio.run(main())
