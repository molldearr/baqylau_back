from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from data_access.db.models.role import Role

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
