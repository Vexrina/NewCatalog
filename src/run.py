import httpx
from src.backend.parsers.to_parse.cpus import amd
from src.backend.parsers.parser import parsing
from src.backend.fill_db import fill_db

response = httpx.get('https://www.citilink.ru/')
print(response.status_code)

links = []
for i in range(10):
    links.append(amd[i])

data, parsed_links = parsing(links, 'cpu')
fill_db(data, 'cpu')
