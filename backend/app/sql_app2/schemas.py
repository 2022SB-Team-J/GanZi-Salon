from typing import List, Optional

from pydantic import BaseModel # 객체 타입설정
#schemas.py works for setting table's type

class ImageBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ImageBase):
    pass


class Item(ImageBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool


    class Config:
        orm_mode = True