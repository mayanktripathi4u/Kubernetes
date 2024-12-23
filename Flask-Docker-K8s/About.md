# Project to deploy Flask Application with Docker & K8s

1. Install required Packages `pip install Flask`
2. Create Simple App --> [main.py](./main.py)
3. Create a [Docker File](./Dockerfile)
4. Build Docker Image --> `docker build -t my-flask-docker_img .`
5. Run Docker Container --> `docker run -p 8080:8080 my-flask-docker_img`
6. Above will create and run the Docker Container.
7. Open another terminal and run the curl command to trigger the app.
```bash
curl http://localhost:8080/
```
8. Stop the Docker Container (Control + Z)
9. Till here it is Docker, going forward will work on K8s. 
    * To run on K8s we first need to tag our Docker Image and push it to our Docker Hub.
    * Should have Docker Hub Account. 
    *  
10. Lets create a tag from the image,  
```bash
# Syntax:
docker tag <image name> <docker hub account id>/<tag name>

docker tag my-flask-docker_img dhmayanktripathi/my-flask-docker_img_tag
```
11. Next to login to Docker Hub from Terminal. `docker login`.
12. Push the Docker Image to Docker Hub.
```bash
docker push dhmayanktripathi/my-flask-docker_img_tag
```
13. Next is to create [deployment.yaml](./deployment.yaml)
14. Create the Deployment using K8s, this will create a deployment and a service
```bash
kubectl apply -f deployment.yaml
```
15. Check & validate
```bash
kubectl get deployments

kubectl get services
```
16. Test the Application, will use localhost, as our load balancer is listening to it whic we have determined from `kubectl get services`. Also we do noto mention the port as in our [deployment.yaml](./deployment.yaml) we have set the port as 80, which is a default port. Also as defined `targetPort` as 8080 as our `containerPort` is 8080 (container listens on this port).
```bash
curl http://localhost/ 
```
17. Cleanup the lab.
```bash
kubectl delete service my-flask-docker_img_tag-service

kubectl delete deployment my-flask-docker_img_tag
```
