from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static",StaticFiles(directory="static/"),name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



# Ruta para la página de Introducción
@app.get("/fatalidadvelocidad", response_class=HTMLResponse)
async def read_introduccion(request: Request):
    return templates.TemplateResponse("1.fatvel.html", {"request": request})

# Ruta para la página de Definición del Problema
@app.get("/fatalidad", response_class=HTMLResponse)
async def read_problema(request: Request):
    return templates.TemplateResponse("2.fatalidad.html", {"request": request})

# Ruta para la página de Selección y Preparación de Datos
@app.get("/severidad", response_class=HTMLResponse)
async def read_preparacion(request: Request):
    return templates.TemplateResponse("3.severidad.html", {"request": request})

# Ruta para la página de Diccionario de Datos
@app.get("/razones", response_class=HTMLResponse)
async def read_diccionario(request: Request):
    return templates.TemplateResponse("4.razones.html", {"request": request})

# Ruta para la página de Narración con Datos
@app.get("/vias", response_class=HTMLResponse)
async def read_graficos(request: Request):
    return templates.TemplateResponse("5.vias.html", {"request": request})

# Ruta para la página de Implementación Técnica
@app.get("/distribucion", response_class=HTMLResponse)
async def read_implementacion(request: Request):
    return templates.TemplateResponse("6.mapa.html", {"request": request})

@app.get("/diccionario", response_class=HTMLResponse)
async def read_implementacion(request: Request):
    return templates.TemplateResponse("7.diccionario.html", {"request": request})