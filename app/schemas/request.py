from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict
from app.models.enums import BloodGroup, RequestStatus, RequestPriority


class BloodRequestBase(BaseModel):
    blood_group: Optional[BloodGroup] = None
    quantity_ml: Optional[int] = None
    status: Optional[RequestStatus] = RequestStatus.PENDING
    priority: Optional[RequestPriority] = RequestPriority.NORMAL
    reason: Optional[str] = None


class BloodRequestCreate(BloodRequestBase):
    hospital_id: UUID
    blood_group: BloodGroup
    quantity_ml: int


class BloodRequestUpdate(BloodRequestBase):
    pass


class BloodRequest(BloodRequestBase):
    id: UUID
    hospital_id: UUID
    
    model_config = ConfigDict(from_attributes=True)
