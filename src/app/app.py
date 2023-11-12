from typing import Any

from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from src.backend.database import SessionLocal
from src.backend.cruds import cpu_crud

app = FastAPI()

# Настройка CORS
origins = [
    "http://localhost:3000",  # Разрешенный источник запросов (адрес вашего React-приложения)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все HTTP-методы (GET, POST, PUT, DELETE и т. д.)
    allow_headers=["*"],  # Разрешаем все заголовки в запросах
)


NOT_PARSED = {'request': "ERROR: Not parsed"}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root(request: Request) -> Any:
    return {'request': 'homepage'}


@app.get('/cpu/', response_model=dict)
async def cpus(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return cpu_crud.get_cpus(db, skip=skip, limit=limit)


@app.get('/cpu/{brand}/', response_model=dict)
async def cpu_brand(
        brand: str,
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)):
    return cpu_crud.get_cpu_by_brand(db=db, brand=brand, skip=skip, limit=limit)


@app.get('/cpu/{model}', response_model=dict)
async def cpu_model(model: str, db: Session = Depends(get_db)):
    return cpu_crud.get_cpu_by_model(model=model, db=db)


@app.get('/gpu/')
async def gpus(request: Request):
    # return {'request': 'gpu'}
    return NOT_PARSED


@app.get('/ram/')
async def ram(request: Request):
    # return {'request': 'ram'}
    return NOT_PARSED


@app.get('/motherboard/')
async def motherboard(request: Request):
    # return {'request': 'motherboard'}
    return NOT_PARSED


@app.get('/storage/')
async def storage(request: Request):
    # return {'request': 'storage'}
    return NOT_PARSED


@app.get('/power_unit/')
async def power_unit(request: Request):
    # return {'request': 'power_unit'}
    return NOT_PARSED


@app.get('/cpu_fan/')
async def cpu_fan(request: Request):
    # return {'request': 'cpu_fan'}
    return NOT_PARSED


@app.get('/shopping_cart/')
async def shopping_cart(request: Request):
    # return {'request': 'shopping_cart'}
    return NOT_PARSED


@app.get('/profile/')
async def profile(request: Request):
    # return {'request': 'profile'}
    return NOT_PARSED
