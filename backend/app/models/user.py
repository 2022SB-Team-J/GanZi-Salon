from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql import func
from database import Base


class UserTable(Base):
    __tablename__ = "user"
    user_index = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(String(20),unique=True, nullable=False)
    user_name = Column(String(20), nullable=False)
    user_password = Column(String(20),nullable=False)
    gender = Column(String(1), default = 'N')
    is_active = Column(Boolean, default=True)
    create_at = Column(TIMESTAMP, server_default = func.now() )
    upload_at = Column(TIMESTAMP, server_default = func.now() )