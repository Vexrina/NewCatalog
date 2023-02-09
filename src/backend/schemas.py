from pydantic import BaseModel
from decimal import *


class CpuSpecsBase(BaseModel):
    socket: str
    num_cores: int
    num_thr: int
    clock: float
    cache: int
    nm: int
    oveclock: bool
    tdp: int
    max_temp: int
    memory_type: int
    memory_clock: int
    memory_channels: int
    videocore: bool = False
    model_videocore: int
    clock_videocore: int


class CpuSpecsCreate(CpuSpecsBase):
    pass


class CpuSpecs(CpuSpecsBase):
    uuid: int
    owner_id: int

    class Config:
        orm_mode = True


class CpuPricesBase(BaseModel):
    price: Decimal
    store: int


class CpuPricesCreate(CpuSpecsBase):
    pass


class CpuPrices(CpuSpecsBase):
    uuid: int

    CPU_owner: int
    Store_owner: int

    class Config:
        orm_mode = True


class CpuBase(BaseModel):
    brand: str
    model: str


class Cpu(CpuBase):
    uuid: int
    specs: list[CpuSpecs] = []
    prices: list[CpuPrices] = []
