- [Steps Overview:](#steps-overview)
- [Prerequisites:](#prerequisites)
- [1. Set Up GKE Cluster](#1-set-up-gke-cluster)
- [2. Build the Flask Application](#2-build-the-flask-application)
- [3. Dockerize the Application](#3-dockerize-the-application)
- [4. Build and Push Docker Image to Google Container Registry (GCR)](#4-build-and-push-docker-image-to-google-container-registry-gcr)
- [5. Create Kubernetes Deployment and Service](#5-create-kubernetes-deployment-and-service)
- [6. Deploy to GKE](#6-deploy-to-gke)
- [7. Access the Application](#7-access-the-application)
- [Code Flow Breakdown](#code-flow-breakdown)
- [Summary:](#summary)


To get started with Google Kubernetes Engine (GKE) and Kubernetes in general, we'll build a simple Python application and deploy it to GKE. The application will be a basic web server built using Flask, and we will use Kubernetes to manage and scale it on GKE. Here's the end-to-end flow and a simple example that covers key steps:

# Steps Overview:
1. Set Up GKE Cluster: Create a Google Cloud project and a GKE cluster.
2. Build a Flask Application: A simple Python Flask application to serve as a basic web server.
3. Dockerize the Application: Create a Docker image for your Flask app.
4. Push Docker Image to Google Container Registry: Push the image to Google Container Registry (GCR).
5. Create Kubernetes Deployment and Service: Write Kubernetes configuration files to deploy the application and expose it.
6. Deploy to GKE: Use `kubectl` to deploy your application to the GKE cluster.
7. Access the Application: Expose your app using a Kubernetes service and access it.

# Prerequisites:
1. Google Cloud SDK (gcloud) installed.
2. `kubectl` installed and configured.
3. A GKE Cluster created via Google Cloud Console or using `gcloud` CLI.


# 1. Set Up GKE Cluster
First, create a GKE cluster if you don't have one. You can create one using the following commands:

```bash
# Authenticate and set up the GKE environment
gcloud auth login
gcloud config set project [PROJECT_ID]   # Set your project ID

# Create a GKE cluster
gcloud container clusters create my-cluster --zone us-central1-a --num-nodes=3
```

# 2. Build the Flask Application
Create a simple Python Flask application. In a directory called `flask-app`, create the following files.

**app.py** (Python Flask Web Application):

```python
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, GKE World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
```

**requirements.txt** (Python dependencies):

```bash
flask==2.1.2
```

# 3. Dockerize the Application
Create a `Dockerfile` to containerize the Flask application.

**Dockerfile**:

```dockerfile
# Use official Python image from Docker Hub
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 to be used by the app
EXPOSE 8080

# Define environment variable to set the Flask app to run on 0.0.0.0
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app
CMD ["python", "app.py"]
```

# 4. Build and Push Docker Image to Google Container Registry (GCR)
Now, build and push the Docker image to Google Container Registry (GCR).

```bash
# Authenticate with Docker
gcloud auth configure-docker

# Build the Docker image
docker build -t gcr.io/[PROJECT_ID]/flask-app:v1 .

# Push the image to Google Container Registry
docker push gcr.io/[PROJECT_ID]/flask-app:v1

```

Make sure to replace [PROJECT_ID] with your actual Google Cloud project ID.

# 5. Create Kubernetes Deployment and Service
Next, we need to create Kubernetes resources for deploying the application.

**deployment.yaml** (Kubernetes Deployment for Flask App):

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: flask-app
  template:
    metadata:
      labels:
        app: flask-app
    spec:
      containers:
      - name: flask-app
        image: gcr.io/[PROJECT_ID]/flask-app:v1
        ports:
        - containerPort: 8080
```

**service.yaml** (Kubernetes Service to expose the Flask App):

```yaml
apiVersion: v1
kind: Service
metadata:
  name: flask-app-service
spec:
  selector:
    app: flask-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
  type: LoadBalancer
```

Replace [PROJECT_ID] with your actual project ID in both files.

# 6. Deploy to GKE
Now, let's deploy the application to GKE.

```bash
# Configure kubectl to interact with the GKE cluster
gcloud container clusters get-credentials my-cluster --zone us-central1-a --project [PROJECT_ID]

# Apply the deployment and service YAML files
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

# 7. Access the Application
Once the deployment and service are applied, Kubernetes will provision a load balancer for your application (this may take a few minutes).

```bash
# Check the service and get the external IP address
kubectl get services
```

Look for the external IP address of the `flask-app-service` under the `EXTERNAL-IP` column. Once the IP is available, open your browser and navigate to that IP address. You should see:

```
Hello, GKE World!
```

# Code Flow Breakdown
1. Flask Application (app.py):

* Creates a simple web server using Flask that returns "Hello, GKE World!" when accessed.
2. Dockerfile:

* Builds a Docker container that includes your Flask app and all dependencies.
* The container exposes port 8080 to allow HTTP traffic to the Flask app.
3. Kubernetes Deployment (deployment.yaml):

* Creates a deployment in GKE with 3 replicas of your Flask app.
* Each replica runs the Flask container exposed on port 8080.
4. Kubernetes Service (service.yaml):

* Exposes your Flask app internally on the cluster using a Kubernetes service.
* Configures the service to be of type LoadBalancer so that it gets an external IP, allowing public access.

# Summary:
By following this example, you have created a basic Python Flask web application, Dockerized it, pushed it to GCR, and deployed it to GKE using Kubernetes. You've learned about the flow from development to containerization and deployment on GKE. You also exposed the application to the internet using a LoadBalancer service.

This process is a simplified version of a full CI/CD pipeline, but it covers many key concepts that will serve as a foundation for learning Kubernetes and GKE.