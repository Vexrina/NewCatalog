from pydantic import BaseModel
from decimal import *

from sqlalchemy.orm.collections import InstrumentedList


class CpuSpecsBase(BaseModel):
    socket: str
    num_cores: int
    num_thr: int
    cache: int
    clock: str
    nm: int
    overclock: int
    tdp: int
    max_temp: int
    memory_type: str
    memory_clock: str
    memory_channels: int
    videocore: int = 0
    model_videocore: str | None
    clock_videocore: str | None


class CpuSpecsCreate(CpuSpecsBase):
    pass


class CpuSpecs(CpuSpecsBase):
    uuid: int
    owner_id: int

    class Config:
        orm_mode = True


# class CpuPricesBase(BaseModel):
#     price: Decimal
#     store: int
#
#
# class CpuPricesCreate(CpuSpecsBase):
#     pass
#
#
# class CpuPrices(CpuSpecsBase):
#     uuid: int
#
#     CPU_owner: int
#     Store_owner: int
#
#     class Config:
#         orm_mode = True


class CpuBase(BaseModel):
    brand: str
    model: str
    images: str


class CpuCreate(CpuBase):
    pass


class Cpu(CpuBase):
    uuid: int
    specs: CpuSpecs

    class Config:
        orm_mode = True
