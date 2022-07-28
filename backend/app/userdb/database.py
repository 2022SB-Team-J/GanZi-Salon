from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_FILE = os.path.join(BASE_DIR,'secrets.json')
secrets = json.loads(open(SECRET_FILE).read())
DB = secrets["DB"]

DB_URL = f"mysql+pymysql//{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"

engine = create_engine(
    DB_URL , encoding = 'utf-8'
)

#위 세션은 아직 데이터베이스가 아님 SessionLocal: 데이터베이스 세션 클래스, 이를 이용해 생성한 인스턴스가 실제 데이터베이스 세션이 된다.
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()
#DB모델이나 클래스를 만들기 위해 선언한 클래스(후에 상속해서 사용함)

#requirements에 추가했으나, sqlalchemy와 pymysql이 추가되었는가 검토한다.