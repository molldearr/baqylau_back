from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from data_access.db.base import Base


class Receipt(Base):
    __tablename__ = "receipts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)        # рецепт атауы
    instructions = Column(String, nullable=False) # дайындалу қадамдары
    cooking_time = Column(Integer)                # минутпен
    
    # АЛЫП ТАСТАУ КЕРЕК!!!!!!!!!!!!!!!!!!!
    difficulty = Column(String)                   # easy / medium / hard

    calorie = Column(Integer)

    dishes = relationship("Dish", back_populates="receipt")
