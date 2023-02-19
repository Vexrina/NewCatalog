import pathlib

from src.backend import models
from src.backend.cruds import cpu_crud
from src.backend.parsers.new_old_keys import cpu_new_keys, cpu_old_keys
from src.backend.database import SessionLocal, engine

models.cpu_models.Base.metadata.create_all(bind=engine)
models.store_benchmarks_models.Base.metadata.create_all(bind=engine)

root = pathlib.Path(__file__).parent

image_path = root / 'images' / 'cpu'
print(image_path)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def rename_keys(specs: dict, old_key: list[str], new_keys: list[str]) -> dict:
    step = 0
    if 'L2 кэш' in specs:
        specs.pop('L2 кэш')
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
                    specs['model_videocore'] = None
                    specs['clock_videocore'] = None
            for key, value in specs.items():
                try:
                    specs[key] = int(value)
                except ValueError:
                    continue
                except TypeError:
                    continue
    return specs


def create_cpu(cpu_data: dict) -> models.cpu_models.Cpus:
    return cpu_crud.create_cpu(cpu_data)


def create_specs_cpu(cpu_id: int, specs: dict) -> models.cpu_models.Cpus_Specs:
    return cpu_crud.create_cpu_specs(specs=specs, cpu_owner_id=cpu_id)


def fill_db(datas: list[dict], category: str):
    match category:
        case 'cpu':
            for step in range(len(datas)):
                datas[step] = rename_keys(datas[step], cpu_old_keys, cpu_new_keys)
                datas[step] = switch_types(datas[step], category)
                cpu_main_data = {
                    'brand': datas[step].pop('brand'),
                    'image': f'{image_path}\\{datas[step]["model"]}',
                    'model': datas[step].pop('model')}
                cpu_id = create_cpu(cpu_main_data).uuid
                create_specs_cpu(specs=datas[step], cpu_id=cpu_id)
        case _:
            raise ValueError('not implemented')
