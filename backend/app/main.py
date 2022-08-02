from fastapi import FastAPI
from typing import List, Optional
from starlette.middleware.cors import CORSMiddleware  
from db import session 
from model import UserTable, User , Image, ImageTable
from typing import Union, Any
from fastapi import FastAPI, APIRouter, Depends, HTTPException,UploadFile,File

#AWS import something
from aws.bucket import post_bucket
from sqlalchemy.sql import func
import uuid

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
    users = session.query(UserTable).order_by(UserTable.user_index).all()
    return users


@app.get("/user/{id}")
def read_user(id: str):
    user = session.query(UserTable).\
        filter(UserTable.id == id).first()
    return user


@app.post("/user")
async def create_user(id: str, name : str ,  password: str, gender: str):
    user = UserTable()
    user.id = id
    user.user_name = name
    user.user_password = password
    user.gender = gender
    session.add(user)
    session.commit()


@app.put("/users")
async def update_user(users: List[User]):
    for new_user in users:
        user = session.query(UserTable).\
            filter(UserTable.id == new_user.id).first()
        user.user_password = new_user.password
        user.gender = new_user.gender
        session.commit()

@app.post("/upload", status_code=200, description="***** Upload JPG asset to S3 *****")
async def upload(file_object: UploadFile = File(...),):
    file_object.filename = f"{uuid.uuid4()}.jpeg"
    content = await file_object.read()
    post_bucket(content, file_object.filename)
        # forward line upload image to S3 file
    image_file = ImageTable()
    image_file.user_index = 1
   # image_file.user_index = Image.query.join(Image.user_index).filter(User.user_index == session.get('login')).all()
    #I cannot prove this code would work perfectly ,  please give me some opinion.
    
    image_file.image_url = f"https://ganzibu.s3.amazonaws.com/{file_object.filename}"
    image_file.create_at = func.now()
    session.add(image_file)
    session.commit()
