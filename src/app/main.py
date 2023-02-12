import httpx
from src.backend.parsers.cpu_to_parse import intel
from src.backend.fill_db import fill_db

response = httpx.get('https://www.citilink.ru/')
print(response.status_code)

fill_db(intel, 'cpu')
