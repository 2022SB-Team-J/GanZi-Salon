from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE = f"mysql+pymysql://root:0701as@db:3307/gzsalon?charset=utf8"

engine = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)

session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()