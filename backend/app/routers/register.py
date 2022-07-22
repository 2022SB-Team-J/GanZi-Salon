import  bcrypt
from fastapi import Depends, APIRouter, HTTPException, status
from starlette import status
from starlette.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from ..dependencies import get_query_token
from ..models import UserCreate, Token, User




fake_users_db = {
    "johndoe": {
        "id": "johndoe",
        "username": "John Doe",
        "gender": "M",
        "password": "fakehashedsecret",
        "active": False,
    },
    "alice": {
        "id": "alice",
        "username": "Alice Wonderson",
        "gender": "F",
        "password": "fakehashedsecret2",
        "active": True,
    },
}



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
api_router = APIRouter(
    tags=["register"],
    # dependencies=[Depends(get_query_token)]
)

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




class UserInDB(User):
    hashed_password: str

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

# 유효한 계정인지 확인, 의존성 주입
async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@api_router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect user's ID or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect user's ID or password")

    return {"access_token": user.username, "token_type": "bearer"}


@api_router.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

# https://github.com/tiangolo/full-stack-fastapi-postgresql/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/backend/app/app/crud/crud_user.py
# 허밍버드 >>https://github.com/kpuce2022CD/hummingbird/blob/06f5a1a620b398db70fd9fb9d18900718a641b66/frontend/components/SignUpPage/SignUpForm/SignUpForm.tsx4
# https://github.com/RowinChalas/IonicFastHospital/blob/c49a149875c2f2b723913bdc15a84e3da7ed66cc/src/app/pages/inicio-sesion/inicio-sesion.page.ts
# https://github.com/zusdn90/fastapi-signUp-API/blob/b3a161201c18e22a5bc8b2a46d7917211faff1a0/backend/app/api/v1/register.py
@api_router.post("/register_user", status_code=200)
async def register(reg_info:UserCreate):
    # 회원가입
    if reg_info.id :
        return JSONResponse(status_code=400, content=dict(msg="이미 존재하는 ID 입니다."))
    if not reg_info.id or reg_info.password:
        return JSONResponse(status_code=400, content=dict(msg="ID and Password must be provided"))
    if not reg_info.password == reg_info.check_password:
        return JSONResponse(status_code=400, content=dict(msg="비밀번호를 올바르게 썼는지 확인해주세요."))
    if not reg_info.gender :
        return JSONResponse(status_code=400, content=dict("성별을 입력해주세요"))

    # 비밀번호 암호화
    # 여기 말고 crud 할 때 암호화 해도 될 듯?
    # https://github.com/tiangolo/full-stack-fastapi-postgresql/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/backend/app/app/crud/crud_user.py
    hash_pw = bcrypt.hashpw(reg_info.pw.encode("utf-8"), bcrypt.gensalt())

    # user = crud.user.create(db, obj_in=user_in)
    # crud에 들어갈 내용 대체
    new_user = User(
        id = reg_info.id,
        name = reg_info.name,
        gender = reg_info.gender,
        password = hash_pw,
        active = True
    )
    return new_user