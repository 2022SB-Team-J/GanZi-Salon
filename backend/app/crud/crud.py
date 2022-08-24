from sqlalchemy.orm import Session #1.

from ..models import users
from ..schemas import schemas


def get_user(db: Session, user_id: int): #2.
    return db.query(users.User).filter(users.User.id == user_id).first()

def get_user_by_email(db: Session, email: str): #3.
    return db.query(users.User).filter(users.User.user_email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100): #4.
    return db.query(users.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate): #1.
    fake_hashed_password = user.user_password + "notreallyhashed"
    db_user = users.User(user_email=user.email, user_name = user.user_name, hashed_password=fake_hashed_password, is_active = user.is_active)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
