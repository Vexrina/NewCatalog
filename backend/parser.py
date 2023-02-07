from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
import platform
import time

# some options for webdriver
chrome_options = Options()
chrome_options.add_argument("--headless")

service = Service(ChromeDriverManager().install())

LOGGER.setLevel(logging.WARNING)


def get_data(link: str) -> list[str]:
    driver = webdriver.Chrome(service=service)  # add options=chrome_options
    driver.get(link)
    time.sleep(30)
    divs = driver.find_elements(By.CLASS_NAME, 'SpecificationsFull')
    specs = []
    for div in divs:
        specs.append(div.get_attribute('outerHTML'))
    driver.close()
    # return specs
    full_spec = []
    for spec in specs:
        a = spec.split('\n')
        for item in a:
            full_spec.append(item)

    k = 0
    while (k != len(full_spec)):
        full_spec[k] = full_spec[k].strip()
        if full_spec[k].find('</div>') == 0:
            full_spec.pop(k)
        elif full_spec[k].find('</h4>') == 0:
            full_spec.pop(k)
        elif full_spec[k].find('<div') == 0:
            full_spec.pop(k)
        else:
            k += 1

    return full_spec


def del_title(titles: list[str], full_spec: list[str]) -> dict:
    for title in titles:
        if title in full_spec:
            full_spec.remove(title)
    result = {}
    for i in range(1, len(full_spec), 2):
        result[full_spec[i-1]] = full_spec[i]
    return result


def del_keys(useless_keys: list[str], preresult: dict) -> dict:
    for key in useless_keys:
        if key in preresult:
            preresult.pop(key)

    return preresult


def fan(link: str) -> dict:
    full_spec = get_data(link)

    titles = [
        'Дополнительные характеристики',
        'Упаковка', 'Размеры, вес',
        'Электропитание', 'Конструкция',
        'Совместимость', 'Основные параметры',
    ]
    result = del_title(titles, full_spec)

    useless_key = [
        'Направление выдува', 'Воздушный поток',
        'Тип подшипника', '-', 'Вес',
        'Вес упаковки (ед)', 'Гарантия',
        'Длина кулера', 'Ширина кулера',
        'Воздушный поток вентилятора',
    ]
    for k, __ in result.items():
        if k.find('Совместимость') != -1:
            useless_key.append(k)

    result = del_keys(useless_key, result)

    return result


def cpu(link: str) -> dict:
    titles = [
        'Спецификация памяти',
        'Спецификация PCI Express',
        'Встроенная графика'
    ]
    useless_keys = [
        'Ядро', 'Разрядность вычислений', 'Тип поставки',
        'Поддержка памяти ECC', 'Версия PCI Express',
        'Количество каналов PCI Express', 'Пропускная способность шины (GT/s)',
        'Конфигурация PCI Express', 'Пропускная способность памяти',
        'Максимальный объем видеопамяти', 'Максимальный объем памяти',
        'Тепловыделение в режиме Turbo'
    ]

    full_spec = get_data(link)
    preresult = del_title(titles, full_spec)
    return del_keys(useless_keys, preresult)


def gpu(link:str) -> dict:
    titles = [
        'Спецификация памяти',
        'Спецификация PCI Express',
        'Встроенная графика',
        'Производитель и модель графического процессора.',
        'Максимальное разрешение дисплея, поддерживаемое интерфейсными выходами видеокарты.',
        'Наличие в видеокарте разъема DVI (Dual-Link), который используется для передачи цифрового видеосигнала.',
        'Длина видеокарты от планки с видеовыходами, до окончания текстолита или системы охлаждения.',
        'Поддержка технологий', 'Питание', 'Разъемы', 'Особенности',
        'Использование в системе охлаждения видеокарты тепловых трубок (heatpipe), которые улучшают охлаждение графического процессора и видеопамяти.',
        'Размеры',
        'Данная характеристика указывает на заводской "разгон" (увеличение частот графического процессора и видеопамяти), который увеличивает производительность видеокарты, по сравнению с референсными видеокартами конкретной модели.'
    ]
    useless_keys = [
        'Интерфейс', 'Разрядность шины видеопамяти',
        'Поддержка технологий NVIDIA', 'Тип поставки',
        'Ширина видеокарты', 'Версия разъема HDMI',
        'Версия разъема Display Port',
        'Использование тепловых трубок',
        'OverClock Edition', "Толщина видеокарты"
    ]
    
    full_spec = get_data(link)
    preresult = del_title(titles, full_spec)
    return del_keys(useless_keys, preresult)

# link = 'https://www.citilink.ru/product/ustroistvo-ohlazhdeniya-kuler-deepcool-gamma-hunter-120mm-ret-1161729/properties/'
# print(get_data(link))
# debug = fan(link)

# for item in debug:
#     print(item)

# for k,v in debug.items():
#     print(f'{k}\t\t{v}')
