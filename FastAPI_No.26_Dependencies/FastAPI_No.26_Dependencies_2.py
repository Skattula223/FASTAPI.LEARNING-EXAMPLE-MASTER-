# -*- coding: UTF-8 -*-
from fastapi import Depends, FastAPI

app = FastAPI()
# 

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# async def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip": skip, "limit": limit}

# common = CommonQueryParams(),FastAPI
class CommonQueryParams:
    def __init__(self, q: str = None, skip: int = 0, limit: int = 100):
        # __init__FastAPI
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)): # FastAPI
                            # CommonQueryParams FastAPI
# async def read_items(commons=Depends(CommonQueryParams)): √√√√√
# async def read_items(commons: CommonQueryParams = Depends()): √√√√√ 
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    # items = fake_items_db[commons.skip: commons.skip + commons.limit]
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


