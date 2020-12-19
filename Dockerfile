FROM python:3-alpine
WORKDIR /usr/src/app
EXPOSE 80
COPY requirements.txt .
RUN pip install -qr requirements.txt
COPY server.py .
CMD ["python3", "./app.py"]