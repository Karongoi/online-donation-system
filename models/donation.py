from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Donation(Base):
    __tablename__ = 'donations'

    id = Column(Integer, primary_key=True)
    donor_id = Column(Integer, ForeignKey('donors.id'))  
    cause_id = Column(Integer, ForeignKey('causes.id'))
    amount = Column(Integer, nullable=False)
    donated_at = Column(DateTime, default=datetime.utcnow)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    donor = relationship("Donor", back_populates="donations")  
    cause = relationship("Cause", back_populates="donations")

    def __repr__(self):
        return f"<Donation(donor_id={self.donor_id}, cause_id={self.cause_id}, amount={self.amount})>"
