from fastapi import Depends, HTTPException, APIRouter, status
from sqlalchemy.orm import Session

from backend.app.crud import crud
from backend.app.schemas import schemas

api_router = APIRouter(
    tags=["회원가입"],
)

# Dependency
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@api_router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user: #2.
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@api_router.get("/users/", response_model=schemas.User)
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

