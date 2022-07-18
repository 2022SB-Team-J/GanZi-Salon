# main.py
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session, sessionmaker

import sqlalchemy.orm.session

import sql_app2.models
import sql_app2.database
import sql_app2.schemas
import sql_app2.crud


sql_app2.models.Base.metadata.create_all(bind=sql_app2.database.engine)
MYSQL_URL = 'mysql+pymysql://root:administrator@localhost:3306/userdb'
app = FastAPI()


# Dependency
def get_db():
    db = sql_app2.database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users",response_model=sql_app2.schemas.User)
def create_user2(user:sql_app2.schemas.UserCreate, db: Session = Depends(get_db)): # 무조건 typing을 해줘야 에러가 발생하지 않음
    db_user = sql_app2.crud.get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return sql_app2.crud.create_user(db=db, user=user)




#first typed sent

# from fastapi import FastAPI
# from fastapi_sqlalchemy import DBSessionMiddleware #DBseesionMiddelware 를 임포트합니다.
# from fastapi_sqlalchemy import db #데이터 베이스 임포트

# from models import Pharmacy, Worker

# #HOSTNAME = 'localhost'
# #PORT = 3306
# #USERNAME = 'root'
# #PASSWORD = 'administrator'
# #DBNAME = 'userdb'
# MYSQL_URL = f'mysql+pymysql://root:administrator@localhost:3306/userdb'
# #MYSQL_URL = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DBNAME}'

# app = FastAPI()

# angine = create_async_engine(MYSQL_URL, echo=True)
# async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
# session = async_scoped_session(async_session, scopefunc=current_task) 
# #비동기 SQLalchemy 엔진 동작 (2.0 문법대로)
# #needs package can get with "$pip install 'sqlalchemy[asyncio]" and "$pip install aiomysql"
# #if greenlet didn't be installed, you can try that command again


# @app.get('/worker')
# async def select_worker():
#   query = select(Worker)
#   result = await session.execute(query)
#   return result.scalars().all()

# @app.get('/pharmacy')
# async def select_pharmacy():
#   query = select(Pharmacy)
#   result = await session.execute(query)
#   return result.scalars().all()

# @app.get('/worker-pharmacy')
# async def join_worker_pharmacy():
#   query = select(
#       Worker.id,
#       Worker.pharmacy_id,
#       Worker.name,
#       Worker.type,
#       Worker.created_at,
#       Worker.updated_at,
#       Worker.is_deleted,
#       Pharmacy.id.label('ph-id'),
#       Pharmacy.name.label('ph-name'),
#       Pharmacy.address.label('ph-address'),
#       Pharmacy.created_at.label('ph-created_at'),
#       Pharmacy.updated_at.label('ph-updated_at')
#   ).join(
#       Pharmacy,
#       Worker.pharmacy_id == Pharmacy.id
#   )
#   result = await session.execute(query)
#   return result.all()