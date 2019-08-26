#!/bin/bash
app="docker.test"
docker build -t ${app} .
docker run -d -p 5001:5001 \
  --name=${app} \
  -v "$PWD:/app" ${app}