from typing import List, Optional

from pydantic import BaseModel # 객체 타입설정
#schemas.py works for setting table's type

class ImageBase(BaseModel):
    autonum : int
    create_at : str
    image_url : str


class ItemCreate(ImageBase):
    pass



class Item(ImageBase):
    user_id: int  # example 가 int 로 되어있어 유지하나, 본인은 이것이 str로 주어져야 된다고 생각하고있음
    #owner_id: int # 폐기된 항목

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    gender : str




class UserCreate(UserBase):
    password: str
    user_id: str
    active: bool
    



class User(UserBase):
    create_at : str
    update_at : str

    class Config:
        orm_mode = True