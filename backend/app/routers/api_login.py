from fastapi import Depends, HTTPException, APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm

from ..auth import auth
from ..auth.auth import fake_users_db, fake_hash_password
from ..auth.schemas import User, UserInDB

api_router = APIRouter(
    tags=["login"],
    # dependencies=[Depends(get_query_token)]
)

@api_router.post("/auth/user/login")
async def login(user:User):
    print(user)

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
