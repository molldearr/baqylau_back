from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from data_access.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    avatar_url = Column(String(500))
    
    role_id = Column(UUID(as_uuid=True), ForeignKey("roles.id"))

    roles = relationship("Role", back_populates="user")

    tutor_profile = relationship("Tutor", back_populates="user", uselist=False)
