from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException

# from api import user
import crud, schemas
from db import get_db
# import db

# import auth

api_router = APIRouter(
    tags=["register"],
    # dependencies=[Depends(get_query_token)]
)


# 회원가입
@api_router.post("/user/auth/join", response_model=schemas.NewUser)
async def join(request : schemas.NewUser, db: Session = Depends(get_db)):
    new_user = crud.create_user(request, db)

    if new_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return new_user