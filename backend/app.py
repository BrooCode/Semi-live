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
import uni_s3iterate as uvi_link
import uid_s3iterate as uid_link
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/create_user')
def get_form(request: Request):
    result = "In Process......"
    return  result

@app.post('/create_user')
async def post_form(request: Request, uid: str = None):
    makefolder.makefolder(uid)
    result = "User Created"
    return {"result" : result}

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
    # filelink = upload.upload(file.filename,token)
    os.mkdir(token)
    result = key.genearte(file.filename,token)
    temp = "my_result" + str(token) + ".wav"
    os.remove(temp)
    # os.remove(file.filename)
    return {"result" : result,"id":token}

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
    open(t,"w")
    req_info = await request.json()
    print( type(req_info), type(request))
    train.train(req_info, token)
    temp = token + "\intents.json"
    with open(temp, "r+") as outfile:
        json.dump(req_info, outfile)
    return {"result" : "AutoBots RollOut"}

@app.get('/uid_link')
def get_form(request: Request):
    result = "All the files on this channel"
    return  result

@app.post('/uid_link')
async def post_form(request: Request,uid: str = None):
    return {"result" : uid_link.link(uid)}

@app.get('/uvi_link')
def get_form(request: Request):
    result = "All the files on s3 "
    return  result

@app.post('/uvi_link')
async def post_form(request: Request):
    return {"result" : uvi_link.link()}

if __name__ == '__main__':
    uvicorn.run(app)