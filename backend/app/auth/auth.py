from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer

from ..auth.schemas import User, UserInDB

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


def fake_hash_password(password: str):
    return "fakehashed" + password


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
