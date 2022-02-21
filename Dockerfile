FROM python:3.9-slim

WORKDIR /app
RUN chmod 777 /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["bash","start.sh"]