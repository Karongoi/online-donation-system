# organiser.py (or wherever your Organiser model is)

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Organiser(Base):
    __tablename__ = 'organisers'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    causes = relationship("Cause", back_populates="organiser")

    def __repr__(self):
        return f"<Organiser(username='{self.username}', email='{self.email}')>"

