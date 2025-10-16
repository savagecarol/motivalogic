#!/bin/bash
cd /home/ec2-user/fastapi-app
echo "Installing dependencies..."
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt

echo "Starting FastAPI app..."
nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
