from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from data_access.db.base import Base


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    created_at = Column(DateTime, default=datetime.now)

    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    dish_id = Column(UUID(as_uuid=True), ForeignKey("dishes.id"))

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    
    value = Column(Integer)

    dish = relationship("Dish", back_populates="ratings")

    user = relationship("User", back_populates="ratings")
