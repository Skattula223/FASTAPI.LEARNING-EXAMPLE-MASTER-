# -*- coding: UTF-8 -*-
from fastapi import FastAPI
from starlette.requests import Request
# from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount('/static', StaticFiles(directory='static'), name='static')


# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
#     "http://127.0.0.1:8888"
    
# ]

# app.add_middleware(         # 
#     CORSMiddleware,         # CORS
#     allow_origins=origins,  # allow_origins=['*'], # 
#     allow_credentials=True, # 
#     allow_methods=["*"],    # 
#     allow_headers=["*"],    # 
# )

@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

