from sqlalchemy import Column, String, Boolean, Enum
from app.models.base import Base
from app.models.enums import UserRole


class User(Base):
    __tablename__ = "users"

    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(Enum(UserRole), default=UserRole.DONOR)
    address = Column(String)
    phone_number = Column(String)
    
    # Specific to hospitals/blood banks
    license_number = Column(String, nullable=True)
