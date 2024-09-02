#!/bin/bash

# Step 1: Create kind cluster if not exists
if ! kind get clusters | grep -q "^kind$"; then
  echo "Creating kind cluster..."
  kind create cluster
else
  echo "Kind cluster already exists."
fi

# Step 2: Build Docker images
echo "Building Docker images..."
docker build -t web-app:latest -f Dockerfile.app .
docker build -t statistics-script:latest -f Dockerfile.script .

# Step 3: Load images into kind cluster
echo "Loading Docker images into kind cluster..."
kind load docker-image web-app:latest
kind load docker-image statistics-script:latest

# Step 4: Apply Kubernetes manifests
echo "Applying Kubernetes manifests..."

# Ensure manifests exist before applying
if [[ -f "web-app-deployment.yml" && -f "script-deployment.yml" ]]; then
  kubectl apply -f web-app-deployment.yml
  kubectl apply -f script-deployment.yml
else
  echo "Error: Kubernetes manifest files not found!"
  exit 1
fi

echo "Deployment complete!"
