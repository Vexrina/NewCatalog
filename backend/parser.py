from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
import time
import re
import pandas as pd
from openpyxl import load_workbook

# some options for webdriver
chrome_options = Options()
chrome_options.add_argument("--headless")

service = Service(ChromeDriverManager().install())

LOGGER.setLevel(logging.WARNING)


def get_data(link: str) -> list[str]:
    # add options=chrome_options
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(link)
    divs = driver.find_elements(By.CLASS_NAME, 'SpecificationsFull')
    specs = []
    for div in divs:
        specs.append(div.get_attribute('outerHTML'))
    driver.close()
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
        'Особенности',
    ]
    preresult = del_title(titles, full_spec)

    useless_key = [
        'Направление выдува', 'Воздушный поток',
        'Тип подшипника', '-', 'Вес',
        'Вес упаковки (ед)', 'Гарантия',
        'Длина кулера', 'Ширина кулера', 'Толщина вентилятора',
        'Воздушный поток вентилятора',
        'Особенности', 'Назначение кулера для бренда',
        'Разборное крепление', 'Термопаста в комплекте',
        'Габариты упаковки (ед) ДхШхВ',

    ]
    pattern = 'Совместимость\s[a-zA-z]{3,}\s?\d+\+?'
    """
    У ситилинка, в разделе спецификаций на охлаждение,
    есть множество различных "совместимостей" с разными Сокетами,
    таких как SocketAM4, LGA 955 и тд. Чтобы избавится от этого,
    рациональнее по времени использовать regex:
    r'Совместимость\s[a-zA-z]{3,}\s?\d+\+?'
    Строка начинается на "Cовместимость" и любой whitespace --- Совместимость\s
    потом идут любые A-z символы от 3 штук --- [a-zA-z]{3,}
    возможен пробел, после идут 1 или больше цифр --- \s?\d+
    возможен плюс на конце --- \+?
    """
    preresult = del_keys(useless_key, preresult)

    result = {k: preresult[k] for k in preresult if not re.match(pattern, k)}

    return result


