	
FROM python:latest

WORKDIR /app/

COPY ./main.py /app/
COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

CMD python -m uvicorn ... --host=0.0.0.0 --port 8000 main:app