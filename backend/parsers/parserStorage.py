import httpx
import time
from bs4 import BeautifulSoup as bs
import pandas as pd
from openpyxl import load_workbook


def debug_data(data):
    i = 0
    for item in data:
        print(f'{i}__{item}')
        i += 1


def get_data(link):
    # Get content form citilink
    response = httpx.get(link)
    print(response.status_code)
    soup = bs(response.content, 'html5lib')
    dataset = soup.get_text()
    dataset = list(dataset.partition('Брэнд'))
    dataset = list(dataset[2].partition('Упаковка'))
    dataset = dataset[0]
    data = dataset.split('\n')
    k = 0
    while k != len(data):
        data[k] = data[k].strip()
        if data[k] == '':
            data.pop(k)
        elif data[k].count('.') > 1:
            data.pop(k)
        else:
            k += 1

    titles = [
        'Скорость',
        'Ресурс',
        'Особенности',
        'Габариты, вес'
    ]

    for item in data:
        if item in titles:
            data.remove(item)
    data.insert(0, 'Брэнд')

    useless_keys = [
        'Уровень шума простоя',
        'Длина устройства',
        'Толщина',
        'Вес устройства',
        'Ударостойкость при работе',
        'Ударостойкость при хранении'
    ]
    result = {}
    for i in range(1, len(data), 2):
        result[data[i-1]] = data[i]

    for key in useless_keys:
        if key in result:
            result.pop(key)
    # debug_data(data)
    return result


def storage_to_databaseBAD(links):
    storage_data = []
    for link in links:
        data = get_data(link)
        if data == {}:
            print('bad link')
        else:
            storage_data.append(data)
        time.sleep(5)
    dfRAM = pd.DataFrame.from_dict(storage_data)
    print(dfRAM)
    try:
        book = load_workbook(r'backend/database.xlsx')
        writer = pd.ExcelWriter(r'backend/database.xlsx', engine='openpyxl')
        writer.book = book

        dfRAM.to_excel(writer, sheet_name='storage', index=False, header=True)
        writer.save()
    except PermissionError:
        print('Please, close database and try again')


links = [
    'https://www.citilink.ru/product/ssd-nakopitel-kingston-a400-sa400s37-480g-480gb-2-5-sata-iii-420253/properties/',
    'https://www.citilink.ru/product/zhestkii-disk-wd-s-sata-iii-1tb-wd10ezex-caviar-blue-7200rpm-64mb-3-5-1776660/properties/',
    'https://www.citilink.ru/product/zhestkii-disk-seagate-barracuda-st2000dm008-2tb-hdd-sata-iii-3-5-1187869/',
    'https://www.citilink.ru/product/zhestkii-disk-toshiba-sata-iii-1tb-hdwd110uzsva-p300-7200rpm-64mb-3-5-1793672/',
    'https://www.citilink.ru/product/nakopitel-ssd-digma-sata-iii-256gb-dgsr2256gs93t-run-s9-2-5-1651620/',
    'https://www.citilink.ru/product/nakopitel-ssd-kingspec-pci-e-512gb-nx-512-m-2-2280-1742084/',
]
# storage_to_databaseBAD(links)
for link in links:
    print(get_data(link))
