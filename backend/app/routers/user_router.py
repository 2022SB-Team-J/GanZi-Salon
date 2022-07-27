import bcrypt
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
api_router = APIRouter(
    tags=["register"],
    # dependencies=[Depends(get_query_token)]
)

# 회원가입
