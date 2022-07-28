import bcrypt
from fastapi import APIRouter, status, Depends, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

# from api import user
from ..auth import schemas
from ..db import get_db

# import auth

api_router = APIRouter(
    tags=["register"],
    # dependencies=[Depends(get_query_token)]
)


# 회원가입
@api_router.post("/user/auth/join", response_model=schemas.NewUser)
async def join(request : schemas.NewUser, db: Session = Depends(get_db)):
    new_user = schemas.createUser(request, db)
    return new_user
