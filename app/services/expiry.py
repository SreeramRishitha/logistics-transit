from datetime import datetime, timedelta
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.inventory import InventoryRepository
from app.models.inventory import BloodInventory


class ExpiryService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.inventory_repo = InventoryRepository(db)

    async def get_expiring_inventory(self, threshold_days: int = 7) -> List[BloodInventory]:
        threshold_date = datetime.utcnow() + timedelta(days=threshold_days)
        # Assuming the inventory repo has a method for this, or we use a filter here
        from sqlalchemy import select
        query = select(BloodInventory).where(BloodInventory.expiry_date <= threshold_date)
        result = await self.db.execute(query)
        return list(result.scalars().all())

    async def check_for_expiry_alerts(self):
        # Logic to return count or list of alerts
        expiring = await self.get_expiring_inventory()
        return {
            "total_alerts": len(expiring),
            "items": expiring
        }
