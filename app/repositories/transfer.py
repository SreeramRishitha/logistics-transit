from typing import List
from sqlalchemy import select
from app.models.transfer import Transfer
from app.models.enums import TransferStatus
from app.repositories.base import BaseRepository


class TransferRepository(BaseRepository[Transfer]):
    def __init__(self, db):
        super().__init__(Transfer, db)

    async def get_by_sender(self, sender_id) -> List[Transfer]:
        query = select(self.model).where(self.model.sender_id == sender_id)
        result = await self.db.execute(query)
        return list(result.scalars().all())

    async def get_by_status(self, status: TransferStatus) -> List[Transfer]:
        query = select(self.model).where(self.model.status == status)
        result = await self.db.execute(query)
        return list(result.scalars().all())
