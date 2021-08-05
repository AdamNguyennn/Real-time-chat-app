#!/bin/bash 
mkdir tempdir
cp -r chatApp/* tempdir

echo "FROM python" >> tempdir/Dockerfile
echo "WORKDIR /app" >> tempdir/Dockerfile 
echo "COPY requirements.txt requirements.txt" >> tempdir/Dockerfile
echo "RUN pip3 install -r requirements.txt" >> tempdir/Dockerfile
echo "COPY . ." >> tempdir/Dockerfile
echo "CMD [\"python\",\"manage.py\",\"runserver\",\"0.0.0.0:8000\"]" >> tempdir/Dockerfile

cd tempdir
docker build -t samplechat .
docker run -t -d -p 8000:8000 --name chatRunning samplechat
docker ps -a