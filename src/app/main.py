import httpx

from src.backend.database import SessionLocal, engine
from src.backend import crud, models, schemas
from src.backend.parsers.parser import parsing


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


response = httpx.get('https://www.citilink.ru/')
print(response.status_code)
print(response.content)
test = {'cpu': [
    'https://www.citilink.ru/product/processor-amd-s-ryzen-7-5800x-am4-100-000000063-3-8ghz-oem-1773839/properties/',
    # 'https://www.citilink.ru/product/processor-amd-s-ryzen-7-3700x-am4-100-000000071-3-6ghz-oem-1804883/properties/',
    # 'https://www.citilink.ru/product/processor-amd-s-ryzen-5-5600g-am4-100-000000252-3-9ghz-amd-radeon-oem-1773831'
    # '/properties/',
    # 'https://www.citilink.ru/product/processor-intel-s-pentium-gold-g6405-soc-1200-4-1ghz-iuhdg610-oem-1722989'
    # '/properties/',
    # 'https://www.citilink.ru/product/processor-intel-s-core-i5-11400f-soc-1200-2-6ghz-oem-1722999/properties/',
    # 'https://www.citilink.ru/product/processor-intel-s-core-i5-12400f-soc-1700-2-5ghz-oem-1782240//'
]}

# parsing(test['cpu'], 'cpu')
