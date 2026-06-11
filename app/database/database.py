from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = "postgresql://chakri:1a2b3c4$@localhost/fastapi_issue_tracker_db"

engine = create_engine(DB_URL)#a connection to PostgreSQL

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)#a session factory

Base = declarative_base()#a base class for models
