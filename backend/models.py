from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric, LargeBinary
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class Cpus(Base):
    __tablename__ = 'cpus'

    uuid = Column(Integer, primary_key=True, index=True)
    brand = Column(String)
    model = Column(String, unique=True)

    specs = relationship('Cpus_Specs', back_populates='owner')


class Cpus_Specs(Base):
    __tablename__ = 'cpus_cpecs'

    uuid = Column(Integer, primary_key=True, index=True)
    socket = Column(String)
    num_cores = Column(Integer)
    num_thr = Column(Integer)
    clock = Column(String)
    cache = Column(Integer)
    nm = Column(Integer)
    oveclock = Column(Boolean)
    tdp = Column(Integer)
    max_temp = Column(Integer)
    memory_time = Column(Integer)
    memory_clock = Column(Integer)
    memory_channels = Column(Integer)
    videocore = Column(Boolean, default=False)
    model_videocore = Column(String)
    clock_videocore = Column(String)

    id_from = Column(Integer, ForeignKey('Cpus.uuid'))

    owner = relationship('Cpus', back_populates='cpus_specs')


class cpus_prices(Base):
    __tablename__ = 'cpus_prices'

    uuid = Column(Integer, primary_key=True, index=True)
    dns = Column(Numeric)
    online_trade = Column(Numeric)
    regard = Column(Numeric)
    citilink = Column(Numeric)

    id_from = Column(Integer, ForeignKey('Cpus.uuid'))
