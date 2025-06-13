1. Create "app-quote.py"
2. Create "requirements.txt"
3. Run it locally.
```bash
cd /Users/tripathimachine/Desktop/Apps/GitHub_Repo/Kubernetes/Python-Quote-App

pip install -r requirements.txt

pip show requests
```
4. Create "Dockerfile"
5. Build Image
```bash
docker build -t mayanktripathi4u/python-quotes:v0.0.1 .

```
6. Push Docker Image
```bash
docker push mayanktripathi4u/python-quotes:v0.0.1  
```
7. Run application in Docker: To run application in docker, we will have to create container with above generated image.
```bash
docker run -it --rm mayanktripathi4u/python-quotes:v0.0.1
```
Our application is running inside docker container.
8. Running application in Kubernetes cluster: We can deploy any application in K8S cluster by creating a pod or deployment (K8S maintain lifecycle of pod, if it is deployed as an Deployment). For this create a deployment manifest yaml file to deploy it in K8S.
File: deploy_mainfest.yaml
9. Next step is to deploy this app in K8S cluster by running below kubectl command.
```bash
kubectl apply -f deploy_mainfest.yaml
```
Once the command is executed successfully, K8S will find a node and will schedule this pod and in few mins, image will be pulled and application will start running.
10. How to check?
```bash
kubectl get deployments

kubectl get pods

kubectl logs <pod-id>
```