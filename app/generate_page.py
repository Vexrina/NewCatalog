from jinja2 import Environment, FileSystemLoader
import os

def generate_homepage() -> None:
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

    fileLoader = FileSystemLoader('templates')
    env = Environment(loader=fileLoader)

    rendered = env.get_template('homepage.html').render(
        header_items=header_items)

    filename = 'homepage.html'

    with open(f'./pages/{filename}', 'w') as f:
        f.write(rendered)
