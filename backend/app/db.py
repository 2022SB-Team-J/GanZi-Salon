from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from pathlib import Path
from dotenv import load_dotenv
import json
import os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# #ENV_DIR = (BASE_DIR.parent).parent
# #ENV_DIR = Path(__file__).resolve(strict=True).parent
# load_dotenv(os.path.join(BASE_DIR, ".env"))

# user_name = os.environ["DB_USER"]
# password = os.environ["DB_ROOT_PASSWORD"]
# database_name = os.environ["DB_DATABASE"]
# host = os.environ["DB_HOST"]

# DATABASE = f"mysql+pymysql://{user_name}:{password}@{host}:3306/{database_name}?charset=utf8" 
DATABASE = f"mysql+pymysql://root:0701as@db:3306/gzsalon?charset=utf8" 

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# SECRET_FILE = os.path.join(BASE_DIR,'secrets.json')
# secrets = json.loads(open(SECRET_FILE).read())
# DB = secrets["DB"]

# DATABASE = f"mysql+pymysql://{DB['user']}:{DB['password']}@db:3306/{DB['database']}?charset=utf8"


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