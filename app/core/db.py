from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:system@127.0.0.1:5432/geoindia"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True   
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()