from fastapi import Depends, FastAPI, Header, HTTPException

from routers import users,items
# from .routers import items, users

app = FastAPI()

async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token": # 
        raise HTTPException(status_code=400, detail="X-Token header invalid") # X


app.include_router(users.router)
app.include_router(items.router,
    # 
    prefix="/items",
    tags=["items"],
    # 
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)