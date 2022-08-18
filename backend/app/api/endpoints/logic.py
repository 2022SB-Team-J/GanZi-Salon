from fastapi import APIRouter, Depends, HTTPException,UploadFile,File,status
from fastapi.responses import JSONResponse
from database import session

from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from models import Image, ImageTable
from typing import List

from PIL import Image
from tempfile import NamedTemporaryFile
import shutil
from shutil import copyfile
from pathlib import Path
import os
from os import rename

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent
SRC_FE_DIR = os.path.join(ASSETS_DIR,'ai_model','assets','celeba_hq','src','female', 'fe')
REF_FE_DIR = os.path.join(ASSETS_DIR,'ai_model','assets','celeba_hq','ref','female', 'fe')
SERVER_IMG_DIR = os.path.join('http://localhost:8000/','app/','img/')

# 사용자 사진 get
@router.get("/getuserimage")
async def get_user_images(image: UploadFile) -> Path:
    print(os.path.realpath(__file__))
    print(os.path.abspath(__file__))
    print(os.listdir(os.getcwd()))
    print(str(os.path.join(SRC_FE_DIR, image.filename)))
    print()
    
    try:
        image.filename = f'src.png'
        suffix = Path(image.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(image.file, tmp)
            tmp_path = Path(tmp.name)
            shutil.copyfile(tmp_path, '/img')
            print('success')
    finally:
        shutil.copyfile(tmp_path, '/img')
    return tmp_path


# Save upload image - hair style image -1
@router.post("/getstyleimage")
def save_image_tmp(image: UploadFile) -> Path:
    
    print(os.path.realpath(__file__))
    print(os.path.abspath(__file__))
    print(os.listdir(os.getcwd()))
    print(str(os.path.join(REF_FE_DIR, image.filename)))
    print()
    
    try:
        image.filename = f'ref.png'
        suffix = Path(image.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(image.file, tmp)
            tmp_path = Path(tmp.name)
            shutil.copyfile(tmp_path, '/img')
            print('success')
    finally:
        shutil.copyfile(tmp_path, '/img')
    return tmp_path


# Save upload image - hair style image -2
@router.post("/getstyleimage2")
async def create_upload_file(uploaded_file: UploadFile = File(...)):    
    # file_location = f"files/{uploaded_file.filename}"
    try:
        file_location = f"/{uploaded_file.filename}"
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(uploaded_file.file, file_object)   
    except Exception as e:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = { 'message' : str(e) }
            )
    else:
        return JSONResponse(
            status_code = status.HTTP_200_OK,
            content = {"info": f"file '{uploaded_file.filename}' saved at '{file_location}'"}
            )     
# https://stackoverflow.com/questions/63580229/how-to-save-uploadfile-in-fastapi



@router.post('/upload-images')
async def upload_board( image : List[UploadFile] = File(...)):
    print(BASE_DIR)
    file_urls=[]
    saved_file_name = 'ref.png'
    print(saved_file_name)

    file_location = os.path.join('.img',saved_file_name)
    with open(file_location, "wb+") as file_object:
        file_object.write(image.file.read())
    file_urls.append(SERVER_IMG_DIR+saved_file_name)
    result={'fileUrls' : file_urls}
    return result
