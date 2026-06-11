from typing import List
from sqlalchemy import select
from app.models.inventory import BloodInventory
from app.models.enums import BloodGroup
from app.repositories.base import BaseRepository
from datetime import datetime


class InventoryRepository(BaseRepository[BloodInventory]):
    def __init__(self, db):
        super().__init__(BloodInventory, db)

    async def get_by_blood_group(self, blood_group: BloodGroup) -> List[BloodInventory]:
        query = select(self.model).where(self.model.blood_group == blood_group)
        result = await self.db.execute(query)
        return list(result.scalars().all())

    async def get_expiring_soon(self, days: int = 7) -> List[BloodInventory]:
        # Implementation for expiry monitoring
        pass
