#코드 점검후 app의 main과 합칠것을 고려한다.

from typing import List

from fastapi import FastAPI

from . import model
from .database import engine

models.Base.metadata.create_all(bind= engine)

app = FastAPI()