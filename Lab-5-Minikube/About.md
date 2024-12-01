- [Containerize your Flask App: A guide to Kubernetes deployment](#containerize-your-flask-app-a-guide-to-kubernetes-deployment)
- [Step 1: Installation](#step-1-installation)
  - [Pre-requisites](#pre-requisites)
  - [Installation](#installation)
  - [System Requirements for Minikube](#system-requirements-for-minikube)
- [Step 2: Create a Flask Application](#step-2-create-a-flask-application)
- [Step 4: Deploy Application on Minikube Cluster.](#step-4-deploy-application-on-minikube-cluster)
- [Debug](#debug)


# Containerize your Flask App: A guide to Kubernetes deployment

# Step 1: Installation

## Pre-requisites
* Minikube: Local Kubernetes
  * Minikube creates a single-node kubernetes cluster on your machine. This is great for development and testing.
  * [About Minikube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Fmacos%2Farm64%2Fstable%2Fbinary+download )
* Kubectl: The command-line tool for interacting with Kubernetes.
  * The Kubernetes command-line tool, kubectl, allows you to run commands against Kubernetes clusters. 
  * You can use kubectl to deploy applications, inspect and manage cluster resources, and view logs
* Docker: Docker is a platform that enables developers to automate the deploymeht, scaling and management of applications using containerization. Make sure Docker is installed on your machine.

## Installation
* [Install Minikube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Fmacos%2Farm64%2Fstable%2Fbinary+download)
  * Check for system requirements.
  * Using Home `brew install minikube`
  * Start your cluster: From a terminal with administrator access (but not logged in as root), run: `minikube start` and to check the status run `minikube status`.
* [Install Kubectl](https://kubernetes.io/docs/tasks/tools/)
* If you are on `macOS` and using `Homebrew` package manager, you can install `kubectl` with Homebrew.
  * Run the installation command:
`brew install kubectl`
or
`brew install kubernetes-cli`
  * Test to ensure the version you installed is 
`kubectl version --client`
  * Check if `kubectl` is running by proving the command as `kubectl`.
  * To check how many nodes are there in my minukube cluster, run `kubectl get nodes`

## System Requirements for Minikube
* What you’ll need
  * 2 CPUs or more
  * 2GB of free memory
  * 20GB of free disk space
  * Internet connection
  * Container or virtual machine manager, such as: Docker, QEMU, Hyperkit, Hyper-V, KVM, Parallels, Podman, VirtualBox, or VMware Fusion/Workstation

To check CPU cores and free memory on a Mac using the command line, open Terminal and type the command "`sysctl -n hw.ncpu`" to see the number of CPU cores, and "`top -o mem`" to view a list of processes with their memory usage, where the line with the highest "free" value represents the available memory. 

* Explanation:
* `sysctl -n hw.ncpu`:
  * `sysctl`: A command used to access system information. 
  * `-n`: Option to display only the value of the specified key. 
  * `hw.ncpu`: The key that returns the number of CPU cores. 

* `top -o mem`:
  * `top`: A command that displays a list of active processes with their resource usage. 
  * `-o mem`: Option to sort the output by memory usage.


# Step 2: Create a Flask Application
* Flask is a lightweight web framework for Python that allows developers to build web applications quickly and easily.
* DIrectory structure --> 
```bash
Flask-Web-Application
    |--- app.py --> It serves as the entry point for running the application. When you execute "python app.py", it initializes and starts the web server.
    |
    |--- Dockerfile --> A Dockerfile is a text file that contains a series of instructions used to build a Docker Image. It defines how to setup an application and its environment inside a container.


# Step 3: Build the Docker Image
* Connect to Docker Desktop or start the Docker from Terminal.

```bash
docker build -t flask-app .

docker images

# Tag and Push to DockerHub.
docker tag flask-app <DockerHub login id>/<App Name>:<version>

docker tag flask-app dhmayanktripathi/flask-app:1.0.0

docker login

docker push dhmayanktripathi/flask-app:1.0.0
```



# Step 4: Deploy Application on Minikube Cluster.
* Create `deployment.yaml` file.
* `kubectl apply -f deployment.yaml`
  * deployment.apps/flask-app created
  * service/flask-app created
* `kubectl get deployments`
* `kubectl get service`
* `kubectl get pods`
* `minikube service flask-app` to expose in the browser.

# Debug
If you're running `minikube service flask-app` and the browser opens but doesn't display your app, there could be multiple reasons why the application isn't accessible or not functioning as expected. To debug the issue, follow these steps:

1. Check Minikube Logs and Service Status
Start by checking if the service is running properly and if Minikube has encountered any issues.
   * Check the Service and Pod Status
    First, ensure that your `flask-app` service and its corresponding pods are running without issues. Run the following commands:
```bash
kubectl get svc flask-app
kubectl get pods
```
   * Verify that the flask-app service is assigned an external NodePort (for example, 30080).
   * Ensure that the pod is in the Running state.

    * Check Pod Logs
    If the service and pod are running, but you're still not seeing the app in your browser, check the logs of the pod to identify any application issues. You can find the pod name by running:
```bash
Copy code
kubectl get pods
```
Then, use the following command to view the logs for the pod:
```bash
kubectl logs <pod-name>
```
Look for any errors or stack traces that might indicate issues with the Flask app itself, such as missing dependencies, crashes, or issues binding to the desired port.

   * Check for CrashLoopBackOff or Errors
   * If the pod is restarting or failing, you may see a status like CrashLoopBackOff. In that case, look at the logs for more details.
```bash
kubectl describe pod <pod-name>
```
This will provide detailed information about the pod's state and any recent events. It can help you identify if the app is crashing due to some internal error.

* Check Minikube Dashboard
  * Minikube provides a dashboard that can help you visualize and debug the state of your Kubernetes resources. To open the Minikube dashboard:
```bash
minikube dashboard
```
  * This will open a web-based dashboard in your browser where you can see your pods, services, and logs in a more graphical interface. It can also help you spot issues with your deployments or services.

* Minikube Logs
  * Finally, you can check Minikube's own logs for any issues:
```bash
minikube logs
```
  * This might provide additional insight into issues related to your Minikube VM or Kubernetes configuration.