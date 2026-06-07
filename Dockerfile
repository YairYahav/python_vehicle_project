FROM python:3.11 

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY src/ ./src
COPY logs/ ./logs

VOLUME ["/app/logs"]

CMD ["python", "-u", "src/main.py"]