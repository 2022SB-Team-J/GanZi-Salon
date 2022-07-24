FROM python:3.9

COPY ./ /backend

WORKDIR /backend

RUN pip install -r requirements.txt

WORKDIR /backend/app

CMD python -m uvicorn --host=0.0.0.0 --port 8000 main:app