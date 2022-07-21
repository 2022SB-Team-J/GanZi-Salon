from fastapi import APIRouter, HTTPException, Depends
from typing import Any
from pydantic import BaseModel

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


USERS = [
    {
        "id": "1",
        "name": "장아령",
        "gender": "여성",
        "password": "WKDDKFUD",
        "active": "TRUE",
    },
    {
        "id": "2",
        "name": "우현쨩",
        "gender": "남성",
        "password": "DNGUSwID",
        "active": "FALSE",
    },
]

class User(BaseModel) :
    id : str
    name : str
    gender: str
    password : str
    active : bool

# 회원가입
@router.post("/register",
            status_code=201,
            summary="회원가입")
async def register(user:User):
    return user


# 로그인
@router.post("/login",
             status_code=201,
             summary="로그인")
async def register(user:User):
    return user

# 회원정보 조회
@router.get("/users/", tags=["users"],
            status_code=201,
            summary="회원정보 조회")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}

@router.get("/users/{user_id}", tags=["users"], status_code=200, response_model=User)
async def fetch_user(*, user_id: str) -> Any:
    result = [user1 for user1 in USERS if user1["id"] == user_id]
    if not result:
        raise HTTPException(
            status_code = 404,
            detail="User with ID {user_id} not found"
        )

    return result[0]
    # return {"user_id": str}
