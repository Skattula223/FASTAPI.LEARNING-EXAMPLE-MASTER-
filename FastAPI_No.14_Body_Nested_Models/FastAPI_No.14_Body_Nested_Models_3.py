# -*- coding: UTF-8 -*-
from typing import List, Dict

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl    # URLJSON Schema / OpenAPI
                    #  https://pydantic-docs.helpmanual.io/usage/types/
    name: str

# 
@app.post("/images/multiple/")
async def create_multiple_images(*, images: List[Image]):
    return images

# dicts (/)()
@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]): 
    return weights



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

