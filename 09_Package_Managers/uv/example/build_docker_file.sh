#!/bin/bash 

docker build -t fastapi-uv .

docker run -d --name fastapi-uv -p 8888:80 fastapi-uv 

