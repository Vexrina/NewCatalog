from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric, Float, SmallInteger
from sqlalchemy.orm import relationship

from .database import Base

class Stores(Base):
    __tablename__ = 'Stores'
    
    uuid = Column(Integer, primary_key=True,index=True)
    naming = Column(String, unique=True)
    
    store = relationship('CPU_Prices', back_populates='Store_owner')
    

class Cpus(Base):
    __tablename__ = 'CPU'

    uuid = Column(Integer, primary_key=True, index=True)
    brand = Column(String)
    model = Column(String, unique=True)

    specs = relationship('CPU_Specs', back_populates='CPU_owner')
    prices = relationship('CPU_Prices', back_populates='CPU_owner')


class Cpus_Specs(Base):
    __tablename__ = 'CPU_Specs'

    uuid = Column(Integer, primary_key=True, index=True)
    socket = Column(String)
    num_cores = Column(Integer)
    num_thr = Column(Integer)
    clock = Column(Float)
    cache = Column(Integer)
    nm = Column(SmallInteger)
    oveclock = Column(Boolean)
    tdp = Column(Integer)
    max_temp = Column(Integer)
    memory_type = Column(Integer)
    memory_clock = Column(Integer)
    memory_channels = Column(SmallInteger)
    videocore = Column(Boolean, default=False)
    model_videocore = Column(String)
    clock_videocore = Column(Integer)

    id_from = Column(Integer, ForeignKey('CPUs.uuid'))

    CPU_owner = relationship('CPUs', back_populates='specs')


class Cpus_prices(Base):
    __tablename__ = 'CPU_prices'

    uuid = Column(Integer, primary_key=True, index=True)
    price = Column(Numeric)

    store = Column(Integer, ForeignKey('Stores.uuid'))
    id_from = Column(Integer, ForeignKey('CPUs.uuid'))

    Store_owner = relationship('Stores', back_populates='store')
    CPU_owner = relationship('CPUs', back_populates='prices')