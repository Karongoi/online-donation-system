from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Cause(Base):
    __tablename__ = 'causes'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    goal_amount = Column(Integer)
    deadline = Column(DateTime)
    organiser_id = Column(Integer, ForeignKey('users.id'))

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    donations = relationship("Donation", back_populates="cause")
    organizer = relationship("User", back_populates="causes")

    def __repr__(self):
        return f"<Cause(title='{self.title}', goal={self.goal_amount})>"
