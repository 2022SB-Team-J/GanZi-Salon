# 타입 힌트를 지원하기 위한 typing 모듈
# typing ?  https://www.daleseo.com/python-typing/
from typing import Sequence
from pydantic import BaseModel

# Recipe : BaseModel - from pydantic- 상속
class User(BaseModel):
    id: str
    name: str
    password: str
    active: bool


class UserCreate(BaseModel):
    id: str
    name: str
    password: str
    active: bool

# 3  uses Pydantic’s recursive capability to define a field
#   that refers to another Pydantic class we’ve previously defined, the Recipe class
class UserSearchResults(BaseModel):
    # 4 Sequence (which is an iterable with support for len and __getitem__) of Recipes.
    results: Sequence[User]