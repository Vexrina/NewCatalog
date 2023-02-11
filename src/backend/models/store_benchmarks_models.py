from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.backend.database import Base


class Stores(Base):
    __tablename__ = 'Stores'

    uuid = Column(Integer, primary_key=True, index=True)
    naming = Column(String, unique=True)

    store = relationship('Cpus_prices', back_populates='Store_owner')
