import bcrypt
from sqlalchemy.orm import Session

import model
import schemas


def get_user(db: Session, user_id: int):
    return db.query(model.User).filter(model.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.User).offset(skip).limit(limit).all()

def HashPwd(password):
    return bcrypt.hashpw(password=password.encode("utf-8"), salt=bcrypt.gensalt())

def create_user(db: Session, new_user: schemas.NewUser):
    hashed_password = HashPwd(new_user.pswd)
    db_user = schemas.NewUser(id = new_user.id,
                              user_name= new_user.user_name,
                              pswd =  hashed_password,
                              gender = new_user.gender,
                              active = True)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()
#
#
# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = model.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
