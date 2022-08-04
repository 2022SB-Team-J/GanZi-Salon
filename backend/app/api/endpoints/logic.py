from fastapi import APIRouter, Depends, HTTPException,UploadFile,File
from database import session

from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schemas.image_schema import Image
from models.image import ImageTable
from typing import List
from api.dep import get_db

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



@router.post("/upload-file/")
async def create_upload_file(uploaded_file: UploadFile = File(...)):    
    # file_location = f"files/{uploaded_file.filename}"
    file_location = f"img/{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(uploaded_file.file, file_object)    
    return {"info": f"file '{uploaded_file.filename}' saved at '{file_location}'"}