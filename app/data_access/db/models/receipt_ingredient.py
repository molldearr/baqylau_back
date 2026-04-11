from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from data_access.db.base import Base


class ReceiptIngredient(Base):
    __tablename__ = "receipt_ingredients"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    receipt_id = Column(UUID(as_uuid=True), ForeignKey("receipts.id"))

    ingredient_id = Column(UUID(as_uuid=True), ForeignKey("ingredients.id"))

    quantity = Column(String)  # например: "200g", "1 tbsp", "по вкусу"

    receipt = relationship("Receipt", back_populates="receipt_ingredients")

    ingredient = relationship("Ingredient", back_populates="receipt_ingredients")
