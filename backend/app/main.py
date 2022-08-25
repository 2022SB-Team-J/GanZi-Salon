from fastapi import FastAPI

from .database import engine, Base
from .routers import api_join, api_login


app = FastAPI(title='gz-salon')
app.include_router(api_login.api_router, prefix="/api")
app.include_router(api_join.api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app.get("/users/")
# async def read_users(token: str = Depends(oauth2_scheme)):
#     return {"token": token}