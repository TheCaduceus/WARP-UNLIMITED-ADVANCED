FROM ubuntu:22.04

WORKDIR /app

RUN apt-get update & apt-get upgrade -y
RUN apt-get -qq install -y git python3 python3-pip

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3","warp-plus.py"]
