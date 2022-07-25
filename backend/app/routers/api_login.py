from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from ..auth import auth
from backend.app.auth.schemas import User

api_router = APIRouter(
    tags=["login"],
    # dependencies=[Depends(get_query_token)]
)

@api_router.post("/token")
async def 사용자_로그인(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = auth.fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = auth.UserInDB(**user_dict)
    hashed_password = auth.fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


@api_router.get("/users/me")
async def read_users_me(current_user: User = Depends(auth.get_current_active_user)):
    return current_user
