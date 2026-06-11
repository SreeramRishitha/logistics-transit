from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies.auth import get_current_user, RoleChecker
from app.db.session import get_db
from app.models.enums import UserRole
from app.repositories.inventory import InventoryRepository
from app.schemas.inventory import BloodInventory, BloodInventoryCreate, BloodInventoryUpdate

router = APIRouter()
allow_blood_bank_admin = RoleChecker([UserRole.BLOOD_BANK, UserRole.ADMIN])


@router.post("/", response_model=BloodInventory)
async def create_inventory(
    obj_in: BloodInventoryCreate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(allow_blood_bank_admin)
):
    repo = InventoryRepository(db)
# 1. Convert the Pydantic model to a standard dictionary
    inventory_data = obj_in.dict()
    
    # 2. Strip the timezone info from expiry_date if it exists
    if inventory_data.get("expiry_date") and inventory_data["expiry_date"].tzinfo is not None:
        inventory_data["expiry_date"] = inventory_data["expiry_date"].replace(tzinfo=None)
        
    # 3. Pass the cleaned dictionary to your repository
    return await repo.create(obj_in=inventory_data)

@router.get("/", response_model=List[BloodInventory])
async def read_inventory(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    repo = InventoryRepository(db)
    return await repo.get_multi(skip=skip, limit=limit)


@router.put("/{id}", response_model=BloodInventory)
async def update_inventory(
    id: UUID,
    obj_in: BloodInventoryUpdate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(allow_blood_bank_admin)
):
    repo = InventoryRepository(db)
    db_obj = await repo.get(id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return await repo.update(db_obj=db_obj, obj_in=obj_in.dict(exclude_unset=True))


@router.delete("/{id}", response_model=BloodInventory)
async def delete_inventory(
    id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(allow_blood_bank_admin)
):
    repo = InventoryRepository(db)
    return await repo.remove(id=id)
