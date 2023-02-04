import time
from googlesearch import search
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import httpx
from bs4 import BeautifulSoup as bs
import platform

# some options for webdriver
chrome_options = Options()
chrome_options.add_argument("--headless")

LINUX_driver_path = r'\usr\bin\google-chrome'
WINDOWS_driver_path = r'C:\Users\drivers\chromedriver.exe'

os = platform.platform()
if os.find('Win') != -1:
    driver_path = WINDOWS_driver_path
else:
    driver_path = LINUX_driver_path

# query must have 'site:' for good search in google


def get_links(query: str) -> list[str]:
    # what sites to parse
    sites = ['dns-shop.ru', 'citilink.ru', 'regard.ru', 'onlinetrade.ru']

    # links what will be found in googlesearch
    dnsLinks = []
    citiLinks = []
    regardLinks = []
    onlineLinks = []

    # search links
    for i in range(4):
        for link in search(query=query+sites[i], tld="co.in", num=1, stop=1, pause=2):
            match i:
                case 0:
                    dnsLinks.append(link)
                case 1:
                    citiLinks.append(link)
                case 2:
                    regardLinks.append(link)
                case 3:
                    onlineLinks.append(link)
            time.sleep(5)

    # take first result
    result = [
        dnsLinks[0],
        onlineLinks[0],
        citiLinks[0],
        regardLinks[0],
    ]
    # return links
    return result


def dns_price(link: str) -> int:
    # open selenium to get html
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get(link)
    time.sleep(5)  # prophylactic delay
    # find element with price
    div = driver.find_element(By.CLASS_NAME, 'product-buy__price')
    price = div.get_attribute('outerHTML')
    driver.close()
    # take price and return
    price = price[price.find('>')+1:]
    price = price[:price.find('<')-1].replace(' ', '')
    return int(price)


def onlinetrade_price(link: str) -> int:
    # open selenium and get link
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get(link)
    time.sleep(5)  # prophylactic delay
    # find elem with price
    elem = driver.find_element(
        by='class name', value='productPage__priceCover').text
    driver.close()
    # take price and return
    index = elem.find('\n')
    price = elem[index+1:-2].replace(' ', '')
    return int(price)


def regard_price(dataset: str) -> int:
    # find price in html code
    dataset = dataset.partition('ВтПолные характеристики')
    dataset = list(dataset[2].partition('В наличии')).pop(0)
    # delete some chars
    dataset = dataset[:-1].replace('\xa0', '')
    # return price
    return int(dataset)


def citilink_price(dataset: str):
    # find element with price
    dataset = list(dataset.partition('В корзину'))
    dataset = list(dataset[2].partition('Оформить заказ')).pop(0)
    # deleting useless strings
    data = dataset.split('\n')
    k = 0
    while k != len(data):
        data[k] = data[k].strip()
        if data[k] == '':
            data.pop(k)
        else:
            k += 1
    # return price
    return int(data[0])


def get_price(link: str, site: int) -> int:
    # get link and flag of site
    match site:
        case 1:
            # site is dns
            return dns_price(link)
        case 2:
            # site is onlinetrade
            return onlinetrade_price(link)
        case 3:
            # site is citilink.
            # open selenium in background for take full html code
            browser = webdriver.Chrome(
                executable_path=driver_path, options=chrome_options
            )
            browser.get(link)
            html = browser.page_source
            time.sleep(10)  # prophylactic delay
            browser.close()  # close browser
            # parse html with bs4
            soup = bs(html, 'html5lib')
            soup.prettify()
            dataset = soup.get_text()
            # call function
            return citilink_price(dataset)
        case 4:
            # use httpx for get html
            response = httpx.get(link)
            html = response.text
            # parse html with bs4
            soup = bs(html, 'html5lib')
            soup.prettify()
            dataset = soup.get_text()
            # call function
            return regard_price(dataset)


def parse_prices(query: str) -> dict:
    # query must have 'site:' for good search in google
    # so add that if str dont have.
    if query[-5:] != 'site:':
        query = query + ' site:'
    # take some links
    links = get_links(query)

    # links = [
    #     'https://www.dns-shop.ru/product/b9c6465190d21b80/processor-amd-ryzen-5-3600-oem/',
    #     'https://www.onlinetrade.ru/catalogue/protsessory-c342/amd/protsessor_amd_ryzen_5_3600_am4_oem_100_000000031-1849861.html',
    #     'https://www.citilink.ru/product/processor-amd-s-ryzen-5-3600-am4-100-000000031-3-6ghz-oem-1773826/',
    #     'https://www.regard.ru/product/324861/processor-amd-ryzen-5-3600-oem',
    # ]

    # take prices
    prices = []
    for i in range(len(links)):
        prices.append(get_price(links[i], i+1))
        
    # create dict with prices and return that
    result = {
        'dns': prices[0],
        'onlinetrade': prices[1],
        'citilink': prices[2],
        'regard': prices[3]
    }
    
    return result


# print(parse_prices('ryzen 5 3600 oem'))
