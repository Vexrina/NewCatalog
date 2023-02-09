from typing import Any
# import generate_page

from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path

from sqlalchemy.orm import Session


from src.backend import crud, models,  schemas
from src.backend.database import SessionLocal, engine


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.mount(
    '/static/',
    StaticFiles(directory=Path(__file__).parent.parent/'static'),
    name='static',
)

templates = Jinja2Templates(directory='pages')

@app.get("/", response_class=HTMLResponse)
async def root(request: Request) -> Any:
    # generate_page.generate_homepage()
    context = {'request':request}
    return templates.TemplateResponse("homepage.html", context)

@app.get('/cpu/')
async def cpus(request: Request):
    # generate_page.generate_category_page('cpu')
    context = {'request':request}
    return templates.TemplateResponse("cpu.html", context)

@app.get('/gpu/')
async def cpus(request: Request):
    return {'request':'gpu'}

@app.get('/ram/')
async def cpus(request: Request):
    return {'request':'ram'}

@app.get('/motherboard/')
async def cpus(request: Request):
    return {'request':'motherboard'}

@app.get('/storage/')
async def cpus(request: Request):
    return {'request':'storage'}

@app.get('/power_unit/')
async def cpus(request: Request):
    return {'request':'power_unit'}

@app.get('/cpu_fan/')
async def cpus(request: Request):
    return {'request':'cpu_fan'}

@app.get('/shopping_cart/')
async def cpus(request: Request):
    return {'request':'shopping_cart'}

@app.get('/profile/')
async def cpus(request: Request):
    return {'request':'profile'}