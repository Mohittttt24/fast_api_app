from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import os

# Read database URL from environment or default to a local SQLite file for development
SQLALCHEMY_DATABASE_URL = 

# SQLite needs check_same_thread when used with SQLAlchemy in some environments


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()