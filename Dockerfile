FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install pip -U && pip install -r requirements.txt

COPY . .

ENTRYPOINT ["pytest"]

CMD ["tests/test_pass.py"]
