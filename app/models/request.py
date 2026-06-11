from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.models.base import Base
from app.models.enums import BloodGroup, RequestStatus, RequestPriority


class BloodRequest(Base):
    __tablename__ = "blood_requests"

    hospital_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    blood_group = Column(Enum(BloodGroup), nullable=False)
    quantity_ml = Column(Integer, nullable=False)
    status = Column(Enum(RequestStatus), default=RequestStatus.PENDING)
    priority = Column(Enum(RequestPriority), default=RequestPriority.NORMAL)
    reason = Column(String, nullable=True)
    
    hospital = relationship("User", backref="requests")
