from typing import List, Dict, Any
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.inventory import InventoryRepository
from app.repositories.request import RequestRepository
from app.repositories.user import UserRepository
from app.models.enums import BloodGroup, UserRole


class MatchingService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.inventory_repo = InventoryRepository(db)
        self.request_repo = RequestRepository(db)
        self.user_repo = UserRepository(db)

    async def find_matches(self, request_id: UUID) -> List[Dict[str, Any]]:
        request = await self.request_repo.get(request_id)
        if not request:
            return []

        matches = []

        # 1. Search Blood Banks
        inventory_matches = await self.inventory_repo.get_by_blood_group(request.blood_group)
        for inv in inventory_matches:
            if inv.quantity_ml >= request.quantity_ml:
                matches.append({
                    "type": "blood_bank",
                    "source_id": inv.blood_bank_id,
                    "available_ml": inv.quantity_ml,
                    "expiry_date": inv.expiry_date,
                    "score": 100  # Highest score for immediate availability
                })

        # 2. Search Donors (Placeholder logic for proximity)
        # In a real app, you'd use PostGIS or a Geo library
        donors = await self.user_repo.get_multi(limit=50)  # Simplified for demo
        for donor in donors:
            if donor.role == UserRole.DONOR:
                # Assuming donors have a 'blood_group' attribute (need to add to model if not there)
                # For this hackathon, we'll assume they match for now or filter by a placeholder
                matches.append({
                    "type": "donor",
                    "source_id": donor.id,
                    "full_name": donor.full_name,
                    "score": 50
                })

        # Sort matches by score descending
        matches.sort(key=lambda x: x["score"], reverse=True)
        return matches
