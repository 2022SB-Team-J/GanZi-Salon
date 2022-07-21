from fastapi import APIRouter, HTTPException, Depends
from typing import Any
from pydantic import BaseModel
from starlette.responses import JSONResponse

from ..dependencies import get_token_header
from ..models import User

api_router = APIRouter(
    prefix="/login",
    tags=["login"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@api_router.post("/login", status_code=200)
async def login(reg_info:User):
    user : User

    # 임시 로그인
    user.id= "admin"
    user.password= "admin"
    if not user.id == reg_info.id:
        return JSONResponse(status_code=400, content=dict("존재하지 않는 아이디입니다."))

        # db 에서 가져올 때 암호화된 password임
    if not user.password == reg_info.password:
        return JSONResponse(status_code=400, content=dict("비밀번호를 확인해주세요."))

    return user
