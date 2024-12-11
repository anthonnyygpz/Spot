from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from ..config import get_settings

settings = get_settings()

engine = create_engine(
    settings.DATABASE_URL, pool_pre_ping=True, pool_size=5, max_overflow=10
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
