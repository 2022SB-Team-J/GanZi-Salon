from fastapi import APIRouter
from ..auth.schemas import JoinUser, User

api_router = APIRouter(
    tags=["회원가입"],
    # dependencies=[Depends(get_query_token)]
)

# @api_router.post("/api/auth/join", status_code=200)
# async def register(reg_info:JoinUser):
#
