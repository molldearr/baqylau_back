import asyncio
from sqlalchemy import UUID, select
from sqlalchemy.ext.asyncio import AsyncSession
from data_access.db.models.kitchen import Kitchen


async def seed_kitchens(db: AsyncSession):
    kitchens_data = [
        "Italian",
        "Japanese",
        "American",
        "French",
        "Mexican"
    ]

    for title in kitchens_data:
        result = await db.execute(select(Kitchen).where(Kitchen.title == title))
        exists = result.scalar_one_or_none()
        if not exists:
            kitchen = Kitchen(title=title)
            db.add(kitchen)

    await db.commit()
    print("Kitchens seeded!")
