#!/bin/bash
echo "Stopping any existing FastAPI app..."
pkill -f "uvicorn main:app" || true
