from typing import Union
from fastapi import FastAPI
#for run fastapi backend framework server
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#import the SQLAlchemy parts

SQLALCHEMY_DATABASE_URL = "mysql://./sql_app.db" #this sql url is virtual ( not defined )
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
) # for sqlalchemy run their engine, i made this to communicate with sql
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#this "SessionLocal" is still not a database session yet
#We name it sessionlocal to disting

Base = declarative_base()
#Base model declar

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
