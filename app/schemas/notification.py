from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class NotificationBase(BaseModel):
    user_id: UUID
    title: str
    message: str

class NotificationCreate(NotificationBase):
    pass

class NotificationUpdate(BaseModel):
    is_read: bool

class NotificationResponse(NotificationBase):
    id: UUID
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True