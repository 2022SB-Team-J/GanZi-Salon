from typing import Union, Any
from fastapi import FastAPI, APIRouter, Depends, HTTPException

# 1 딕셔너리 형태로 예시 데이터 생성
from .schemas import User

from .routers import users
from .dependencies import get_query_token, get_token_header



app = FastAPI(title='gz-salon', dependencies=[Depends(get_query_token)])
app.include_router(users.router)
# users 와 items 내에서 사용되는 라우터를 app에 포함시킴

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
@app.get("/", status_code=200)
def root() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}