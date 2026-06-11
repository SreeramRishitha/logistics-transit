from app.repositories.base import BaseRepository
from app.models.donation import Donation
from sqlalchemy.ext.asyncio import AsyncSession

class DonationRepository(BaseRepository[Donation]):
    def __init__(self, db: AsyncSession):
        super().__init__(Donation, db)