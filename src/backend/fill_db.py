import logging
from sqlalchemy.orm import Session

from src.backend import models
from src.backend.cruds import cpu_crud
from src.backend.schemas import cpu_schemas
from src.backend.parsers.new_old_keys import cpu_new_keys, cpu_old_keys
from src.backend.database import SessionLocal, engine
from src.backend.parsers.cpu_to_parse import intel, amd
from src.backend.parsers.parser import parsing, cpu


models.cpu_models.Base.metadata.create_all(bind=engine)
models.store_benchmarks_models.Base.metadata.create_all(bind=engine)
intels_cpu = intel
amds_cpu = amd


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


data = cpu(intels_cpu[0])
# print(data)

def rename_keys(specs: dict, old_key: list[str], new_keys: list[str]) -> dict:
    step = 0
    while step != len(specs):
        specs[new_keys[step]] = specs.pop(old_key[step])
        step += 1
    return specs


def switch_types(specs: dict, category: str) -> dict:
    match category:
        case 'cpu':
            specs['cache'] = specs['cache'][:-3]
            specs['nm'] = specs['nm'][:-3]
            match specs['overclock']:
                case 'заблокированный':
                    specs['overclock'] = 0
                case 'разблокированный':
                    specs['overclock'] = 1
            specs['tdp'] = specs['tdp'][:-3]
            specs['max_temp'] = specs['max_temp'][:-3]
            match specs['videocore']:
                case 'есть':
                    specs['videocore'] = 1
                case 'отсутствует':
                    specs['videocore'] = 0
            for key, value in specs.items():
                try:
                    specs[key] = int(value)
                except ValueError:
                    continue
    return specs


data = rename_keys(data, cpu_old_keys, cpu_new_keys)
data = switch_types(data, 'cpu')


def create_cpu(cpu_data: dict) -> models.cpu_models.Cpus:
    return cpu_crud.create_cpu(cpu_data)


def create_specs_cpu(cpu_id: int, specs: dict):
    return cpu_crud.create_cpu_specs(specs=specs, cpu_owner_id=cpu_id)


cpu = dict()
cpu['brand'] = data.pop('brand')
cpu['model'] = data.pop('model')
for k, v in data.items():
    print(f'{k}__{v}__{type(v)}')
id = create_cpu(cpu_data=cpu).uuid
print(id)
create_specs_cpu(specs=data, cpu_id=id)


def fill_db(links: list[str], category: str):
    try:
        datas = parsing(links, category)
        for step in range(len(datas)):
            datas[step] = rename_keys(datas[step], cpu_old_keys, cpu_new_keys)
            datas[step] = switch_types(datas[step], category)
            cpu = dict()
            cpu['brand'] = datas[step].pop('brand')
            cpu['model'] = datas[step].pop('model')
            id = create_cpu(cpu).uuid

    except Exception as err:
        logging.error(f'Bad status code: {type(err)}: {err}')
