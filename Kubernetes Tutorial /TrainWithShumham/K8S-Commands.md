Start Minikube, [minukube start options](https://minikube.sigs.k8s.io/docs/commands/start/)

Now Minikube supports [multi-node](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)

```bash
# start the cluster
minikube start 

# 
# -n, --nodes   --> int     --> The total number of nodes to spin up. Defaults to 1. (default 1)
# -p, --profile --> string  --> The name of the minikube VM being used. This can be set to allow having multiple instances of minikube independently. (default "minikube")
minikube start --nodes 3 -p minikube-multinode-demo

minikube status

# view the cluster details.
kubectl cluster-info

```

Stop Minikube
```bash
minikube stop
```

Get All Namespaces
```bash
kubectl get namespace
or
kubectl get ns
```

Output would be 
* default --> 
* kube-node-lease --> 
* kube-public --> 
* kube-system --> 
* local-path-storage --> 
* kubernetes-dashboard --> 

Create a New Namespace, say the name as nginx, choose any meaningful name.
```bash
kubectl create ns nginx
```

CHeck the COntext
```bash
kubectl config get-contexts

kubectl config current-context
```
Incase it errors when working with GKE from your local shell, you may face issue. In that case stop the Minikube and restart.

Run the Namespace / Create Pod for nginx.
```bash
# Create Pod in default namespace.
kubectl run nginx --image=nginx 

# Checking in Default Namespace.
kubectl get pods

# As we have created in Default Namespace the below command will return "No Resources found in nginx namespace".
kubectl get pods -n nginx

# Delete Pod
kubectl delete pod nginx

# Create Pod in given namespace
kubectl run nginx --image=nginx -n nginx

kubectl get pods
kubectl get pods -n nginx
kubectl delete pod nginx -n nginx
kubectl delete ns nginx

```

# Create Pod via mainefest or configuration file.
```bash
# Create Namespace
kubectl apply -f nginx-namespace.yml

kubectl get ns

# Crate Pod
kubectl get pods -n nginx
kubectl apply -f nginx-pod.yml
kubectl get pods -n nginx
```

Open Interactive Terminal (work inside Pod)
```bash
kubectl exec -it nginx-pod -n nginx -- bash
```
It will take you or open the bash terminal to work inside the pod.
Output would look like 
```bash
root@nginx-pod:/# 
root@nginx-pod:/# ls
root@nginx-pod:/# curl 127.0.0.1

# To exit out of the interactive terminal.
root@nginx-pod:/# exit
```
We can run `ls` command, and to see the "Welcome to nginx" html code.. run the `curl` command as `curl 127.0.0.1`.


For Debug purpose, we could view the details of the prod.
```bash
kubectl describe pod/nginx-pod -n nginx
```

Deployment
```bash
# Make sure to delete the previous created nginx-pod created via nginx-pod.yml.
kubectl delete -f nginx-pod.yml 

kubectl apply -f nginx-deployment.yml 

kubectl get deployment -n nginx

# Verify if two Pods are created, as we set replicas as 2.
kubectl get pods -n nginx

# Incase we have to scale this (up or down) and create 5 replicas use below.
kubectl scale deployment/nginx-deployment -n nginx --replicas=5

# Check more details of Pods.. likw on which worker node it is running.
kubectl get pods -n nginx -o wide

# Delete Deployment
kubectl delete -f nginx-deployment.yml
```


ReplicaSet
```bash
# Make sure to delete the previous created pod created via nginx-deployment.yml.
kubectl delete -f nginx-deployment.yml

kubectl apply -f nginx-replicaSet.yml 

kubectl get replicasets -n nginx

# Verify if two Pods are created, as we set replicas as 2.
kubectl get pods -n nginx

# Delete replicaSet
kubectl delete -f nginx-replicaSet.yml
```

DaemonSet
```bash
# Make sure to delete the previous created pod created via nginx-replicaSet.yml.
kubectl delete -f nginx-replicaSet.yml

kubectl apply -f nginx-daemonSets.yml

kubectl get daemonSet -n nginx

# Verify if two Pods are created.
kubectl get pods -n nginx

kubectl get pods -n nginx -o wide

# Delete daemonSet
kubectl delete -f nginx-daemonSets.yml

```

Job
```bash

kubectl apply -f job.yml

kubectl get job -n nginx

# Verify if two Pods are created.
kubectl get pods -n nginx

kubectl get pods -n nginx -o wide

# CHeck Logs
kubectl logs pod/demo-job-669tm -n nginx

# Delete daemonSet
kubectl delete -f job.yml

```

CronJob
```bash
kubectl apply -f cronjob.yml

kubectl get cronjob -n nginx

kubectl get pods -n nginx

kubectl logs pod/minute-backup-28925566-l7gzd  -n nginx

# Delete CronJob
kubectl delete -f cronjob.yml
```