from typing import Union
from fastapi import FastAPI, APIRouter, Query, HTTPException  # 1

# 1 딕셔너리 형태로 예시 데이터 생성
from backend.app.schemas import User

USERS = [
    {
        "id": 1,
        "name": "장아령",
        "password": "WKDDKFUD",
        "active": "TRUE",
    },
    {
        "id": 2,
        "name": "길연쨩",
        "password": "RLFDUSwKD",
        "active": "FALSE",
    },
]

app = FastAPI(title='gz-salon')
# api 통신을 위한 라우터 객체 생성
api_router = APIRouter()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@api_router.get("/user/user_id", status_code=200, response_model=User)



