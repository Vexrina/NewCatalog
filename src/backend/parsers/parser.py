import time
from random import randint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
import re
import httpx
import src.backend.parsers.useless_title_and_keys as utlk

chrome_options = Options()
chrome_options.add_argument("--headless")

service = Service(ChromeDriverManager().install())

LOGGER.setLevel(logging.WARNING)


# webdriver.DesiredCapabilities.CHROME['proxy']

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
    while k != len(full_spec):
        full_spec[k] = full_spec[k].strip()
        if full_spec[k].find('</div>') == 0:
            full_spec.pop(k)
        elif full_spec[k].find('</h4>') == 0:
            full_spec.pop(k)
        elif full_spec[k].find('<div') == 0:
            full_spec.pop(k)
        else:
            k += 1

    full_spec = list(filter(None, full_spec))
    return full_spec


def del_title(titles: list[str], full_spec: list[str]):
    k = 0
    while k != len(full_spec):
        if full_spec[k] in utlk.notuniq_titles:
            full_spec.pop(k)
        elif full_spec[k] in titles:
            full_spec.pop(k)
        else:
            k += 1
    result = {}
    for i in range(1, len(full_spec), 2):
        result[full_spec[i - 1]] = full_spec[i]
    return result


def del_keys(useless_keys: list[str], preresult: dict) -> dict:
    for key in utlk.notuniq_keys:
        if key in preresult:
            preresult.pop(key)
    for key in useless_keys:
        if key in preresult:
            preresult.pop(key)
    return preresult


def fan(link: str) -> dict:
    full_spec = []
    step = 0
    while len(full_spec) == 0 and step != 10:
        full_spec = get_data(link)
        timeout = randint(5, 30)
        print(f'Trying again, waiting for timeout {timeout}')
        time.sleep(timeout)
        step += 1
    preresult = del_title(utlk.fan_titles, full_spec)
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
    preresult = del_keys(utlk.fan_keys, preresult)

    result = {k: preresult[k] for k in preresult if not re.match(pattern, k)}

    return result


def cpu(link: str) -> dict:
    full_spec = []
    step = 0
    while len(full_spec) == 0 and step != 10:
        full_spec = get_data(link)
        timeout = randint(5, 10)
        print(f'Trying again, waiting for timeout {timeout}')
        time.sleep(timeout)
        step += 1
    preresult = del_title(utlk.cpu_titles, full_spec)
    return del_keys(utlk.cpu_keys, preresult)


def gpu(link: str) -> dict:
    full_spec = []
    step = 0
    while len(full_spec) == 0 and step != 10:
        full_spec = get_data(link)
        timeout = randint(5, 30)
        print(f'Trying again, waiting for timeout {timeout}')
        time.sleep(timeout)
        step += 1
    preresult = del_title(utlk.gpu_titles, full_spec)
    return del_keys(utlk.gpu_keys, preresult)


def storage(link: str) -> dict:
    full_spec = []
    step = 0
    while len(full_spec) == 0 and step != 10:
        full_spec = get_data(link)
        timeout = randint(5, 30)
        print(f'Trying again, waiting for timeout {timeout}')
        time.sleep(timeout)
        step += 1
    indexes = [i for i, j in enumerate(full_spec) if j == 'Особенности']
    if len(indexes) > 1:
        full_spec.pop(indexes[-1])
        full_spec.pop(indexes[-1])
    preresult = del_title(utlk.storage_titles, full_spec)
    return del_keys(utlk.storage_keys, preresult)


def ram(link: str) -> dict:
    full_spec = []
    step = 0
    while len(full_spec) == 0 and step != 10:
        full_spec = get_data(link)
        timeout = randint(5, 30)
        print(f'Trying again, waiting for timeout {timeout}')
        time.sleep(timeout)
        step += 1
    if 'Конфигурация чипов' in full_spec:
        full_spec.remove('Конфигурация чипов')
    preresult = del_title(utlk.ram_titles, full_spec)
    return del_keys(utlk.ram_keys, preresult)


def motherboard(link: str) -> dict:
    full_spec = []
    step = 0
    while len(full_spec) == 0 and step != 10:
        full_spec = get_data(link)
        timeout = randint(5, 30)
        print(f'Trying again, waiting for timeout {timeout}')
        time.sleep(timeout)
        step += 1
    if 'Чипсет' in full_spec:
        full_spec.remove('Чипсет')
    preresult = del_title(utlk.motherboard_titles, full_spec)
    return del_keys(utlk.motherboard_keys, preresult)


def power_unit(link: str) -> dict:
    full_spec = []
    step = 0
    while len(full_spec) == 0 and step != 10:
        full_spec = get_data(link)
        timeout = randint(5, 30)
        print(f'Trying again, waiting for timeout {timeout}')
        time.sleep(timeout)
        step += 1
    preresult = del_title(utlk.pu_titles, full_spec)
    return del_keys(utlk.pu_keys, preresult)


def parsing(links: list[str], what_parse: str)-> list[dict]:
    response = httpx.get('https://www.citilink.ru/')
    response.raise_for_status()
    data = []
    match what_parse:
        case 'fan':
            for link in links:
                response = httpx.get(link)
                response.raise_for_status()
                temp = fan(link)
                if len(temp) != 0:
                    data.append(temp)
                else:
                    print(f'link is bad\n{link}')
        case 'cpu':
            for link in links:
                response = httpx.get(link)
                response.raise_for_status()
                temp = cpu(link)
                if len(temp) != 0:
                    data.append(temp)
                else:
                    print(f'link is bad\n{link}')
        case 'gpu':
            for link in links:
                response = httpx.get(link)
                response.raise_for_status()
                temp = gpu(link)
                if len(temp) != 0:
                    data.append(temp)
        case 'storage':
            for link in links:
                response = httpx.get(link)
                response.raise_for_status()
                temp = storage(link)
                if len(temp) != 0:
                    data.append(temp)
                else:
                    print(f'link is bad\n{link}')
        case 'ram':
            for link in links:
                response = httpx.get(link)
                response.raise_for_status()
                temp = ram(link)
                if len(temp) != 0:
                    data.append(temp)
                else:
                    print(f'link is bad\n{link}')
        case 'motherboard':
            for link in links:
                response = httpx.get(link)
                response.raise_for_status()
                temp = motherboard(link)
                if len(temp) != 0:
                    data.append(temp)
                else:
                    print(f'link is bad\n{link}')
        case 'power_unit':
            for link in links:
                response = httpx.get(link)
                response.raise_for_status()
                temp = power_unit(link)
                if len(temp) != 0:
                    data.append(temp)
                else:
                    print(f'link is bad\n{link}')
    return data
