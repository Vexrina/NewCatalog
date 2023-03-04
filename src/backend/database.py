from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys


windows_path = "sqlite:///C:\\Users\\Vexrina\\Desktop\\projects\\NewCatalog\\src\\backend\\newcatalog_db.db"
linux_path = "sqlite:////home/vexrinawlw/Документы/projects/NewCatalog/src/backend/newcatalog_db.db"
if sys.platform == 'linux':
    SQLALCHEMY_DATABASE_URL = linux_path
else:
    SQLALCHEMY_DATABASE_URL = windows_path


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
