#!/bin/bash
docker stop fastapi-app || true
docker rm fastapi-app || true
echo "PreDeploy: old container stopped/removed."
