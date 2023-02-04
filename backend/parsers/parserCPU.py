import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from openpyxl import load_workbook
import time


def content_from_link(link:str)->str:
    # Get content from citilink
    response = requests.get(link)
    time.sleep(4)
    print(response.status_code)
    soup = bs(response.content, 'html5lib')
    return soup.get_text()

def delete_useless(dataset:str)->list[str]:
    # deleting useless html code
    dataset = list(dataset.partition('Брэнд'))
    dataset = list(dataset[2].partition('Упаковка')).pop(0)
    data = dataset.split('\n')
    for i in range(len(data)):
        data[i] = data[i].strip()
    k = 0
    while k != len(data):
        if data[k] == '':
            data.pop(k)
        else:
            k += 1    
    return data

def get_data(link:str)->dict:
    dataset = content_from_link(link)
    data = delete_useless(dataset)

    # deleting titles
    titles = [
        'Спецификация памяти',
              'Спецификация PCI Express',
               'Встроенная графика'
               ]
    for title in titles:
        if title in data:
            data.remove(title)
    # create dict
    data.insert(0, 'Брэнд')
    result = {}
    for i in range(1, len(data), 2):
        result[data[i-1]] = data[i]

    # delete useless rows
    useless_str = [
        'Ядро', 'Разрядность вычислений', 'Тип поставки',
        'Поддержка памяти ECC', 'Версия PCI Express',
        'Количество каналов PCI Express', 'Пропускная способность шины (GT/s)',
        'Конфигурация PCI Express', 'Пропускная способность памяти',
        'Максимальный объем видеопамяти', 'Максимальный объем памяти',
        'Тепловыделение в режиме Turbo'
    ]
    for key in useless_str:
        if key in result:
            result.pop(key)

    return result


def CPU_to_databaseBAD(links):
    dataAMD = []
    dataIntel = []
    for link in links:
        # time.sleep(15)
        try: 
            data = get_data(link)
            if data['Брэнд'] == 'AMD':
                dataAMD.append(data)
            elif data['Брэнд'] == 'INTEL':
                dataIntel.append(data)
        except KeyError:
            print(f'{link} is bad')
        finally:
            time.sleep(1)
    dfAMD = pd.DataFrame.from_dict(dataAMD)
    dfIntel = pd.DataFrame.from_dict(dataIntel)

    df_dict = {'AMDCPU': dfAMD, 'Intel': dfIntel}

    book = load_workbook(r'backend/database.xlsx')
    writer = pd.ExcelWriter(r'backend/database.xlsx', engine='openpyxl')
    writer.book = book

    for sheet, df in df_dict.items():
        df.to_excel(writer, sheet_name=sheet, index=False, header=True)
    writer.save()


links = [
    'https://www.citilink.ru/product/processor-amd-s-ryzen-7-5800x-am4-100-000000063-3-8ghz-oem-1773839/properties/',
    'https://www.citilink.ru/product/processor-amd-s-ryzen-7-3700x-am4-100-000000071-3-6ghz-oem-1804883/properties/',
    'https://www.citilink.ru/product/processor-amd-s-ryzen-5-5600g-am4-100-000000252-3-9ghz-amd-radeon-oem-1773831/properties/',
    'https://www.citilink.ru/product/processor-intel-s-pentium-gold-g6405-soc-1200-4-1ghz-iuhdg610-oem-1722989/properties/',
    'https://www.citilink.ru/product/processor-intel-s-core-i5-11400f-soc-1200-2-6ghz-oem-1722999/properties/',
    'https://www.citilink.ru/product/processor-intel-s-core-i5-12400f-soc-1700-2-5ghz-oem-1782240/properties/'
]

CPU_to_databaseBAD(links)

# data = get_data(links[1])
# print(data)