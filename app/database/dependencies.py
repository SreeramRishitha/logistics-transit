from sqlalchemy.orm import Session
from app.database.database import SessionLocal

def get_db():
    db = SessionLocal()  # Create a new database session
    try:
        yield db  # Provide the session to the route
    finally:
        db.close()  # Close the session after the request is processed