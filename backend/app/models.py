#models.py configure table (sql)

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
#import needed one
from .database import Base
from datetime import  datetime
# . means local

class User(Base):
    #user table setup
    __tablename__ = "Users"

    user_id = Column(String(20), primary_key=True)
    name = Column(String(20), unique=True, index=True)
    password = Column(String(100) ,index = True )
    create_at = Column(String(30) ,index = True, default = datetime.now())
    upload_at = Column(String(30) ,index = True, default = datetime.now())

    is_active = Column(Boolean, default=True,index = True)
    #gender = Column(Boolean, default = True) #가능성 유
    gender = Column(String(1), default = 'N',index = True )


    #image table setup
class Image(Base):
    __tablename__ = "Images"

    autonum = Column(Integer, primary_key=True) #you can see user : item is constructed 1 : N forms
    user_id = Column(String(20), ForeignKey('Users'),  index=True )
    image_url = Column(String(100), index = True)
    create_at = Column(String(30),index = True ,default = datetime.now() )
#우선 datetime 을 저장하기위해 String 형태로 저장하게 하였으나, 더 나은 방법이있다면 언급부탁드립니다.