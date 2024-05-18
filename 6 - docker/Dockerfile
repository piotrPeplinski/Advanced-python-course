FROM python:3.10.7

WORKDIR /app

COPY test.py /app
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "test.py"]
