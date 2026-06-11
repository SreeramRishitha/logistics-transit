from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies.auth import get_current_user
from app.db.session import get_db
from app.schemas.user import User, UserCreate
from app.schemas.token import Token
from app.services.auth import AuthService

router = APIRouter()


@router.post("/register", response_model=User)
async def register(
    user_in: UserCreate, db: AsyncSession = Depends(get_db)
):
    auth_service = AuthService(db)
    return await auth_service.register_user(user_in)


@router.post("/login", response_model=Token)
async def login(
    db: AsyncSession = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    auth_service = AuthService(db)
    user = await auth_service.authenticate(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    return auth_service.create_token(user)


@router.get("/me", response_model=User)
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user
