FROM python:3.11

ENV PYTHONPATH="${PYTHONPATH}:/project"

WORKDIR /project

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./src/ src/

EXPOSE 8081/tcp

ENTRYPOINT ["python", "src/app/main.py"]