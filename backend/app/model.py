from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP
from datetime import datetime
from pydantic import BaseModel
from db import Base
from db import ENGINE


class UserTable(Base):
    __tablename__ = "user"
    user_idx = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(String(20),unique=True, nullable=False)
    pswd = Column(String(20),nullable=False)
    gender = Column(String(1), default = 'N')
    create_at = Column(TIMESTAMP, default = datetime.now())
    upload_at = Column(TIMESTAMP, default = datetime.now())
    is_active = Column(Boolean, default=True)


class User(BaseModel):
    user_idx: int
    id: str
    password: str
    gender: str
    is_active: bool


class ImageTable(Base):
    __tablename__ = "images"
    img_idx = Column(Integer, primary_key=True, autoincrement=True) 
    user_idx = Column(String(20), ForeignKey('Users'), nullable=False)
    img_url = Column(String(100), nullable=False)
    create_at = Column(TIMESTAMP, default = datetime.now() )


class Image(BaseModel):
    img_idx: int
    user_idx:str
    img_url: str
    create_at: str


def main():
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()