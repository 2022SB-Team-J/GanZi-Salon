import sqlalchemy.orm as _orm
import passlib.hash as _hash

from . import db as _database
from . import schemas as _schemas

from . import model as _models

def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
# error
async def create_user(user: _schemas.UserCreate, db: _orm.Session):
    user_obj = _models.UserTable(
        id=user.id, pswd=_hash.bcrypt.hash(user.pswd)
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj

async def get_user_by_id(id: str, db: _orm.Session):
    return db.query(_models.User).filter(_models.User.id == id).frst()