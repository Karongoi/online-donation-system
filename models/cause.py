from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Cause(Base):
    __tablename__ = 'causes'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    target_amount = Column(Integer, nullable=False)
    collected_amount = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    organiser_id = Column(Integer, ForeignKey('organisers.id'), nullable=False)  

    donations = relationship("Donation", back_populates="cause")
    organiser = relationship("Organiser", back_populates="causes")

    def __repr__(self):
        return f"<Cause(title='{self.title}', target={self.target_amount})>"
