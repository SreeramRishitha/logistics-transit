from app.database.database import Base, engine
from app.models import *  # Import your models here

# Create all tables
Base.metadata.create_all(bind=engine)