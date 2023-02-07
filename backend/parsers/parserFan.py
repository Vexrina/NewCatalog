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

# LINUX_driver_path = r'\usr\bin\google-chrome'
# WINDOWS_driver_path = r'C:\Users\drivers\chromedriver.exe'

# os = platform.platform()
# if os.find('Win') != -1:
#     driver_path = WINDOWS_driver_path
# else:
#     driver_path = LINUX_driver_path

LOGGER.setLevel(logging.WARNING)

def get_data(link):
    driver = webdriver.Chrome(service=service)# add options=chrome_options 
    driver.get(link)
    time.sleep(30)
    divs = driver.find_elements(By.CLASS_NAME, 'SpecificationsFull')
    specs =[]
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
    while(k!=len(full_spec)):
        full_spec[k]=full_spec[k].strip()
        if full_spec[k].find('</div>')==0:
            full_spec.pop(k)
        elif full_spec[k].find('</h4>')==0:
            full_spec.pop(k)
        elif full_spec[k].find('<div')==0:
            full_spec.pop(k)    
        else:
            k+=1
    
    
    titles = [
        'Дополнительные характеристики',
        'Упаковка', 'Размеры, вес',
        'Электропитание', 'Конструкция',
        'Совместимост', 'Основные параметры',
    ]
    for title in titles:
        if title in full_spec:
            full_spec.remove(title)
    
    result = {}
    for i in range(1, len(full_spec), 2):
        result[full_spec[i-1]]=full_spec[i]
    return result


link = 'https://www.citilink.ru/product/ustroistvo-ohlazhdeniya-kuler-deepcool-gamma-hunter-120mm-ret-1161729/properties/'
# print(get_data(link))
debug = get_data(link)

# for item in debug:
#     print(item)

for k,v in debug.items():
    print(f'{k}\t\t{v}')