from sqlalchemy import Column, Integer, Enum, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.models.base import Base
from app.models.enums import BloodGroup


class Donation(Base):
    __tablename__ = "donations"

    donor_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    blood_bank_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    blood_group = Column(Enum(BloodGroup), nullable=False)
    quantity_ml = Column(Integer, nullable=False)
    donation_date = Column(DateTime, nullable=False)
    
    donor = relationship("User", foreign_keys=[donor_id], backref="donations_made")
    blood_bank = relationship("User", foreign_keys=[blood_bank_id], backref="donations_received")
