#!/bin/bash
cd /home/ec2-user/fastapi-app
docker build -t fastapi-app .
docker run -d -p 8000:8000 --name fastapi-app fastapi-app
echo "PostDeploy: FastAPI app is running in Docker."
