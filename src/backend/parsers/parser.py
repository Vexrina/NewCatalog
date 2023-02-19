import os
import pathlib
import shutil

import time
from random import randint
import logging
import re
import httpx

from httpx import HTTPError
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.proxy import Proxy, ProxyType
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent

from src.backend.parsers.proxyHTTP import proxy

import src.backend.parsers.useless_title_and_keys as utlk

# for saving images while parsing
root = pathlib.Path(__file__).parent.parent

image_path = root / 'images' / 'new_image.png'
new_image_path = root / 'images'
# for saving images while parsing

# settings of selenium
chrome_options = Options()
chrome_options.add_argument("--headless")

service = Service(ChromeDriverManager().install())

LOGGER.setLevel(logging.WARNING)

prox = Proxy()
prox.proxy_type = ProxyType.MANUAL

capabilities = webdriver.DesiredCapabilities.CHROME


# settings of selenium


def randomize_driver() -> None:
    prox.http_proxy = proxy[randint(0, len(proxy) - 1)]
    size_x = randint(300, 1920)
    size_y = randint(600, 1080)
    ua = UserAgent()
    user_agent = ua.random
    chrome_options.add_argument(f'user-agent={user_agent}')
    chrome_options.add_argument(f'window-size={size_x},{size_y}')
    prox.add_to_capabilities(capabilities)


def find_elem(driver: webdriver, what_return: int, timeout: int = 300) -> WebElement | list[WebElement]:
    while timeout > 0:
        try:
            match what_return:
                case 1:
                    return driver.find_elements(By.XPATH, '//main/div/div/div/div/div/div/ul/li')
                case 2:
                    return driver.find_element(By.XPATH, '//div/img')
        except Exception as e:
            print(f'Type error: {type(e)}\nError: {e}\n')
            time.sleep(1)
            timeout -= 1
    raise RuntimeError('Can\'t load page')


def get_data(link: str) -> list[str]:
    # add options=chrome_options
    randomize_driver()
    driver = webdriver.Chrome(service=service, options=chrome_options, desired_capabilities=capabilities)
    driver.get(link)
    try:
        divs = find_elem(driver=driver, what_return=1)
        image = find_elem(driver=driver, what_return=2)
    except RuntimeError as e:
        print(e)
    else:
        with image_path.open('wb') as file:
            file.write(image.screenshot_as_png)
        text = ''
        for div in divs:
            text = text + '\n' + div.text
        driver.close()
        specs = text.split('\n')
        while specs[-1] != 'Дополнительные характеристики':
            specs.pop()

        full_spec = list(filter(None, specs))

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
    full_spec = get_data(link)
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
    full_spec = get_data(link)
    step = 0
    while len(full_spec) == 0 and step != 10:
        full_spec = get_data(link)
        timeout = randint(5, 30)
        print(f'Trying again, waiting for timeout {timeout}')
        time.sleep(timeout)
        step += 1
    preresult = del_title(utlk.cpu_titles, full_spec)
    src = preresult['Модель']
    os.rename(image_path, new_image_path / f'{src}.png')
    shutil.move(new_image_path / f'{src}.png', new_image_path / 'cpu' / f'{src}.png')
    return del_keys(utlk.cpu_keys, preresult)


def gpu(link: str) -> dict:
    full_spec = get_data(link)
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
    full_spec = get_data(link)
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
    full_spec = get_data(link)
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
    full_spec = get_data(link)
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
    full_spec = get_data(link)
    step = 0
    while len(full_spec) == 0 and step != 10:
        full_spec = get_data(link)
        timeout = randint(5, 30)
        print(f'Trying again, waiting for timeout {timeout}')
        time.sleep(timeout)
        step += 1
    preresult = del_title(utlk.pu_titles, full_spec)
    return del_keys(utlk.pu_keys, preresult)


def parsing(links: list[str], what_parse: str) -> tuple[list[dict], list[str]]:
    data = []
    parsed_links = []
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
                try:
                    response = httpx.get(link)
                    response.raise_for_status()
                    temp = cpu(link)
                    if len(temp) != 0:
                        data.append(temp)
                        parsed_links.append(link)
                    else:
                        print(f'link is bad\n{link}')
                except HTTPError as err:
                    print(f'Congrats, u have timeout on citilink.ru.\n{type(err)}:{err}')
                    return data, parsed_links
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
    return data, parsed_links
