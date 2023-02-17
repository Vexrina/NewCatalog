import httpx
from src.backend.parsers.cpu_to_parse import amd
from src.backend.parsers.parser import parsing

response = httpx.get('https://www.citilink.ru/')
print(response.status_code)

