import os.path

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

# BASE_DIR =os.path.dirname(os.path.abspath(__file__))
# SECRETE_FILE = os.path.join(BASE_DIR, 'secrete.json')
# secrets = json.loads(open(SECRETE_FILE).read())
# DB = secrets["DB"]

# DATABASE = f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"

DATABASE = "mysql+pymysql://root:0701as@db:3307/gzsalon?charset=utf8"

engine = create_engine(
    DATABASE,
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()