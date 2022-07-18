#models.py configure table (sql)

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
#import needed one
from .database import Base
# . means local

class User(Base):
    __tablename__ = "users"

    id = Column(String(20), primary_key=True, index=True)
    name = Column(String(20), unique=True, index=True)
    hashed_password = Column(String(100))
    is_active = Column(Boolean, default=True)

    images = relationship("Image", back_populates="owner")


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True) #you can see user : item is constructed 1 : N forms
    title = Column(String(20), index=True)
    description = Column(String(20), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="images")