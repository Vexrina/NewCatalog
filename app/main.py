from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()
app.mount(
    '/static/',
    StaticFiles(directory=Path(__file__).parent.parent/'static'),
    name='static',
)

templates = Jinja2Templates(directory='templates')

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "homepage.html", {"request":request}
    )