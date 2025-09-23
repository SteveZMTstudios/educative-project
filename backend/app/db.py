from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from .core.config import settings


DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{os.path.join('.', 'dev.db')}")

# For SQLite need check_same_thread
connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(DATABASE_URL, connect_args=connect_args, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
Base = declarative_base()


def init_db():
    # create tables
    Base.metadata.create_all(bind=engine)
