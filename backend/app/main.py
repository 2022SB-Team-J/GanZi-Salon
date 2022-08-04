from typing import List, Optional

from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

from . import model
from .db import session
from .model import UserTable, User
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
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

#         --------------------------->

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


# --------------------------------------------

class UserBase(BaseModel):
    id:str
    class Config:
        orm_mode = True


class UserIn(UserBase):
    # username: str
    password: str
    gender :str


class UserOut(UserBase):
    # username: str
    gender :str
# --------------------^ schemas.py

def get_user_by_id(db: Session, user_id: str):
    return db.query(model.UserTable).filter(model.UserTable.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.UserTable).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserIn):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = model.UserTable(user_idx=2, id=user.id, pswd=fake_hashed_password, gender=user.gender, is_active=True)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# --------------------^ crud.py
# Dependency
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.post("/user/", status_code=201, response_model=UserOut)
async def create_user(user:UserIn, db:Session = Depends(get_db)):
    db_user = get_user_by_id( db,user_id=user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


#
# for new_user in users:
#     user = session.query(UserTable). \
#         filter(UserTable.id == new_user.id).first()
#     user.password = new_user.password
#     user.gender = new_user.gender
@app.put("/users")
async def update_user(users: List[User]):
    pass
























