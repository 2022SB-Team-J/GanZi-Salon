FROM python:latest

#COPY ./ /backend
COPY requirements.txt /backend/

WORKDIR /backend

RUN pip install -r requirements.txt
#RUN pip install pydantic


RUN pip install -r requirements.txt

CMD python -m uvicorn --host=0.0.0.0 --port 8000 app.main:app