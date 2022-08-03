from pydantic import BaseModel

class ImageBase(BaseModel): 
    class Config:
        orm_mode = True

class Image(BaseModel):
    image_index: int
    user_index: int 
    image_url: str
    create_at: str
