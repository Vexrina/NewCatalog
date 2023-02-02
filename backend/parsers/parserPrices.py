from googlesearch import search
from selenium import webdriver
from selenium.webdriver.common.by import By 


def get_links(query:str)->list[str]:
    sites = ['dns-shop.ru', 'citilink.ru', 'regard.ru', 'onlinetrade.ru']

    dnsLinks = []
    citiLinks = []
    regardLinks = []
    onlineLinks = []

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
    result = [
        dnsLinks[0],
        citiLinks[0],
        regardLinks[0],
        onlineLinks[0],
    ]
    return result

query = 'ryzen 5 3600 oem site:'


import time

def get_dns_price(link:str):
    driver = webdriver.Chrome(r'\usr\bin\google-chrome')
    driver.get(link)
    # time.sleep(5)
    div = driver.find_element(By.CLASS_NAME,'product-buy__price')
    price = div.get_attribute('outerHTML')
    driver.close()
    price = price[price.find('>')+1:]
    price = price[:price.find('<')-1].replace(' ','')
    return price
    