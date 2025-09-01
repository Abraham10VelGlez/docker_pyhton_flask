FROM python:3.12

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 3000

CMD ["python", "src/app.py"]

# Arranca la app con Gunicorn (4 workers, puerto 3000)


#docker build -t flaskpython .
#docker run -it -p 5000:5000 flaskpython