from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from . import auth
from ..models import User

api_router = APIRouter()

@api_router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = auth.fake_users_db.get(form_data.id)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = auth.UserInDB(**user_dict)
    hashed_password = auth.fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.client_id, "token_type": "bearer"}


@api_router.get("/users/me")
async def read_users_me(current_user: User = Depends(auth.get_current_active_user)):
    return current_user
