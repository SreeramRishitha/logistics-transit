from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict
from app.models.enums import BloodGroup


class BloodInventoryBase(BaseModel):
    blood_group: Optional[BloodGroup] = None
    quantity_ml: Optional[int] = None
    expiry_date: Optional[datetime] = None


class BloodInventoryCreate(BloodInventoryBase):
    blood_bank_id: UUID
    blood_group: BloodGroup
    quantity_ml: int
    expiry_date: datetime


class BloodInventoryUpdate(BloodInventoryBase):
    pass


class BloodInventory(BloodInventoryBase):
    id: UUID
    blood_bank_id: UUID
    
    model_config = ConfigDict(from_attributes=True)
