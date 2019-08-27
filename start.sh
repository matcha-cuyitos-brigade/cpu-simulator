#!/bin/bash
app="flask-api"
docker build -t ${app}:latest .
docker run -p 5000:80 ${app}