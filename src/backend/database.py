# from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# directory = Path(__file__).parent
# directory = directory / 'newcatalog_db.db'

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:postgres@localhost:8353/my_db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
