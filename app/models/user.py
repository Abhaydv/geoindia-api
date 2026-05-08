from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # 🔗 relationship with APIKey
    api_keys = relationship("APIKey", back_populates="user", cascade="all, delete")