def cpu(link: str) -> dict:
    titles = [
        'Основные характеристики',
        'Спецификация памяти',
        'Спецификация PCI Express',
        'Встроенная графика',
        'Дополнительные характеристики',
        'Упаковка',
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


def gpu(link: str) -> dict:
    with open('backend/gpu_useless_lines.txt',encoding='utf-8') as f:
        titles = f.readlines()
    for i in range(len(titles)):
        titles[i] = titles[i][:-1]
    # print(titles)
    useless_keys = [
        'Интерфейс', 'Разрядность шины видеопамяти',
        'Поддержка технологий NVIDIA', 'Тип поставки',
        'Ширина видеокарты', 'Версия разъема HDMI',
        'Версия разъема Display Port',
        'Использование тепловых трубок',
        'OverClock Edition', "Толщина видеокарты",
        'Вес упаковки (ед)', 'Габариты упаковки (ед) ДхШхВ',
        'Гарантия', 'Высота видеокарты',
    ]

    full_spec = get_data(link)
    full_spec = list(filter(None, full_spec))
    preresult = del_title(titles, full_spec)
    # return preresult
    return del_keys(useless_keys, preresult)


def storage(link: str) -> dict:
    titles = [
        'Основные характеристики',
        'Скорость',
        'Ресурс',
        'Особенности',
        'Габариты, вес'
    ]
    useless_keys = [
        'Уровень шума простоя',
        'Длина устройства',
        'Толщина',
        'Вес устройства',
        'Ударостойкость при работе',
        'Ударостойкость при хранении'
    ]
    full_spec = get_data(link)
    preresult = del_title(titles, full_spec)
    return del_keys(useless_keys, preresult)


def ram(link: str) -> dict:
    titles = [
        'Основные характеристики',
        'Тестовые характеристики',
        'Характеристики SPD',
        'Конструкция', 'Конфигурация чипов',
        'Error Checking and Correction',
        'Скорость памяти в тестовом режиме.',
        'Автоматические настройки модуля памяти.',
        'Задержка памяти в тестовом режиме.',
        'Скорость памяти в тестовом режиме.',
        'Напряжение памяти в тестовом режиме.',
        'Упаковка','Дополнительные характеристики',
        ''
    ]
    useless_keys = [
        'Показатель скорости', 'Буферизация',
        'Поддержка ECC', 'Скорость (SPD)',
        'Напряжение (SPD)', 'Задержка (SPD)',
        'Радиатор охлаждения', 'Тип поставки',
        'Количество чипов', 'Конфигурация чипов',
        'Крепление чипов', 'Вес упаковки',
        'Гарантия', 'Вес упаковки (ед)',
    ]
    full_spec = get_data(link)
    preresult = del_title(titles, full_spec)
    return del_keys(useless_keys, preresult)


def parsing(links: list[dict], what_parse: str):
    data = []
    k = 0
    match what_parse:
        case 'fan':
            for link in links:
                temp = fan(link)
                if len(temp) == 0:
                    print(f'Bad link{k}, try again')
                else:
                    data.append(temp)
                k += 1
        case 'cpu':
            for link in links:
                temp = cpu(link)
                if len(temp) == 0:
                    print(f'Bad link{k}, try again')
                else:
                    data.append(temp)
                k += 1
        case 'gpu':
            for link in links:
                temp = gpu(link)
                if len(temp) == 0:
                    print(f'Bad link{k}, try again')
                else:
                    data.append(temp)
                k += 1
        case 'storage':
            for link in links:
                temp = storage(link)
                if len(temp) == 0:
                    print(f'Bad link{k}, try again')
                else:
                    data.append(temp)
                k += 1
        case 'ram':
            for link in links:
                temp = ram(link)
                if len(temp) == 0:
                    print(f'Bad link{k}, try again')
                else:
                    data.append(temp)
                k += 1
    df = pd.DataFrame.from_dict(data)
    try:
        book = load_workbook(r'backend/database.xlsx')
        writer = pd.ExcelWriter(r'backend/database.xlsx', engine='openpyxl')
        writer.book = book

        df.to_excel(writer, sheet_name=what_parse + 's', index=False, header=True)
        writer.save()
    except PermissionError:
        print('Excelbook is opened. Please, close it and start again code')


test = {}
test['fan'] = [
    'https://www.citilink.ru/product/ustroistvo-ohlazhdeniya-kuler-deepcool-gamma-hunter-120mm-ret-1161729/properties/',
    'https://www.citilink.ru/product/ustroistvo-ohlazhdeniya-kuler-id-cooling-se-903-r-v2-soc-am4-am3-1150-1622823/properties/',
    'https://www.citilink.ru/product/ustroistvo-ohlazhdeniya-kuler-deepcool-theta-21-pwm-92mm-ret-668261/properties/',
    'https://www.citilink.ru/product/ventilyator-aerocool-frost-12-pwm-120mm-ret-1170440/properties/',
]
test['storage'] = [
    'https://www.citilink.ru/product/ssd-nakopitel-kingston-a400-sa400s37-480g-480gb-2-5-sata-iii-420253/properties/',
    'https://www.citilink.ru/product/zhestkii-disk-wd-s-sata-iii-1tb-wd10ezex-caviar-blue-7200rpm-64mb-3-5-1776660/properties/',
    'https://www.citilink.ru/product/zhestkii-disk-seagate-barracuda-st2000dm008-2tb-hdd-sata-iii-3-5-1187869/',
    'https://www.citilink.ru/product/zhestkii-disk-toshiba-sata-iii-1tb-hdwd110uzsva-p300-7200rpm-64mb-3-5-1793672/',
    'https://www.citilink.ru/product/nakopitel-ssd-digma-sata-iii-256gb-dgsr2256gs93t-run-s9-2-5-1651620/',
    'https://www.citilink.ru/product/nakopitel-ssd-kingspec-pci-e-512gb-nx-512-m-2-2280-1742084/',
]

test['cpu'] = [
    'https://www.citilink.ru/product/processor-amd-s-ryzen-7-5800x-am4-100-000000063-3-8ghz-oem-1773839/properties/',
    'https://www.citilink.ru/product/processor-amd-s-ryzen-7-3700x-am4-100-000000071-3-6ghz-oem-1804883/properties/',
    'https://www.citilink.ru/product/processor-amd-s-ryzen-5-5600g-am4-100-000000252-3-9ghz-amd-radeon-oem-1773831/properties/',
    'https://www.citilink.ru/product/processor-intel-s-pentium-gold-g6405-soc-1200-4-1ghz-iuhdg610-oem-1722989/properties/',
    'https://www.citilink.ru/product/processor-intel-s-core-i5-11400f-soc-1200-2-6ghz-oem-1722999/properties/',
    'https://www.citilink.ru/product/processor-intel-s-core-i5-12400f-soc-1700-2-5ghz-oem-1782240//'
]
test['gpu'] = [
    'https://www.citilink.ru/product/videokarta-palit-pci-e-pa-rtx2060super-dual-8g-no-led-nv-rtx2060super-1489448/properties/',
    'https://www.citilink.ru/product/videokarta-palit-pci-e-pa-rtx3050-dual-nv-rtx3050-8192mb-128-gddr6-155-1658278/properties/',
    'https://www.citilink.ru/product/videokarta-asus-pci-e-4-0-dual-rx6650xt-o8g-amd-rx6650xt-8192mb-128-gd-1781223/properties/',
    'https://www.citilink.ru/product/videokarta-gigabyte-pci-e-gv-r65xtgaming-oc-4gd-amd-rx6500xt-4096mb-64-1654728/properties/',
    'https://www.citilink.ru/product/videokarta-gigabyte-pci-e-4-0-gv-ia310wf2-4gd-intel-arc-a380-windforce-1874762/properties/',
    'https://www.citilink.ru/product/videokarta-gigabyte-pci-e-4-0-gv-ia380wf2oc-6gd-intel-arc-a380-windfor-1874760/properties/',
    'https://www.citilink.ru/product/videokarta-gigabyte-pci-e-4-0-gv-ia380gaming-oc-6gd-intel-arc-a380-gam-1874758/properties/',
]
test['ram'] = [
    'https://www.citilink.ru/product/modul-pamyati-corsair-vengeance-lpx-cmk16gx4m2b3200c16-ddr4-2x-8gb-320-330758/properties/',
    'https://www.citilink.ru/product/pamyat-ddr4-2x8gb-3200mhz-kingston-kf432c16bbk2-16-rtl-pc4-25600-cl16-1560200/properties/',
    'https://www.citilink.ru/product/pamyat-ddr5-2x16gb-5200mhz-kingston-kf552c40bbk2-32-fury-beast-rtl-cl4-1628858/properties/',
    'https://www.citilink.ru/product/pamyat-ddr5-2x16gb-6000mhz-kingston-kf560c40bbk2-32-fury-beast-rtl-cl4-1676551/properties/',
    'https://www.citilink.ru/product/modul-pamyati-patriot-xms3-dhx-psd38g16002-ddr3-8gb-1600-dimm-ret-352753/properties/',
]
# datas = []
# for link in test['gpu']:
#     datas.append(gpu(link))

# for data in datas:
#     print(data)
#     print('___')

for key, links in test.items():
    parsing(links, key)