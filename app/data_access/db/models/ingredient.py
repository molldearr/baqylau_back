from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from data_access.db.base import Base


class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)

    receipt_ingredients = relationship(
        "ReceiptIngredient",
        back_populates="ingredient"
    )
