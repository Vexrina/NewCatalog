from jinja2 import Environment, FileSystemLoader
import os
from typing import List, Type
from src.backend.models import cpu_models

def take_header_items() -> list[dict]:
    header_items = []

    for __, __, files in os.walk('./static/img/svg/'):
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


def generate_homepage() -> None:
    header_items = take_header_items()

    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    rendered = env.get_template('homepage.html').render(
        header_items=header_items)

    filename = 'homepage.html'

    with open(f'./pages/{filename}', 'w', encoding='UTF-8') as f:
        f.write(rendered)


def generate_category_page(query_result: list[Type[cpu_models.Cpus]], category: str) -> None:
    header_items = take_header_items()

    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)


    data = []
    for link in links:
        data.append(get_data(link))

    for item in data:
        if len(item)==0:
            data.remove(item)

    rendered = env.get_template('category.html').render(
        header_items=header_items,
        Category=category,
        items=data
    )

    with open(f'./pages/{category.lower()}.html', 'w',  encoding='UTF-8') as f:
        f.write(rendered)
    print('Html is rendered')


# generate_category_page('CPU')
