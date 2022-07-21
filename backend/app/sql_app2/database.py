from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_FILE = os.path.join(BASE_DIR,'secrets.json')
secrets = json.loads(open(SECRET_FILE).read())
DB = secrets["DB"]

#DB_URL = f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"
# 이곳의 db url 이 maindml 것과 같이 제공되도 좋은지 모르겠습니다.

#*_URL = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DBNAME}'
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:administrator@localhost:3306/testdb2" #<= lagacy code
#우선 localhost에서 구동되는걸 중점으로 예시를 적어놓았습니다만, 이것이 유효한가에 대해 의문이 있습니다. 예시를 따라가고 있습니다.

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()