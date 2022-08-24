# import bcrypt
from fastapi import Depends, HTTPException, APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm

from ..auth import auth
from ..auth.auth import fake_users_db, fake_hash_password
from ..auth.schemas import UserInDB

api_router = APIRouter(
    tags=["로그인"],
    # dependencies=[Depends(get_query_token)]
)
# @api_router.post("/api/auth/login", status_code=200)
# async def login(reg_info:UserInDB):

    # hash_pw = bcrypt.hashpw(reg_info.hashed_password.encode("utf-8"), bcrypt.gensalt())
    # if hash_pw :# crud에 들어갈 내용 대체
    #     login_user = UserInDB(
    #         user_id = reg_info.user_id,
    #         username = reg_info.username,
    #         hashed_password = hash_pw,
    #         gender = reg_info.gender
    #     )


    # print("login>> ", login_user)
    # return login_user


# @api_router.post("/token")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user_dict = fake_users_db.get(form_data.username)
#     if not user_dict:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     user = UserInDB(**user_dict)
#     hashed_password = fake_hash_password(form_data.password)
#     if not hashed_password == user.hashed_password:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#
#     return {"access_token": user.username, "token_type": "bearer"}
#
#
# @api_router.get("/users/me")
# async def read_users_me(current_user: User = Depends(auth.get_current_active_user)):
#     return current_user
