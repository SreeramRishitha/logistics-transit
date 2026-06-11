from typing import List
from sqlalchemy import select
from app.models.request import BloodRequest
from app.models.enums import BloodGroup, RequestStatus
from app.repositories.base import BaseRepository


class RequestRepository(BaseRepository[BloodRequest]):
    def __init__(self, db):
        super().__init__(BloodRequest, db)

    async def get_by_hospital(self, hospital_id) -> List[BloodRequest]:
        query = select(self.model).where(self.model.hospital_id == hospital_id)
        result = await self.db.execute(query)
        return list(result.scalars().all())

    async def get_pending_by_group(self, blood_group: BloodGroup) -> List[BloodRequest]:
        query = select(self.model).where(
            self.model.blood_group == blood_group,
            self.model.status == RequestStatus.PENDING
        )
        result = await self.db.execute(query)
        return list(result.scalars().all())
