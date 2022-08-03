from fastapi import APIRouter, Depends, HTTPException,UploadFile,File
from db import session

from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from model import Image, ImageTable
from typing import List

from PIL import Image
import shutil
from pathlib import Path
import os

router = APIRouter()

ASSETS_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent
SRC_FE_DIR = os.path.join(ASSETS_DIR,'ai_model','assets','celeba_hq','src','female', 'fe')
REF_FE_DIR = os.path.join(ASSETS_DIR,'ai_model','assets','celeba_hq','ref','female', 'fe')


# 사용자 사진 get
@router.get("/getuserimage")
async def get_user_images(file_o):
    images = session.query(ImageTable).order_by(ImageTable.image_index).all()
    return images


# 헤어스타일 사진 get
@router.post("/getstyleimage")
async def get_style_images(image: UploadFile = File(...)):
    content = await image.read()
    with open(os.path.join(REF_FE_DIR, image.filename), "wb") as fp:
        fp.write(content)
    print(image.filename)
    return {"filename": image.filename}


async def create_upload_files(files: List[UploadFile] = File(...)):
    UPLOAD_DIRECTORY = "./"
    for file in files:
        contents = await file.read()
        with open(os.path.join(UPLOAD_DIRECTORY, file.filename), "wb") as fp:
            fp.write(contents)
        print(file.filename)
    return {"filenames": [file.filename for file in files]}
