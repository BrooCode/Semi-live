import shutil
from fastapi import FastAPI, File, UploadFile ,Request
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
 

from starlette.responses import HTMLResponse, StreamingResponse
from typing import Optional


app = FastAPI()
templates = Jinja2Templates(directory="templates/")
import main_gen as key

@app.get('/')
def read_form():
    return 'hello world'

@app.get("/uploadfile",response_class=HTMLResponse)
def form_post(request: Request):
    result = "Upload an image"
    return templates.TemplateResponse('home.html', context={'request': request, 'result': result})

@app.post("/uploadfile",response_class=HTMLResponse)
async def form_post(request: Request,file: UploadFile = File(...)):
    content = await file.read()
    with open(f'{file.filename}',"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    print(content)
    result = key.genearte(file.filename)    
    result = file.filename
    return templates.TemplateResponse('home.html', context={'request': request})

