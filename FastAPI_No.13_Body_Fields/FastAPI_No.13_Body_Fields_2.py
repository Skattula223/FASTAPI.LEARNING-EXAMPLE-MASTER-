# -*- coding: UTF-8 -*-
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float     = Field(..., gt=0)
    tax: float       = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item = Body(...,
        example={   # exampleBodyexample
            "name": "Foo",
            "description": "A very nice Item",
            "price": 0,
            "toooo": 3.2,
            # "toooooooooo": 3.2, # Item
        },
    )
):
    results = {"item_id": item_id, "item": item}
    return results

    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

