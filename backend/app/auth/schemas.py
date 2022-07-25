# 타입 힌트를 지원하기 위한 typing 모듈
# typing ?  https://www.daleseo.com/python-typing/
from datetime import datetime
from typing import Sequence
from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    username: str
    gender: str | None = None
    active: bool = True


# 상속
class UserInDB(User):
    hashed_password: str

# 회원가입 시간
class JoinUser(User):
    create_at : datetime | None = None

# 업데이트 시간
class UpdateUser(User):
    update_at : datetime | None = None


# 3  uses Pydantic’s recursive capability to define a field
#   that refers to another Pydantic class we’ve previously defined, the Recipe class
class UserSearchResults(BaseModel):
    # 4 Sequence (which is an iterable with support for len and __getitem__) of Recipes.
    results: Sequence[User]

class Token(BaseModel):
    Authorization: str = None