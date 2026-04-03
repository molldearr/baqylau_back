from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from data_access.db.models.difficulty import Difficulty

async def seed_difficulties(db: AsyncSession):
    difficulties_data = ["easy", "medium", "hard"]

    for name in difficulties_data:
        result = await db.execute(select(Difficulty).where(Difficulty.name == name))
        exists = result.scalar_one_or_none()
        if not exists:
            diff = Difficulty(name=name)
            db.add(diff)

    await db.commit()
    print("Difficulties seeded!")
