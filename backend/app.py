import uvicorn
from fastapi import FastAPI, Request,UploadFile, File
import shutil
import main_gen as key
import s3upload as upload
import s3folder as makefolder
import os
import uuid
import train as train
import chatbot as bot
import json
import s3iterate as link

app = FastAPI()

@app.get('/keyword')
def get_form(request: Request):
    result = "upload your file"
    return  result

@app.post('/keyword')
async def post_form(request: Request, file: UploadFile = File(...)):
    print(file)
    with open(f'{file.filename}',"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    token = str(uuid.uuid4())
    filelink = upload.upload(file.filename,token)
    os.mkdir(token)
    result = key.genearte(file.filename)
    os.remove(file.filename)
    os.remove("my_result.wav")
    return {"result" : result,"link" : filelink,"id":token}

@app.get('/askbot')
def get_form(request: Request):
    result = "pucho banchoo"
    return  result

@app.post('/askbot')
async def post_form(request: Request, ask: str = None,token: str = None):
    result = bot.response(token,ask)
    return {"result" : result}

@app.get('/trainbot')
def get_form(request: Request):
    result = "give it to mee"
    return  result

@app.post('/trainbot')
async def post_form(request: Request,token: str = None):
    t = token + "\intents.json"
    open(t,"W")
    req_info = await request.json()
    temp = token + "\intents.json"
    with open(temp, "r+") as outfile:
        json.dump(req_info, outfile)
    return {"result" : "AutoBots RollOut"}

@app.get('/link')
def get_form(request: Request):
    result = "All the files on s3 "
    return  result

@app.post('/link')
async def post_form(request: Request):
    return {"result" : link.link()}

if __name__ == '__main__':
    uvicorn.run(app)