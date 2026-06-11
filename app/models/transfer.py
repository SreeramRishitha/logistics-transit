from sqlalchemy import Column, String, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.models.base import Base
from app.models.enums import TransferStatus


class Transfer(Base):
    __tablename__ = "transfers"

    sender_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    receiver_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    request_id = Column(UUID(as_uuid=True), ForeignKey("blood_requests.id"), nullable=True)
    status = Column(Enum(TransferStatus), default=TransferStatus.REQUESTED)
    tracking_number = Column(String, unique=True, index=True)
    
    sender = relationship("User", foreign_keys=[sender_id], backref="transfers_sent")
    receiver = relationship("User", foreign_keys=[receiver_id], backref="transfers_received")
    request = relationship("BloodRequest", backref="transfers")
