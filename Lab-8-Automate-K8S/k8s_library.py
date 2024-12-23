# pip install kubernetes
"""
https://github.com/kubernetes-client/python
https://mckornfield.medium.com/getting-started-with-the-kubernetes-python-client-ac48199537a9
https://www.velotio.com/engineering-blog/kubernetes-python-client

* The library provides access to all Kubernetes API endpoints, allowing you to manage any resource type.
* It supports multiple authentication methods, including kubeconfig files, service accounts, and bearer tokens.
* The library provides a convenient object-oriented interface for interacting with Kubernetes resources.

Check Version:
pip freeze | grep kubernetes
pip show kubernetes

"""
from kubernetes import client, config
import kubernetes

print(f"Kuberenets Library is Loaded. Current version is {kubernetes.__version__}")

# Load Kubernetes configuration from your local kubeconfig file
config.load_kube_config()

# Create an instance of the CoreV1Api client
v1 = client.CoreV1Api()

# List all pods in the default namespace
pods = v1.list_namespaced_pod("default")
for pod in pods.items:
    print(pod.metadata.name)
