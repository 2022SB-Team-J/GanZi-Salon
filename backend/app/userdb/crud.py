#crud.py   데이터베이스의 데이터와 상호작용 및 재사용함수가 있음

from sqlalchemy.orm import Session
from . import models, schemas
from . import database

# import sql_app.models # 절대경로로 불러오는방법
# import sql_app.schemas # 절대경로로 불러오는방법


def create_user(db: Session, user: schemas.UserCreate): #파라미터로 받은 db 를 활용해 쿼리를 날리고 user는 payload값으로 보면된다. 함수 실행은 main.py에서 실행
    #schemas에서 지정한 UserCreate를 가져와서 Typehinting 을 하였다.
    fake_hashed_password = user.password + "notreallyhashed"
    #일단 fakehashedpassword를 사용하나, 실제론 사용해선 안된다.
    db_user = models.User(create_at = user,user_id = user.user_id ,name=user.name, password=fake_hashed_password,)
    #우선 능력부족으로 name 로 이용중이나 이를 변형해, 이름데이터를 기록할 생각이다.
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    
def create_image(db : Session, image : schemas.UserCreate):
    db_image = models.Image()

