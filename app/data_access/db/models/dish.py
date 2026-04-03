from sqlalchemy import Column, ForeignKey, String, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from data_access.db.base import Base


class Dish(Base):
    __tablename__ = "dishes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    
    # difficulty = 

    receipt_id = Column(UUID(as_uuid=True), ForeignKey("receipts.id"))
    
    kitchen_id = Column(UUID(as_uuid=True), ForeignKey("kitchens.id"))

    images = relationship("DishImage", back_populates="dish")

    receipt = relationship("Receipt", back_populates="dishes")

    kitchen = relationship("Kitchen", back_populates="dishes")

    ratings = relationship("Rating", back_populates="dish")

    comments = relationship("Comment", back_populates="dish")
