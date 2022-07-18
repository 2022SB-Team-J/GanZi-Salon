from fastapi import APIRouter, HTTPException, Depends, Form
from pydantic import BaseModel
from starlette.responses import JSONResponse

from ..dependencies import get_query_token

class User(BaseModel):
    id: str
    name: str
    gender: str
    password: str
    active: bool = True


api_router = APIRouter(
    tags=["register"],
    dependencies=[Depends(get_query_token)]
)

#
# # https://fastapi.tiangolo.com/tutorial/request-forms/
# @api_router.post("/register", status_code=200, responses=User)
# async def create_user(*, new_user: User):
#     dicted_user = new_user.dict()
#     dicted_user['success'] =True
#
#     return JSONResponse(dicted_user)

@api_router.post("/register/form")
async def regiester(username: str = Form(),
                    password: str = Form(),
                    id: str = Form(),
                    gender: str = Form()):
    return {"username": username,
            "password" : password,
            "id" : id,
            "gender" : gender
            }