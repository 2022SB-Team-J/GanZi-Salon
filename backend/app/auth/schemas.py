from pydantic import BaseModel


class UserBase(BaseModel):
    user_email: str
    user_name: str
    gender : str


class UserCreate(UserBase):
    user_password: str
    is_active: bool


class User(UserBase):

    class Config:
        orm_mode = True
