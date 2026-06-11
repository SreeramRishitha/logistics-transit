from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth, inventory, requests, donors, transfers, analytics,donations,notifications
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_STR}/openapi.json",
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth.router, prefix=f"{settings.API_STR}/auth", tags=["Authentication"])
app.include_router(inventory.router, prefix=f"{settings.API_STR}/inventory", tags=["Inventory"])
app.include_router(requests.router, prefix=f"{settings.API_STR}/requests", tags=["Requests"])
app.include_router(donors.router, prefix=f"{settings.API_STR}/donors", tags=["Donors"])
app.include_router(transfers.router, prefix=f"{settings.API_STR}/transfers", tags=["Transfers"])
app.include_router(analytics.router, prefix=f"{settings.API_STR}/analytics", tags=["Analytics"])
app.include_router(donations.router, prefix=f"{settings.API_STR}/donations", tags=["Donations"])
app.include_router(notifications.router, prefix=f"{settings.API_STR}/notifications", tags=["notifications"])


@app.get("/")
async def root():
    return {"message": "Welcome to BloodLink AI API"}
