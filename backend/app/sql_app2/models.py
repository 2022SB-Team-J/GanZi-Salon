#models.py configure table (sql)

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
#import needed one
from .database import Base
from datetime import datetime
# . means local

class User(Base):
    #user table setup
    __tablename__ = "Gz_Users"

    user_id = Column(String(20), primary_key=True, index=True)
    name = Column(String(20), unique=True, index=True)
    password = Column(String(100) )
    create_at = Column(String(30), default = datetime.datetime.now() )
    upload_at = Column(String(30), default = datetime.datetime.now() )

    active = Column(Boolean, default=True)
    #gender = Column(Boolean, default = True) #가능성 유
    gender = Column(String(1), default = 'N' )

    images = relationship("Image", back_populates="owner")


    #image table setup
class Image(Base):
    __tablename__ = "Images"

    autonum = Column(Integer, primary_key=True,  autonum = True, index = True) #you can see user : item is constructed 1 : N forms
    user_id = Column(String(20), ForeignKey('Gz_Users', index=True))
    image_url = Column(String(100), index = True)
    create_at = Column(String(30), datetime.datetime.now(),index = True )
#우선 datetime 을 저장하기위해 String 형태로 저장하게 하였으나, 더 나은 방법이있다면 언급부탁드립니다.