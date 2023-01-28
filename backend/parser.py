import requests
from bs4 import BeautifulSoup as bs
import time, pandas as pd
from openpyxl import load_workbook

def get_data(link):
    #Get content from citilink
    response = requests.get(link)
    print(response.status_code)
    soup = bs(response.content, 'html5lib')
    dataset = soup.get_text().split('\n') 
    
    # Delete bad content
    while(dataset[0].find('Основные характеристики')==-1):
        dataset.pop(0)
    while(dataset[-1].find('Упаковка')==-1):
        dataset.pop()
    dataset.pop()
    dataset.pop(0)

    # Delete '\t','\n' or '' strings
    k = 0
    while(k!=len(dataset)):
        dataset[k]=dataset[k].strip()
        if dataset[k] == '':
            dataset.pop(k)
        else:
            k+=1

    # Delete Titles strings
    replace_data = [
        'Спецификация памяти', 'Спецификация PCI Express', 'Встроенная графика'
        ]
    del_str = []
    for i in range(len(dataset)):
        for s in replace_data:
            index = dataset[i].find(s)
            if index == -1:
                continue
            else:
                del_str.append(i)
    k = 0
    for item in del_str:
        dataset.pop(item-k)
        k+=1

    # Create dict
    data = {}
    for i in range(1, len(dataset), 2):
        data[dataset[i-1]] = dataset[i]
    
    # Delete useless strings for database
    what_pop = [
        'Ядро', 'Разрядность вычислений', 'Тип поставки',
        'Поддержка памяти ECC', 'Версия PCI Express',
        'Количество каналов PCI Express'
    ]
    for item in what_pop:
        data.pop(item)
    return data

links = [
    'https://www.citilink.ru/product/processor-amd-s-ryzen-7-5800x-am4-100-000000063-3-8ghz-oem-1773839/properties/',
    'https://www.citilink.ru/product/processor-amd-s-ryzen-7-3700x-am4-100-000000071-3-6ghz-oem-1804883/properties/',
    'https://www.citilink.ru/product/processor-amd-s-ryzen-5-5600g-am4-100-000000252-3-9ghz-amd-radeon-oem-1773831/properties/',
    'https://www.citilink.ru/product/processor-intel-s-pentium-gold-g6405-soc-1200-4-1ghz-iuhdg610-oem-1722989/properties/'

]

def to_databaseBAD(links):
    dataAMD = []
    dataIntel = []
    for link in links:
        time.sleep(15)
        data = get_data(link)
        if data['Брэнд'] == 'AMD':
            dataAMD.append(data)
        elif data['Брэнд'] == 'INTEL':
            dataIntel.append(data)
        

    dfAMD = pd.DataFrame.from_dict(dataAMD)
    dfIntel = pd.DataFrame.from_dict(dataIntel)

    df_dict = {'AMD':dfAMD, 'Intel':dfIntel}

    book = load_workbook(r'backend/database.xlsx')
    writer = pd.ExcelWriter(r'backend/database.xlsx',engine='openpyxl')
    writer.book = book

    for sheet, df in df_dict.items():
        df.to_excel(writer, sheet_name=sheet, index=False, header=True)
    writer.save()