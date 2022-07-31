from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from crud import HashPwd
from model import UserTable
# from schemas import NewUser

# from api import user
import crud, schemas
from db import get_db, session

# import db

# import auth

api_router = APIRouter(
    tags=["register"],
    # dependencies=[Depends(get_query_token)]
)

# 회원가입
# @api_router.post("/auth/user/join")
# def createUser(request:NewUser, db:Session):
#     hashed_password = HashPwd(request.pswd)
#     new_user = UserTable()
#     new_user.id= request.id
#     new_user.pswd= hashed_password
#     new_user.gender= request.gender
#     new_user.is_active= True
#     db.add(new_user)
#     db.commit()
#     db.refresh()
#     return new_user

@api_router.post("/auth/user/join")
async def create_user(id: str, password: str, gender: str):
    user = UserTable()
    user.id = id
    user.pswd = password
    user.gender = gender
    session.add(user)
    session.commit()

# # 회원가입
# @api_router.post("/user/auth/join", response_model=schemas.NewUser)
# async def join(request : schemas.NewUser, db: Session = Depends(get_db)):
#     new_user = crud.create_user(request, db)

#     if new_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return new_user
