#!/bin/bash
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker build -t testing .
docker run -v $(pwd)/database:/app/database testing