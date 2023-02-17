from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, SmallInteger
from sqlalchemy.orm import relationship

from src.backend.database import Base


class Cpus(Base):
    __tablename__ = 'CPUs'

    uuid = Column(Integer, primary_key=True, index=True)
    brand = Column(String)
    model = Column(String, unique=True)
    image = Column(String, unique=True, nullable=True)

    specs = relationship('Cpus_Specs', back_populates='CPU_owner')
    prices = relationship('Cpus_prices', back_populates='CPU_owner')


class Cpus_Specs(Base):
    __tablename__ = 'CPU_Specs'

    uuid = Column(Integer, primary_key=True, index=True)
    cpu_id = Column(Integer, ForeignKey('CPUs.uuid'))
    socket = Column(String)
    num_cores = Column(Integer)
    num_thr = Column(Integer)
    cache = Column(Integer)
    clock = Column(String)
    nm = Column(Integer)
    overclock = Column(Integer)
    tdp = Column(Integer)
    max_temp = Column(Integer)
    memory_type = Column(String)
    memory_clock = Column(String)
    memory_channels = Column(Integer)
    videocore = Column(Integer, default=0)
    model_videocore = Column(String)
    clock_videocore = Column(String)

    CPU_owner = relationship('Cpus', back_populates='specs')


class Cpus_prices(Base):
    __tablename__ = 'CPU_prices'

    uuid = Column(Integer, primary_key=True, index=True)
    price = Column(Numeric)

    store = Column(Integer, ForeignKey('Stores.uuid'))
    id_from = Column(Integer, ForeignKey('CPUs.uuid'))

    Store_owner = relationship('Stores', back_populates='store')
    CPU_owner = relationship('Cpus', back_populates='prices')
