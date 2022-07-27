import bcrypt
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
api_router = APIRouter(
    tags=["register"],
    # dependencies=[Depends(get_query_token)]
)
