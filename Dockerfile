FROM alpine:3.10

FROM python:3.12

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "src/app.py"]

#docker build -t flaskpython .
#docker run -it -p 3000:3000 flaskpython