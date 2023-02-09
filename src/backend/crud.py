from sqlalchemy.orm import Session

from . import models, schemas


def create_cpu(db: Session, cpu: schemas.CpuCreate) -> models.Cpus:
    db_cpu = models.Cpus(brand=cpu.brand, model=cpu.model)
    db.add(db_cpu)
    db.commit()
    db.refresh(db_cpu)
    return db_cpu


def create_cpu_specs(db: Session, specs: schemas.CpuSpecsCreate, cpu_owner_id: int) -> models.Cpus_Specs:
    db_specs = models.Cpus_Specs(**specs.dict(), CPU_owner=cpu_owner_id)
    db.add(db_specs)
    db.commit()
    db.refresh()
    return db_specs


def get_cpu(db: Session, cpu_id: int) -> models.Cpus | None:
    return db.query(models.Cpus).filter(models.Cpus.uuid == cpu_id).first()


def get_cpu_by_model(db: Session, model: str) -> models.Cpus | None:
    return db.query(models.Cpus).filter(models.Cpus.model == model).first()


def get_cpu_by_brand(db: Session, brand: str) -> models.Cpus | None:
    return db.query(models.Cpus).filter(models.Cpus.brand == brand).first()


def get_cpus(db: Session, skip: int = 0, limit: int = 100) -> list[models.Cpus]:
    return db.query(models.Cpus).offset(skip).limit(limit).all()


def get_cpu_specs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cpus.specs).offset(skip).limit(limit).all()
