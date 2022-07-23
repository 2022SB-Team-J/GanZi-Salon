
## 본인의 뒤떨어지는 판단력에 의해, 스키마가 정상적으로 제공되지 못할 가능성이 높으며, 수정하고싶은 사항이 있다면 알려주시면 감사하겠습니다.

from typing import List, Optional

from pydantic import BaseModel # 객체 타입설정
#schemas.py works for setting table's type

class ImageBase(BaseModel):
    autonum : int
    user_id : str
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
    active: str
    create_at : str
    upload_at : str
    name : str
    gender : str
    



class User(UserBase):
    create_at : str
    update_at : str

    class Config:
        orm_mode = True



