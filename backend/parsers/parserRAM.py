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
    # print(dataset)
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

    # debug_data(data)

    titles = [
        'Тестовые характеристики',
        'Характеристики SPD',
        'Конструкция', 'Конфигурация чипов',
        'Error Checking and Correction',
        'Скорость памяти в тестовом режиме.',
        'Автоматические настройки модуля памяти.',
        'Задержка памяти в тестовом режиме.',
        'Скорость памяти в тестовом режиме.',
        'Напряжение памяти в тестовом режиме.',
    ]
    # print(data)
    for item in data:
        if item in titles:
            data.remove(item)
    data.insert(0, 'Брэнд')

    # print(data)

    result = {}
    for i in range(1, len(data), 2):
        result[data[i-1]] = data[i]

    useless_keys = [
        'Показатель скорости', 'Буферизация',
        'Поддержка ECC', 'Скорость (SPD)',
        'Напряжение (SPD)', 'Задержка (SPD)',
        'Радиатор охлаждения', 'Тип поставки',
        'Количество чипов', 'Конфигурация чипов',
        'Крепление чипов',
    ]
    for key in useless_keys:
        if key in result:
            result.pop(key)
    # print(result)
    return result


def RAM_to_databaseBAD(links):
    ram_data = []
    for link in links:
        data = get_data(link)
        if data == {}:
            print('bad link')
        else:
            ram_data.append(data)
        time.sleep(5)
    dfRAM = pd.DataFrame.from_dict(ram_data)
    print(dfRAM)
    try:
        book = load_workbook(r'backend/database.xlsx')
        writer = pd.ExcelWriter(r'backend/database.xlsx', engine='openpyxl')
        writer.book = book

        dfRAM.to_excel(writer, sheet_name='RAM', index=False, header=True)
        writer.save()
    except PermissionError:
        print('Please, close database and try again')


# links = [
#     'https://www.citilink.ru/product/modul-pamyati-corsair-vengeance-lpx-cmk16gx4m2b3200c16-ddr4-2x-8gb-320-330758/properties/',
#     'https://www.citilink.ru/product/pamyat-ddr4-2x8gb-3200mhz-kingston-kf432c16bbk2-16-rtl-pc4-25600-cl16-1560200/properties/',
#     'https://www.citilink.ru/product/pamyat-ddr5-2x16gb-5200mhz-kingston-kf552c40bbk2-32-fury-beast-rtl-cl4-1628858/properties/',
#     'https://www.citilink.ru/product/pamyat-ddr5-2x16gb-6000mhz-kingston-kf560c40bbk2-32-fury-beast-rtl-cl4-1676551/properties/',
#     'https://www.citilink.ru/product/modul-pamyati-patriot-xms3-dhx-psd38g16002-ddr3-8gb-1600-dimm-ret-352753/properties/',
# ]
# RAM_to_databaseBAD(links)
# get_data(links[-1])
