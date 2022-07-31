import fastapi as _fastapi
import fastapi.security as _security

import passlib.hash as _hash
import sqlalchemy.orm as _orm

from typing import List
from starlette.middleware.cors import CORSMiddleware  
# # from db import session
# from model import UserTable
# from schemas import User
# import user_router

# import model as _model
from . import service as _services
from . import schemas as _schmas


app = _fastapi.FastAPI()
# app.include_router(user_router.api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------API-----------
@app.get("/")
async def read_fastapi_hello():
    print("hellllo")
    return {"Hello" : "fastapii"}

# @app.get("/users")
# def read_users():
#     users = session.query(UserTable).order_by(UserTable.user_idx).all()
#     return users


# @app.get("/user/{id}")
# def read_user(id: str):
#     user = session.query(UserTable).\
#         filter(UserTable.id == id).first()
#     return user


@app.post("/api/users")
async def create_user(user: _schmas.UserCreate, db: _orm.Session = _fastapi.Depends(_services.get_db())):
    db_user = await _services.get_user_by_id(user.id, db)
    if db_user:
        raise _fastapi.HTTPException(status_code=400, detail="id is already in database")
    return await _services.create_user(user, db)

# @app.post("/user")
# async def create_user(id: str, password: str, gender: str):
#     user = UserTable()
#     user.id = id
#     user.password = password
#     user.gender = gender
#     session.add(user)
#     session.commit()


# @app.put("/users")
# async def update_user(users: List[User]):
#     for new_user in users:
#         user = session.query(UserTable).\
#             filter(UserTable.id == new_user.id).first()
#         user.pswd = new_user.password
#         user.gender = new_user.gender
#         session.commit()