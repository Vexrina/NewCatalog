import requests
import time
from bs4 import BeautifulSoup as bs
import pandas as pd
from openpyxl import load_workbook


def get_data(link:str) -> dict:
    # Get content from citilink
    response = requests.get(link)
    print(response.status_code)
    soup = bs(response.content, 'html5lib')
    dataset = soup.get_text()
    dataset = list(dataset.partition('Бренд'))
    dataset = list(dataset[2].partition('Упаковка'))
    # print(dataset[1])
    data = dataset[0].split('\n')
    k = 0
    while k != len(data):
        data[k] = data[k].strip()
        if data[k] == '':
            data.pop(k)
        elif data[k].count('.') > 1:
            data.pop(k)
        else:
            k += 1

    # deleting titles and 'helpful' strings
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
    for title in titles:
        if title in data:
            data.remove(title)
    data.insert(0, 'Брэнд')

    result = {}
    for i in range(1, len(data), 2):
        result[data[i-1]] = data[i]

    useless_keys = [
        'Интерфейс', 'Разрядность шины видеопамяти',
        'Поддержка технологий NVIDIA', 'Тип поставки',
        'Ширина видеокарты', 'Версия разъема HDMI',
        'Версия разъема Display Port',
        'Использование тепловых трубок',
        'OverClock Edition', "Толщина видеокарты"
    ]
    for key in useless_keys:
        if key in result:
            result.pop(key)

    return result


def GPU_to_databaseBAD(links: list[str]):
    data_nvidia = []
    data_amd = []
    data_intel = []
    for link in links:
        try:
            data = get_data(link)
            if data['Видеочипсет'].find('NVIDIA') != -1:
                data_nvidia.append(data)
            elif data['Видеочипсет'].find('AMD') != -1:
                data_amd.append(data)
            else:
                data_intel.append(data)
        except KeyError:
            print(f'{link} is bad')
        finally:
            time.sleep(5)

    dfAMD = pd.DataFrame.from_dict(data_amd)
    dfIntel = pd.DataFrame.from_dict(data_intel)
    dfNvidia = pd.DataFrame.from_dict(data_nvidia)

    df_dict = {'AMDGpu': dfAMD, 'IntelGpu': dfIntel, 'Nvidia': dfNvidia}

    try:
        book = load_workbook(r'backend/database.xlsx')
        writer = pd.ExcelWriter(r'backend/database.xlsx', engine='openpyxl')
        writer.book = book

        for sheet, df in df_dict.items():
            df.to_excel(writer, sheet_name=sheet, index=False, header=True)
        writer.save()
    except PermissionError:
        print('Please, close database and try again')
