from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP
from datetime import datetime
from pydantic import BaseModel
from db import Base
from db import ENGINE


class UserTable(Base):
    __tablename__ = "user"
    user_index = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(String(20),unique=True, nullable=False)
    user_name = Column(String(20), nullable=False)
    user_password = Column(String(20),nullable=False)
    gender = Column(String(1), default = 'N')
    is_active = Column(Boolean, default=True)
    create_at = Column(TIMESTAMP, default = datetime.now())
    upload_at = Column(TIMESTAMP, default = datetime.now())


class User(BaseModel):
    user_index: int
    id: str
    user_name: str
    user_password: str
    gender: str
    is_active: bool


class ImageTable(Base):
    __tablename__ = "image"
    image_index = Column(Integer, primary_key=True, autoincrement=True) 
    user_index = Column(Integer, ForeignKey('user.user_index'), nullable=False)
    image_url = Column(String(100), nullable=False)
    create_at = Column(TIMESTAMP, default = datetime.now() )


class Image(BaseModel):
    image_index: int
    user_index: int 
    image_url: str
    create_at: str


def main():
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()