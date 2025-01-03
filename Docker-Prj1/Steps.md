# Deploy a Flask App with Docker

Flask App --> Docker ---|
                        |____ 
                        |---- Output Application
MySQL DB  --> Docker ___|                        


**Steps**:
* Server --> Use Local SYstem; AWS EC2; GCP VM etc.
* Docker --> Install on Local Dev platform.
* Code --> Flask App.
* Dockerfile --> Create a file to build image.
* Docker Network
```bash
docker network create my-network

docker network ls
```
* Create and Run the MySQL Container
```bash
docker run -d \
    --name mysql_container-1v \
    --network my-network \
    -e MYSQL_ROOT_PASSWORD=password \
    -e MYSQL_DATABASE=mydb \
    -p 3307:3306 \
    mysql:8.0

docker ps


```
* Verify MySQL Setup
```bash
# Check if the MySQL container is running
docker ps -a

# Enter the MySQL container to check if the database was created.
docker exec -it mysql_container mysql -u root -p

# Once entered into container...
show databases;

use mydb;
```

 


