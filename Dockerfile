FROM python:3.11

WORKDIR /src

COPY . /src

RUN pip install --no-chache-dir -r requirements.txt

CMD ["python", "./app/main.py"]