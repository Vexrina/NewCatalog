from jinja2 import Environment, FileSystemLoader
import os


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

    fileLoader = FileSystemLoader('templates')
    env = Environment(loader=fileLoader)

    rendered = env.get_template('homepage.html').render(
        header_items=header_items)

    filename = 'homepage.html'

    with open(f'./pages/{filename}', 'w', encoding='UTF-8') as f:
        f.write(rendered)


def generate_category_page(category: str) -> None:
    header_items = take_header_items()

    fileLoader = FileSystemLoader('templates')
    env = Environment(loader=fileLoader)

    first_cpu = {
        'Брэнд': 'AMD', 'Модель': '5800X',
        'Гнездо процессора': 'SocketAM4', 'Количество ядер': '8',
        'Количество потоков': '16', 'Частота': '3.8 ГГц и 4.7 ГГц в режиме Turbo',
        'L3 кэш': '32 МБ', 'Технологический процесс': '7 нм',
        'Множитель': 'разблокированный', 'Тепловыделение': '105 Вт',
        'Максимальная температура': '90 °С', 'Тип памяти': 'DDR4',
        'Поддержка частот памяти': '3200 МГц', 'Количество каналов памяти': '2',
        'Встроенное графическое ядро': 'отсутствует'}
    rendered = env.get_template('category.html').render(
        header_items=header_items,
        Category=category,
        items=[first_cpu]
    )

    with open(f'./pages/{category.lower()}.html', 'w',  encoding='UTF-8') as f:
        f.write(rendered)


generate_category_page('CPU')
