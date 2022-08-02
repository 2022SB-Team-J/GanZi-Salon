from fastapi import FastAPI
from typing import List, Optional

from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware  
from db import session 
from model import UserTable, User 
from typing import Union, Any
from fastapi import FastAPI, APIRouter, Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer

# # 1 딕셔너리 형태로 예시 데이터 생성
# # from .models import User

# from .routers import api_join, api_login
# # from .dependencies import get_query_token, get_token_header

app = FastAPI()
# app = FastAPI(title='gz-salon')
# app.include_router(api_login.api_router)
# app.include_router(api_join.api_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------API-----------
@app.get("/hello")
async def read_fastapi_hello():
    print("hellllo")
    return {"Hello" : "fastapii"}

@app.get("/users")
def read_users():
    users = session.query(UserTable).order_by(UserTable.user_idx).all()
    return users


@app.get("/user/{id}")
def read_user(id: str):
    user = session.query(UserTable).\
        filter(UserTable.id == id).first()
    return user

class UserIn(BaseModel):
    username: str
    id : str
    password: str
    gender :str


class UserOut(BaseModel):
    username: str
    id : str
    gender :str


@app.post("/user", status_code=201, response_model=UserOut)
async def create_user(user:UserIn):
    return user


@app.put("/users")
async def update_user(users: List[User]):
    for new_user in users:
        user = session.query(UserTable).\
            filter(UserTable.id == new_user.id).first()
        user.password = new_user.password
        user.gender = new_user.gender
        session.commit()
