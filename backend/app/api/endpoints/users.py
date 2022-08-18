from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import session

from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from typing import List
from schemas.user_schema import User
from models.user import UserTable
from api.dep import get_db

router = APIRouter()


# user테이블에 있는 모든 유저 read
@router.get("/readusers")
def read_users():
    users = session.query(UserTable).order_by(UserTable.user_index).all()
    return users


# user테이블에 있는 유저 검색 <- user id로 검색
@router.get("/user/{id}")
def read_user(id: str):
    user = session.query(UserTable).\
        filter(UserTable.id == id).first()
    return user


# create user 
@router.post("/createuser")
async def create_user(id: str, name: str, password: str, gender: str):
    user = UserTable()
    user.id = id
    user.user_name = name
    user.user_password = password
    user.user_name = name
    user.gender = gender
    session.add(user)
    session.commit()


@router.put("/updateuser")
async def update_user(users: List[User]):
    for new_user in users:
        user = session.query(UserTable).\
            filter(UserTable.id == new_user.id).first()
        user.user_password = new_user.password
        user.name = new_user.name
        user.gender = new_user.gender
        session.commit()

