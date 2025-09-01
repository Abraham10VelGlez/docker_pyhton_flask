FROM alpine:3.10

FROM python:3.12

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 3000

# CMD ["python", "src/app.py"]

# Arranca la app con Gunicorn (4 workers, puerto 3000)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:3000", "src.app:app"]


#docker build -t flaskpython .
#docker run -it -p 5000:5000 flaskpython