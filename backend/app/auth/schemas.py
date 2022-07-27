# 타입 힌트를 지원하기 위한 typing 모듈
# typing ?  https://www.daleseo.com/python-typing/
from datetime import datetime
from typing import Sequence
from fastapi import HTTPException

import bcrypt
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status

from backend.app import model



# 유저
class User(BaseModel):
    user_index: int | None = None
    user_id : str
    username: str
    gender: str | None = None
    active: bool = True
    hashed_password: str
    create_at : datetime | None = None
    update_at : datetime | None = None
    # 초기화
    def __init__(self, user_id,username, password, gender):
        self.user_id=user_id
        self.username=username
        self.hashed_password=password
        self.gender=gender
        self.active = True

    # 업데이트. 업데이트 일자 추가 예정
    def updeate(self, user_id, username, password, update_at):
        pass
    # 비활성화. 업데이트 일자 추가 예정
    def inactive(self):
        self.active=False

# 비밀번호 암호화
class HashPwd(BaseModel):
    hashed_password: str
    def __init__(self, password):
        self.hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


#회원가입
def createUser(request:User, db:Session):
    hashed_password = HashPwd(request.password)
    user = User( request.user_id, request.username, hashed_password, request.gender)
    db.add(user)
    db.commit()
    db.refresh()
    return user

# 회원 조회
def showUser(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
        )
    return user

def get_all(db: Session):
    return db.query(model.UserTable).all()




# # 3  uses Pydantic’s recursive capability to define a field
# #   that refers to another Pydantic class we’ve previously defined, the Recipe class
# class UserSearchResults(BaseModel):
#     # 4 Sequence (which is an iterable with support for len and __getitem__) of Recipes.
#     results: Sequence[User]
#
# class Token(BaseModel):
#     Authorization: str = None