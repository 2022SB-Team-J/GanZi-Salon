from fastapi import FastAPI
from typing import List, Optional
from starlette.middleware.cors import CORSMiddleware  
from db import session 
from model import UserTable, User

app = FastAPI()

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
    users = session.query(UserTable).all()
    return users

# user_id vs id 고려해봐야함
@app.get("/user/{id}")
def read_user(id: int):
    user = session.query(UserTable).\
        filter(UserTable.id == id).first()
    return user


@app.post("/user")
async def create_user(password: str, gender: str):
    user = UserTable()
    user.password = password
    user.gender = gender
    session.add(user)
    session.commit()


@app.put("/users")
async def update_user(users: List[User]):
    for new_user in users:
        user = session.query(UserTable).\
            filter(UserTable.id == new_user.id).first()
        user.password = new_user.password
        user.gender = new_user.gender
        session.commit()