from fastapi import APIRouter
from api.endpoints import users, logic, awsimage

api_router = APIRouter()

api_router.include_router(logic.router, prefix="/logic", tags=["logic"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(awsimage.router, prefix="/awsimages", tags=["awsimages"])