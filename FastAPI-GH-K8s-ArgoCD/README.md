# Run a FastAPI Application in K8S
Will be using 
- GitHub 
- GitHub Actions
- Docker
- Kubernetes
- ArgoCD

Flow would be something like
```
Developer 
    ⬇️
Push Code Changes 
    ⬇️
Trigger GH Actions 
    ⬇️
GH Actions
- Checkout Code
- Build Docker Image
- Push Image to Docker Hub
- Deploy to K8S
    ⬇️
New Docker Image
    ⬇️
Docker Hub
    ⬇️
Image Notification
    ⬇️
Kubernetes
- Deploy Image
- Run FastAPI App
    ⬇️
Monitoring (Watch)
- ArgoCD
- Sync with GH
- Manage Deployment
```

# Pre-Requisite
Make sure to have DockerHub Account, as we are using DockerHub to push the Image. Alternate could use other Repository / Registry as well such as Google Cloud Artifact Registry; Nexus Repository etc.

Install below if not already

- Docker Desktop
  
```bash
brew install git

brew install kubectl

brew install argocd

brew install minikube
```

Start the Minikube
```bash
# Check for status
minikube status

# If need to stop
minikube stop

# Incase want to delete
minikube delete

# Start the Minikube
minikube start

# Activation
kubectl config use-context minikube

# kubectl is pointing to which cluster and context
kubectl config get-contexts

kubectl get pods -n argocd

kubectl create namespace argocd

# Install ArgoCD in K8S Cluster
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Access ArgoCD server by port forwarding
kubectl port-forward svc/argocd-server -n argcocd 8080:443

# Now access the ArgoCD UI at http://localhost:8080
```

```bash
# Retrieve the Initial Admin password
kubectl get secrets -n argocd

kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}"|base64 --decode
```

Virtual Env.
```bash
python -m venv venv

source venv/bin/activate
```

