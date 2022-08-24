import os.path

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

BASE_DIR =os.path.dirname(os.path.abspath(__file__))
SECRETE_FILE = os.path.join(BASE_DIR, 'secrete.json')
secrets = json.loads(open(SECRETE_FILE).read())
DB = secrets["DB"]
DATABASE = f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"

engine = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()