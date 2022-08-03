from fastapi import APIRouter
from api.endpoints import user, logic, awsimage

api_router = APIRouter()

api_router.include_router(logic.router, prefix="/logic", tags=["logic"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(awsimage.router, prefix="/awsimage", tags=["awsimage"])
