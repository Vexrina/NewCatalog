from typing import Any
import generate_page

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path


app = FastAPI()
app.mount(
    '/static/',
    StaticFiles(directory=Path(__file__).parent.parent/'static'),
    name='static',
)

templates = Jinja2Templates(directory='pages')

@app.get("/", response_class=HTMLResponse)
async def root(request: Request) -> Any:
    generate_page.generate_homepage()
    context = {'request':request}
    return templates.TemplateResponse("homepage.html", context)

@app.get('/cpu/')
async def cpus(request: Request):
    return {'request':'cpu'}

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