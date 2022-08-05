from .connection import Connect
#from .config import S3_BUCKET
from botocore.exceptions import ClientError
S3_BUCKET="ganzibu"


def post_bucket(image_file: str, key_name: str):
    connect = Connect()
    with connect as client:
        try:
            client = connect.connect()
            client.put_object(
                Body=image_file, Bucket=S3_BUCKET, Key=key_name, ContentType="image.jpeg"
            )
        except ClientError as e:
            print("Error during image upload. {}".format(e.response["Error"]["Code"]))
