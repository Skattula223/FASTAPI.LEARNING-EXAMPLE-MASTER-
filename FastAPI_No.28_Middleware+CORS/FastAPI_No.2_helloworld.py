# -*- coding: UTF-8 -*-
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8000"
    
]

app.add_middleware(         # 
    CORSMiddleware,         # CORS
    allow_origins=origins,  # 
    allow_credentials=True, # 
    allow_methods=["*"],    # 
    allow_headers=["*"],    # 
)

@app.get("/")
async def main():
    return {"message": "Hello FastAPI, from get..."}
    
@app.post("/")
async def main1(q: str = None):
    return {"message": "Hello FastAPI, from post..."}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)

