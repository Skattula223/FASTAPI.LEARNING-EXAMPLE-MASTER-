# -*- coding: UTF-8 -*-
from fastapi import FastAPI
from enum import Enum

class Name(str, Enum):
    Allan = ''
    Jon   = ''
    Bob   = ''

app = FastAPI()


@app.get("/{who}")
async def get_day(who: Name):
    if who == Name.Allan:
        return {"who": who, "message": ""}
    if who.value == '':
        return {"who": who, "message": ""}
    return {"who": who, "message": ""}


@app.get("/")
async def main():
    return {"message": "HelloFastAPI"}



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)