# Deploy a Flask App with Docker

Flask App --> Docker ---|
                        |____ 
                        |---- Output Application
MySQL DB  --> Docker ___|                        


**Steps**:
* Server --> Use Local SYstem; AWS EC2; GCP VM etc.
* Docker --> Install on Local Dev platform.
* Code --> Flask App. 
  * app.py
  * templates/login.html
  * templates/register.html
  * static/style.css
  * requirements.txt
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

# It was ask for password, use password from "MySQL Container".

# Once entered into container...
show databases;

use mydb;
```

* Update Flask App `app.py` with the MySQL Connection.
```bash
# Add below.
db = mysql.connector.connect (
    host="mysql_container", # MySQL Container Name
    user="root",
    password="password",
    database="mydb"
)
```
* Next step is to Create `Dockerfile`.

 


