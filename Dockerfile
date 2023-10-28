FROM python:3.11

ENV PYTHONPATH="${PYTHONPATH}:/project"

WORKDIR /project

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./src/ src/

ENTRYPOINT ["python", "src/app/main.py"]