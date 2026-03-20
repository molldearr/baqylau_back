import asyncio
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
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


async def run_seeders(db: AsyncSession):
    await seed_farms(db)
    await seed_crops(db)


async def main():
    async with AsyncSessionLocal() as db:
        await run_seeders(db)


if __name__ == "__main__":
    asyncio.run(main())