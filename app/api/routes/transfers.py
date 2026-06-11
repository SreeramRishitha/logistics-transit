from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies.auth import get_current_user, RoleChecker
from app.db.session import get_db
from app.models.enums import UserRole
from app.repositories.transfer import TransferRepository
from app.schemas.transfer import Transfer, TransferCreate, TransferUpdate

router = APIRouter()


@router.post("/", response_model=Transfer)
async def create_transfer(
    obj_in: TransferCreate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    repo = TransferRepository(db)
    return await repo.create(obj_in=obj_in.dict())


@router.get("/", response_model=List[Transfer])
async def read_transfers(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    repo = TransferRepository(db)
    return await repo.get_multi(skip=skip, limit=limit)


@router.patch("/{id}", response_model=Transfer)
async def update_transfer(
    id: UUID,
    obj_in: TransferUpdate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    repo = TransferRepository(db)
    db_obj = await repo.get(id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Transfer not found")
    return await repo.update(db_obj=db_obj, obj_in=obj_in.dict(exclude_unset=True))
