from pymysql import TIMESTAMP
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base

class User(Base):
    __tablename__ = "user"

    user_index = Column(Integer, primary_key=True, index=True)
    user_email = Column(String, unique=True, index=True)
    user_name = Column(String, index=True)
    user_password = Column(String)
    gender = Column(String(1), default = 'N')

    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP)
    is_active = Column(Boolean, nullable=False)
