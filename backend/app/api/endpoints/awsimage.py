from fastapi import APIRouter, Depends, HTTPException,UploadFile,File
from db import session

from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from model import Image, ImageTable

#AWS import something
from aws.bucket import post_bucket
from sqlalchemy.sql import func
import uuid

router = APIRouter()


# image테이블에 있는 모든 data read
@router.get("/images")
def read_images():
    images = session.query(ImageTable).order_by(ImageTable.image_index).all()
    return images

        
# 결과이미지를 aws로 upload
@router.post("/awsupload", status_code=200, description="***** Upload JPG asset to S3 *****")
async def upload(file_object: UploadFile = File(...),):
    file_object.filename = f"{uuid.uuid4()}.jpeg"
    content = await file_object.read()
    post_bucket(content, file_object.filename)
        # forward line upload image to S3 file
    image_file = ImageTable()
    image_file.user_index = 1
    # image_file.user_index = Image.query.join(Image.user_index).filter(User.user_index == session.get('login')).all()
    # I cannot prove this code would work perfectly ,  please give me some opinion.
    image_file.image_url = f"https://ganzibu.s3.amazonaws.com/{file_object.filename}"
    image_file.create_at = func.now()
    session.add(image_file)
    session.commit()
