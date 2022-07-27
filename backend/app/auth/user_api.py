from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer

from ..auth.schemas import User

fake_users_db = {
    "johndoe": {
        "user_id": "johndoe",
        "username": "John Doe",
        "gender": "M",
        "hashed_password": "fakehashedsecret",
        "active": False,
    },
    "alice": {
        "user_id": "alice",
        "username": "Alice Wonderson",
        "gender": "F",
        "hashed_password": "fakehashedsecret2",
        "active": True,
    },
    "admin": {
        "user_id": "amin",
        "username": "test admin",
        "gender": "N",
        "hashed_password": "fakehashedsecret3",
        "active": True,
    },
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")




# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return (**user_dict)


# def fake_decode_token(token):
#     # This doesn't provide any security at all
#     # Check the next version
#     user = get_user(fake_users_db, token)
#     return user


# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     user = fake_decode_token(token)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authentication credentials",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     return user


# 활성화 상태 유저인지 판단
async def get_current_active_user(current_user: User):
    if not current_user.active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user