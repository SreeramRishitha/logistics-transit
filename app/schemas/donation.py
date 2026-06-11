from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from app.models.enums import BloodGroup

class DonationBase(BaseModel):
    donor_id: UUID
    blood_bank_id: UUID
    blood_group: BloodGroup
    quantity_ml: int

class DonationCreate(DonationBase):
    expiry_date: datetime  # Captured to automatically update inventory later if needed

class DonationResponse(DonationBase):
    id: UUID
    donation_date: datetime

    class Config:
        from_attributes = True