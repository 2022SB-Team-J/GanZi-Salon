from pydantic import BaseModel

class UserBase(BaseModel): 
    class Config:
        orm_mode = True
        
class User(BaseModel):
    user_index: int
    id: str
    user_name: str
    user_password: str
    gender: str
    is_active: bool