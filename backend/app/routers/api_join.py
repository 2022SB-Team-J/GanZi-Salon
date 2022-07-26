import bcrypt
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from starlette.responses import JSONResponse

from ..auth.schemas import JoinUser, User



# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
api_router = APIRouter(
    tags=["회원가입"],
    # dependencies=[Depends(get_query_token)]
)


# https://github.com/tiangolo/full-stack-fastapi-postgresql/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/backend/app/app/crud/crud_user.py
# 허밍버드 >>https://github.com/kpuce2022CD/hummingbird/blob/06f5a1a620b398db70fd9fb9d18900718a641b66/frontend/components/SignUpPage/SignUpForm/SignUpForm.tsx4
# https://github.com/RowinChalas/IonicFastHospital/blob/c49a149875c2f2b723913bdc15a84e3da7ed66cc/src/app/pages/inicio-sesion/inicio-sesion.page.ts
# https://github.com/zusdn90/fastapi-signUp-API/blob/b3a161201c18e22a5bc8b2a46d7917211faff1a0/backend/app/api/v1/register.py
@api_router.post("/api/auth/join", status_code=200)
async def register(reg_info:JoinUser):
    # 회원가입
    # if reg_info.id :
    #     return JSONResponse(status_code=400, content=dict(msg="이미 존재하는 ID 입니다."))
    # if not reg_info.id or reg_info.password:
    #     return JSONResponse(status_code=400, content=dict(msg="ID and Password must be provided"))
    # if not reg_info.password == reg_info.check_password:
    #     return JSONResponse(status_code=400, content=dict(msg="비밀번호를 올바르게 썼는지 확인해주세요."))
    # if not reg_info.gender :
    #     return JSONResponse(status_code=400, content=dict("성별을 입력해주세요"))

    hash_pw = bcrypt.hashpw(reg_info.hashed_password.encode("utf-8"), bcrypt.gensalt())

    # crud에 들어갈 내용 대체
    new_user = JoinUser(
        user_id = reg_info.user_id,
        username = reg_info.username,
        hashed_password = hash_pw,
        gender = reg_info.gender,
        create_at = reg_info.create_at
    )
    print(new_user)
    return new_user
