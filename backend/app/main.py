from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware  

from api.api import api_router

from db import Base
from db import ENGINE


app = FastAPI(title="간지살롱")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

app.include_router(api_router, prefix="/api")


@app.get("/hello")
async def read_fastapi_hello():
    print("hellllo")
    return {"Hello" : "fastapii"}








        

