from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime

from app.db.session import get_db
from app.api.dependencies.auth import get_current_user, RoleChecker
from app.models.enums import UserRole
from app.repositories.donation import DonationRepository
from app.repositories.inventory import InventoryRepository
from app.schemas.donation import DonationCreate, DonationResponse

router = APIRouter()
allow_staff = RoleChecker([UserRole.BLOOD_BANK, UserRole.ADMIN])

@router.post("/", response_model=DonationResponse)
async def create_donation(
    obj_in: DonationCreate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(allow_staff)
):
    donation_repo = DonationRepository(db)
    inventory_repo = InventoryRepository(db)
    
    # 1. Log the physical donation history record
    donation_data = obj_in.dict()
    expiry_date = donation_data.pop("expiry_date") # Remove it before saving to donation table
    donation_data["donation_date"] = datetime.utcnow()
    
    new_donation = await donation_repo.create(obj_in=donation_data)
    
    # 2. Automatically add the blood to the active inventory stock
    inventory_data = {
        "blood_bank_id": obj_in.blood_bank_id,
        "blood_group": obj_in.blood_group,
        "quantity_ml": obj_in.quantity_ml,
        "expiry_date": expiry_date.replace(tzinfo=None) # Strip timezone info
    }
    await inventory_repo.create(obj_in=inventory_data)
    
    return new_donation

@router.get("/", response_model=List[DonationResponse])
async def read_donations(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    repo = DonationRepository(db)
    return await repo.get_multi(skip=skip, limit=limit)