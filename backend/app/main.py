from fastapi import FastAPI
from typing import List, Optional
from starlette.middleware.cors import CORSMiddleware  
from .db import session
from .model import UserTable
from .auth.schemas import User
from .routers import user_router

app = FastAPI()
app.include_router(user_router.api_router)

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


@app.post("/user")
async def create_user(id: str, password: str, gender: str):
    user = UserTable()
    user.id = id
    user.password = password
    user.gender = gender
    session.add(user)
    session.commit()


@app.put("/users")
async def update_user(users: List[User]):
    for new_user in users:
        user = session.query(UserTable).\
            filter(UserTable.id == new_user.id).first()
        user.pswd = new_user.password
        user.gender = new_user.gender
        session.commit()