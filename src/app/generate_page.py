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


# def generate_category_page(category: str) -> None:
#     header_items = take_header_items()

#     fileLoader = FileSystemLoader('templates')
#     env = Environment(loader=fileLoader)

#     links = [
#     'https://www.citilink.ru/product/processor-amd-s-ryzen-7-5800x-am4-100-000000063-3-8ghz-oem-1773839/properties/',
#     'https://www.citilink.ru/product/processor-amd-s-ryzen-7-3700x-am4-100-000000071-3-6ghz-oem-1804883/properties/',
#     'https://www.citilink.ru/product/processor-amd-s-ryzen-5-5600g-am4-100-000000252-3-9ghz-amd-radeon-oem-1773831/properties/',
#     'https://www.citilink.ru/product/processor-intel-s-pentium-gold-g6405-soc-1200-4-1ghz-iuhdg610-oem-1722989/properties/',
#     'https://www.citilink.ru/product/processor-intel-s-core-i5-11400f-soc-1200-2-6ghz-oem-1722999/properties/',
#     'https://www.citilink.ru/product/processor-intel-s-core-i5-12400f-soc-1700-2-5ghz-oem-1782240/properties/'
#     ]

#     data = []
#     for link in links:
#         data.append(get_data(link))
    
#     for item in data:
#         if len(item)==0:
#             data.remove(item)

#     rendered = env.get_template('category.html').render(
#         header_items=header_items,
#         Category=category,
#         items=data
#     )

#     with open(f'./pages/{category.lower()}.html', 'w',  encoding='UTF-8') as f:
#         f.write(rendered)
#     print('Html is rendered')


# generate_category_page('CPU')
