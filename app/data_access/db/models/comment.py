from sqlalchemy import Column, ForeignKey, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from data_access.db.base import Base


class Comment(Base):
    __tablename__ = "comments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    text = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.now)

    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    dish_id = Column(UUID(as_uuid=True), ForeignKey("dishes.id"))

    dish = relationship("Dish", back_populates="comments")
