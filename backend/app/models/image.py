from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql import func

class ImageTable(Base):
    __tablename__ = "image"
    image_index = Column(Integer, primary_key=True, autoincrement=True) 
    user_index = Column(Integer, ForeignKey('user.user_index'), nullable=False)
    image_url = Column(String(100), nullable=False)
    create_at = Column(TIMESTAMP, server_default = func.now())