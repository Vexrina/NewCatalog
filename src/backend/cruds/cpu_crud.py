from typing import Type, Any, List

from src.backend.models import cpu_models
from src.backend.models.cpu_models import Cpus
from src.backend.schemas import cpu_schemas
from sqlalchemy.orm import Session
from src.backend.database import engine


def create_cpu(cpu: dict) -> cpu_models.Cpus:
    with Session(engine) as db:
        db_cpu = cpu_models.Cpus(brand=cpu['brand'], model=cpu['model'], image=cpu['image'])
        db.add(db_cpu)
        db.commit()
        db.refresh(db_cpu)
        print(f'{cpu["brand"]} - {cpu["model"]} is a added to database')
        return db_cpu


def create_cpu_specs(specs: dict, cpu_owner_id: int) -> cpu_models.Cpus_Specs:
    with Session(engine) as db:
        cpu_owner = get_cpu(db, cpu_owner_id)
        db_specs = cpu_models.Cpus_Specs(
            CPU_owner=cpu_owner,
            socket=specs['socket'],
            num_cores=specs['num_cores'],
            num_thr=specs['num_thr'],
            clock=specs['clock'],
            cache=specs['cache'],
            nm=specs['nm'],
            overclock=specs['overclock'],
            tdp=specs['tdp'],
            max_temp=specs['max_temp'],
            memory_type=specs['memory_type'],
            memory_clock=specs['memory_clock'],
            memory_channels=specs['memory_channels'],
            videocore=specs['videocore'],
            model_videocore=specs['model_videocore'],
            clock_videocore=specs['clock_videocore'],
        )
        db.add(db_specs)
        db.commit()
        db.refresh(db_specs)
        return db_specs


def get_cpu(db: Session, cpu_id: int) -> cpu_models.Cpus | None:
    return db.query(cpu_models.Cpus).filter(cpu_models.Cpus.uuid == cpu_id).first()


def get_cpu_by_model(model: str):
    with Session(engine) as db:
        return db.query(cpu_models.Cpus).filter(cpu_models.Cpus.model == model).first()


def get_cpu_by_brand(brand: str):
    with Session(engine) as db:
        return db.query(cpu_models.Cpus).filter(cpu_models.Cpus.brand == brand).all()


def get_cpus(skip: int = 0, limit: int = 100):
    with Session(engine) as db:
        return db.query(cpu_models.Cpus).offset(skip).limit(limit).all()


def get_cpu_specs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(cpu_models.Cpus.specs).offset(skip).limit(limit).all()


def get_cpu_specs_by_cpuid(cpu_id: int):
    with Session(engine) as db:
        return db.query(cpu_models.Cpus_Specs).filter(cpu_models.Cpus_Specs.cpu_id == cpu_id).first()
