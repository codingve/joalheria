FROM python:3.9.0-buster
WORKDIR /joalheria
COPY requirements.txt . 
RUN pip install -r requirements.txt
# CMD ["python", "app.py"]
COPY . . 
EXPOSE 5000