# 타입 힌트를 지원하기 위한 typing 모듈
# typing ?  https://www.daleseo.com/python-typing/
from datetime import datetime
from typing import Optional
from fastapi import HTTPException

import bcrypt
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status

import model



# 신규 유저
class NewUser(BaseModel):
    id:str
    user_name:str
    pswd : str
    gender: str | None = None
    def __int__(self, id, user_name, pswd, gender):
        self.id = id,
        self.user_name = user_name,
        self.pswd = pswd,
        self.gender = gender
# 유저
class User(NewUser):
    user_idx: int | None = None
    create_at : datetime | None = None
    update_at : datetime | None = None
    is_active: bool = True
    class Config:
        orm_mode = True

    # 업데이트. 업데이트 일자 추가 예정
    def updeate(self, user_id, username, password, update_at):
        pass
    # 비활성화. 업데이트 일자 추가 예정
    def inactive(self):
        self.is_active=False

# 비밀번호 암호화
# def HashPwd(password):
#     return bcrypt.hashpw(password=password.encode("utf-8"), salt=bcrypt.gensalt())


# self._password = self.hashed_pass(password=password)

#회원가입
# def createUser(request:NewUser, db:Session):
#     hashed_password = HashPwd(request.pswd)
#     new_user = User(id = request.id,
#                     user_name= request.user_name,
#                     pswd =  hashed_password,
#                     gender = request.gender,
#                     active = True)
#     db.add(new_user)
#     db.commit()
#     db.refresh()
#     return new_user

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