from typing import Union, Any
from fastapi import FastAPI, APIRouter, HTTPException

# 1 딕셔너리 형태로 예시 데이터 생성
from .schemas import User

USERS = [
    {
        "id": "1",
        "name": "장아령",
        "password": "WKDDKFUD",
        "active": "TRUE",
    },
    {
        "id": "2",
        "name": "길연쨩",
        "password": "RLFDUSwKD",
        "active": "FALSE",
    },
]

app = FastAPI(title='gz-salon')
# api 통신을 위한 라우터 객체 생성
api_router = APIRouter()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}


@app.get("/item/{item_id}")
def read_user(item_id: str, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# 원하는 사용자 정보 확인, check user wanted
# ================================== 동작하지 않는 부분
@api_router.get("/users/{user_id}", status_code=200, response_model=User)
def fetch_user(*, user_id: str) -> Any:
    # result = [user1 for user1 in USERS if user1["id"] == user_id]
    # if not result:
    #     raise HTTPException(
    #         status_code = 404,
    #         detail="User with ID {user_id} not found"
    #     )

    return {"msg": "Hello, World!"}

    # return result[0]

