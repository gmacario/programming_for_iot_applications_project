FROM python:3.10.9-slim
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8082
CMD ["python3", "./device_catalog.py"]
