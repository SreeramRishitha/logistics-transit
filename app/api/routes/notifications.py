from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.api.dependencies.auth import get_current_user
from app.repositories.notification import NotificationRepository
from app.schemas.notification import NotificationCreate, NotificationResponse, NotificationUpdate

router = APIRouter()

@router.post("/", response_model=NotificationResponse)
async def create_notification(
    obj_in: NotificationCreate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    repo = NotificationRepository(db)
    # Convert the Pydantic schema into a dictionary before creating
    return await repo.create(obj_in=obj_in.dict())

@router.get("/", response_model=List[NotificationResponse])
async def read_my_notifications(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    # For a hackathon MVP, we can fetch notifications matching the logged-in user's ID
    repo = NotificationRepository(db)
    all_notifications = await repo.get_multi()
    return [n for n in all_notifications if n.user_id == current_user.id]