from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship
from database import Base
import enum
from datetime import datetime

class RoleEnum(enum.Enum):
    donor = "donor"
    organizer = "organizer"

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    donations = relationship("Donation", back_populates="user")
    causes = relationship("Cause", back_populates="organizer")

    def __repr__(self):
        return f"<User(username='{self.username}', role='{self.role.value}')>"
