from sqlalchemy import Column, ForeignKey, String, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from data_access.db.base import Base


class DishImage(Base):
    __tablename__ = "dish_images"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    image_path = Column(String, nullable=False)
    
    dish_id = Column(UUID(as_uuid=True), ForeignKey("dishes.id"))

    dish = relationship("Dish", back_populates="images")
