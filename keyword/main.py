import shutil
from fastapi import FastAPI, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
 

from starlette.responses import StreamingResponse
from typing import Optional


app = FastAPI()
templates = Jinja2Templates(directory="templates/")

import main_gen as key


@app.get('/')
def read_form():
    return 'hello world'

@app.get("/items/")
async def read_items(q: Optional[str] = None):
    # results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    results = [[]]
    if q:
        results = key.generate_keyword(q)
    return results

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    with open(f'{file.filename}',"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    print(file.filename)    
    result = key.genearte(file.filename)    
    return result

