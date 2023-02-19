from pathlib import Path

from jinja2 import Environment, FileSystemLoader
import os
from typing import List, Type, Any
from src.backend.models import cpu_models
from src.backend.cruds import cpu_crud


directory = Path(__file__).parent.parent


def take_header_items() -> list[dict]:
    header_items = []

    for __, __, files in os.walk(directory/'static/img/svg/'):
        for filename in files:
            if filename != 'red_splash.svg':
                header_items.append(
                    {
                        'alt': filename[2:-4].lower(),
                        'class': f'header__{filename[2:].lower()}-pic',
                        'src': f'../static/img/svg/{filename}'
                    }
                )
    return header_items


def take_db_items(filters: dict | None, query: str = ''):
    if filters is None:
        filters = {}
    match query:
        case 'cpu':
            if len(filters) == 0:
                cpus = cpu_crud.get_cpus()
                data = []
                for cpu in cpus:
                    temp = {
                        'brand': cpu.brand,
                        'model': cpu.model,
                        'image': cpu.image,
                        'specs': cpu_crud.get_cpu_specs_by_cpuid(cpu.uuid)
                    }
                    data.append(temp)
                return data
            elif 'brand' in filters and 'model' not in filters:
                cpus = cpu_crud.get_cpu_by_brand(filters['brand'])
                data = []
                for cpu in cpus:
                    temp = {
                        'brand': cpu.brand,
                        'model': cpu.model,
                        'image': cpu.image,
                        'specs': cpu_crud.get_cpu_specs_by_cpuid(cpu.uuid)
                    }
                    data.append(temp)
                return data
            elif 'model' in filters:
                cpu = cpu_crud.get_cpu_by_model(filters['model'])
                data = {
                    'brand': cpu.brand,
                    'model': cpu.model,
                    'image': cpu.image,
                    'specs': cpu_crud.get_cpu_specs_by_cpuid(cpu.uuid)
                }
                return data
            else:
                raise ValueError('Not implemented')
        case 'gpu':
            pass
        case 'ram':
            pass
        case 'mb':
            pass
        case 'ssd':
            pass
        case 'hdd':
            pass
        case 'pu':
            pass
        case 'fan':
            pass
        case _:
            pass


def generate_homepage() -> None:
    header_items = take_header_items()

    file_loader = FileSystemLoader(directory/'templates')
    env = Environment(loader=file_loader)

    rendered = env.get_template('homepage.html').render(
        header_items=header_items)

    filename = 'homepage.html'

    with open(directory/'pages'/filename, 'w', encoding='UTF-8') as f:
        f.write(rendered)


def generate_category_page(category: str) -> None:
    header_items = take_header_items()

    file_loader = FileSystemLoader(directory/'templates')
    env = Environment(loader=file_loader)

    data = take_db_items(query='cpu', filters=None)

    rendered = env.get_template('category.html').render(
        header_items=header_items,
        Category=category,
        items=data
    )

    with open(f'./pages/{category.lower()}.html', 'w',  encoding='UTF-8') as f:
        f.write(rendered)
    print('Html is rendered')

