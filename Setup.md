# Setting Up Env

# Create Virtual Env to work on the Kubernetes Projects
```bash
cd /Users/tripathimachine/Desktop/Apps/GitHub_Repo/Kubernetes

python3 -m venv k8s-venv

source k8s-venv/bin/activate
```

# Work on your Project
Once virtual env is activated navigate to speciifc project directory and make changes or run accordingly.

## Deploy Python Streamlite ML Model into Kubernetes
[Code](/Kubernetes/ML-Streamlit/)
[Details on Obsidian](obsidian://open?vault=Obsidian%20Vault&file=Container%2FK8S%2FHands-On)


# Dockerizing the Project
Make sure Docker is Running.

Navigate to specific path where Dockerfile exists for your project.


```bash
docker images

docker build -t streamlit-ml-app:v1.0.0 .

docker run -p 8501:8501 streamlit-ml-app:v1.0.0

# Incase Fails: due to address already in use. Error below. Use command.
sudo lsof -t -i :8501 | xargs sudo kill -9
```

Error:
```bash
docker: Error response from daemon: Ports are not available: exposing port TCP 0.0.0.0:8501 -> 127.0.0.1:0: listen tcp 0.0.0.0:8501: bind: address already in use.
```

# Push to DockerHub

Connect to [DockerHub](https://hub.docker.com/)


