from typing import Union, Any
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

# 1 딕셔너리 형태로 예시 데이터 생성
# from .models import User

from .routers import api_join, api_login
# from .dependencies import get_query_token, get_token_header


app = FastAPI(title='gz-salon')
app.include_router(api_login.api_router)
app.include_router(api_join.api_router)



@app.get("/")
async def root():
    return {"message": "Hello World"}



# @app.get("/users/")
# async def read_users(token: str = Depends(oauth2_scheme)):
#     return {"token": token}