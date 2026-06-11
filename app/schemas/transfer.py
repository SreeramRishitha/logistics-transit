from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict
from app.models.enums import TransferStatus


class TransferBase(BaseModel):
    sender_id: Optional[UUID] = None
    receiver_id: Optional[UUID] = None
    request_id: Optional[UUID] = None
    status: Optional[TransferStatus] = TransferStatus.REQUESTED
    tracking_number: Optional[str] = None


class TransferCreate(TransferBase):
    sender_id: UUID
    receiver_id: UUID


class TransferUpdate(TransferBase):
    pass


class Transfer(TransferBase):
    id: UUID
    
    model_config = ConfigDict(from_attributes=True)
