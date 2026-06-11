from app.repositories.base import BaseRepository
from app.models.notification import Notification
from sqlalchemy.ext.asyncio import AsyncSession

class NotificationRepository(BaseRepository[Notification]):
    def __init__(self, db: AsyncSession):
        super().__init__(Notification, db)