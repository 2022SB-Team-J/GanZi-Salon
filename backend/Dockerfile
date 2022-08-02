FROM python:latest

COPY ./ /backend

WORKDIR /backend

RUN pip install -r requirements.txt
RUN pip install pydantic
RUN pip install boto3
RUN pip install python-multipart


WORKDIR /backend/app

CMD python -m uvicorn --host=0.0.0.0 --port 8000 main:app