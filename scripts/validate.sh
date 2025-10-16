#!/bin/bash
STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/health)
if [ "$STATUS" -ne 200 ]; then
    echo "Health check failed!"
    exit 1
else
    echo "Health check passed!"
fi
