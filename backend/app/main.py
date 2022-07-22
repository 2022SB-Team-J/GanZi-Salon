
from typing import Union
from fastapi import FastAPI
from . import userdb.main

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
    

# backend / app / main 에서 구동하는 userdb를 만들고, 이후 적용하고자 함
