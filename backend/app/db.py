from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from pathlib import Path
from dotenv import load_dotenv

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# ENV_DIR = BASE_DIR.parent.parent
# print(ENV_DIR)
# load_dotenv(os.path.join(ENV_DIR, ".env"))

# user_name = os.environ["DB_USER"]
# password = os.environ["DB_ROOT_PASSWORD"]
# database_name = os.environ["DB_DATABASE"]
# host = "localhost"

user_name = "root"
password = "0701as"
database = "gzsalon"
host = "localhost"

DATABASE = f"mysql+pymysql://{user_name}:{password}@3306:3306/{database}?charset=utf8" 


ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)


session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)


Base = declarative_base()
Base.query = session.query_property()