FROM python:3.12-slim
WORKDIR /Python-Flask-App
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app-quote.py"]
