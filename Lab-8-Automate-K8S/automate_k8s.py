from kubernetes import client, config
from kubernetes.client.exceptions import ApiException

# kubernetes: This is the official Python client library for interacting with Kubernetes clusters.
# pip install kubernetes
# client: This module provides access to the various Kubernetes APIs, allowing you to manage resources like pods, deployments, services, etc.
# config: This module is used to load your Kubernetes configuration (usually from a kubeconfig file) so that your script can authenticate and interact with the Kubernetes API.
# ApiException: This is a specific exception class provided by the Kubernetes client library. It is raised when there are errors during API calls (e.g., when trying to read a pod that doesn’t exist or if there are permission issues). Catching this exception allows for better error handling in your code.


import time,random,string

def load_kube_config(): #load_kube_config is defined to encapsulate the logic for loading the Kubernetes configuration.
    try:                #The try block is used to execute code that might raise exceptions
        config.load_kube_config()  #This line calls the load_kube_config() method from the config module of the Kubernetes client library. loads the Kubernetes configuration from the default kubeconfig file (usually located at ~/.kube/config on most systems).
        print(f"Kubeconfig Loaded")
    except Exception as e:
        print(f"Error loading kube config: {e}")  #If an error occurs while trying to load the kubeconfig (for example, if the file does not exist or is improperly formatted), this line catches the exception and assigns it to the variable e
        exit(1)

def list_namespaces(): #list_namespaces is defined to encapsulate the logic for listing Kubernetes namespaces.
    #client.CoreV1Api() creates an instance of the CoreV1Api class from the Kubernetes client library.
    #Purpose: The CoreV1Api class provides methods to interact with various core resources in Kubernetes, including namespaces, pods, services, and more.
    v1 = client.CoreV1Api()
    try:
        #v1.list_namespace() CALLS THE list_namespace() method on the v1 API client.
        #Purpose: This method retrieves a list of all namespaces in the Kubernetes cluster.
        namespaces = v1.list_namespace()
        print("Namespaces:")
        #This loop iterates over the items attribute of the namespaces object, which contains the list of namespace objects
        for ns in namespaces.items:
            #For each namespace object (ns), it prints its name by accessing ns.metadata.name
            print(f"- {ns.metadata.name}")
    except ApiException as e:
        print(f"Exception when listing namespaces: {e}")

def list_pods(namespace):  #list_pods is defined to encapsulate the logic for listing pods in a specific Kubernetes namespace.
    #client.CoreV1Api() creates an instance of the CoreV1Api class from the Kubernetes client library.
    #Purpose: This instance provides access to methods for interacting with core Kubernetes resources, including pods.
    v1 = client.CoreV1Api()
    print(f"\nListing pods in namespace: {namespace}")
    try:
        #This line calls the list_namespaced_pod() method on the v1 API client, passing the specified namespace as an argument
        pods = v1.list_namespaced_pod(namespace)
        #This loop iterates over the items attribute of the pods object, which contains the list of pod objects.
        #For each pod object (pod), it prints its name and current status. The status is accessed using pod.status.phase, indicating whether the pod is running, pending, succeeded, failed, etc.
        for pod in pods.items:
            print(f"- {pod.metadata.name} ({pod.status.phase})")
    except ApiException as e:
        print(f"Exception when listing pods: {e}")

def create_deployment(namespace, name, image):  #It is defined to encapsulate the logic for creating a deployment in a Kubernetes namespace.
#     namespace: The namespace where the deployment will be created.
# name: The name of the deployment.
# image: The container image to be used for the deployment.
    apps_v1 = client.AppsV1Api() #This line creates an instance of the AppsV1Api class from the Kubernetes client library.
# This block defines a container using the V1Container class:
# name: The name of the container, set to the value of the name parameter.
# image: The Docker image to be used, set to the value of the image parameter.
# ports: Specifies which ports to expose (in this case, port 80).
    container = client.V1Container(
        name=name,
        image=image,
        ports=[client.V1ContainerPort(container_port=80)]
    )

    spec = client.V1PodSpec(containers=[container]) #This line creates a pod specification (V1PodSpec) that includes the previously defined container.
#     This creates a pod template specification (V1PodTemplateSpec):
# metadata: Sets labels for the pod, allowing for easier identification and management.
# spec: Sets the pod specification that includes the container.

    template = client.V1PodTemplateSpec(metadata=client.V1ObjectMeta(labels={"app": name}), spec=spec)
#     This creates a deployment specification (V1DeploymentSpec):
# replicas: Sets the desired number of pod replicas (1 in this case).
# selector: Specifies how to select the pods managed by the deployment using labels. This is necessary for the deployment to manage the pods correctly.
# template: Includes the pod template specification defined earlier.

    deployment_spec = client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(match_labels={"app": name}),  # Add this line
        template=template
    )

# This creates the deployment object (V1Deployment):
# api_version: Specifies the API version for the deployment resource.
# kind: Specifies that this resource is a Deployment.
# metadata: Sets the metadata for the deployment, including its name.
# spec: Includes the deployment specification defined earlier.
    deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name=name),
        spec=deployment_spec
    )

# This try block attempts to create the deployment in the specified namespace using the create_namespaced_deployment method.
# If successful, it prints a message with the deployment name and its status.
    try:
        api_response = apps_v1.create_namespaced_deployment(
            namespace=namespace,
            body=deployment
        )
        print(f"Deployment '{name}' created. Status='{api_response.status}'")
    except ApiException as e:
        print(f"Error creating deployment: {e}")

def delete_deployment(namespace, name):
    apps_v1 = client.AppsV1Api()
#  Purpose
# This try block attempts to delete a specific deployment in a given Kubernetes namespace using the Kubernetes API. If any errors occur during this operation, control will be transferred to the corresponding except block to handle those errors.

# Components Explained
# api_response =:
# This variable is assigned the result of the API call to delete the deployment. The response will typically contain information about the status of the deletion request.
# apps_v1.delete_namespaced_deployment(...):
# This is a method call to the delete_namespaced_deployment function of the apps_v1 client instance. This method specifically targets a deployment in a particular namespace for deletion.

# Parameters:

# name=name:
# This specifies the name of the deployment to be deleted. The name variable is expected to contain the name of the deployment that was passed to the delete_deployment function.
# namespace=namespace:
# This specifies the namespace where the deployment resides. The namespace variable should contain the namespace that was passed to the function.
# body=client.V1DeleteOptions(...):
# This parameter provides options for how the deletion should be handled. The V1DeleteOptions class is used to specify these options.
# client.V1DeleteOptions(...):

# This class is used to define deletion behavior for the resource.
# propagation_policy='Foreground':
# This option specifies how resources that depend on the deployment should be deleted.
# Foreground: The deletion will wait for the dependent resources (like pods) to be deleted first before deleting the deployment itself. This ensures that there is no abrupt termination of dependent resources.
# grace_period_seconds=5:
# This option sets a grace period for the deletion, giving resources time to shut down gracefully. In this case, it waits for 5 seconds before forcibly terminating any remaining resources related to the deployment.
    try:
        api_response = apps_v1.delete_namespaced_deployment(
            name=name,
            namespace=namespace,
            body=client.V1DeleteOptions(propagation_policy='Foreground', grace_period_seconds=5)
        )
        print(f"Deployment '{name}' deleted. Status='{api_response.status}'")
    except ApiException as e:
        print(f"Error deleting deployment: {e}")

#once the deployment is created , it will create a pod with deployment name and some random string . To get the exact pod name below function
#can be used .
#Get the pod name starting with deployment name

def get_pod_name_by_deployment_name(namespace, deployment_name):
    # Load Kubernetes configuration
    config.load_kube_config()
    v1 = client.CoreV1Api()

    # List pods in the specified namespace
    try:
        pods = v1.list_namespaced_pod(namespace)
        # Find the pod names starting with the deployment name by iterating through all the pod names
        matching_pods = [pod.metadata.name for pod in pods.items if pod.metadata.name.startswith(deployment_name)]
        return matching_pods
    except client.exceptions.ApiException as e:
        print(f"Error fetching pods: {e}")
        return []

#Checking the health of pod , parameters pod name and namespace.
def check_pod_health(namespace, pod_name):
    v1 = client.CoreV1Api()
    try:
        print(pod_name)
        #The overall purpose of this line is to fetch the details of a specific pod identified by its name (the first element of the pod_name list) within the specified namespace.
        pod = v1.read_namespaced_pod(name=pod_name[0], namespace=namespace)
        status = pod.status.phase
        print(status)
        if status == "Running":
            print(f"Pod '{pod_name}' is running.")
            return True
        else:
            print(f"Pod '{pod_name}' is in state: {status}")
            return False
    except ApiException as e:
        print(f"Error checking pod health: {e}")
        return False

def main():
    #Calling the function to load kubeconfig present at the default location in system ~./kube/config
    load_kube_config()
    
    #default namespace we are using .
    namespace = "default"  # Change as needed
    #calling to list all the ns in your cluster
    list_namespaces()
    #Listing all the pods in particular ns
    list_pods(namespace)
    
    #defining the deploymemt to be created and which image your deployment will use .
    deployment_name = "devopstechstack-deployment"
    image = "nginx:latest"
    
    # Create a new deployment
    #create_deployment(namespace, deployment_name, image)
    
    # Wait for the pod to be ready
    time.sleep(20)  # Wait for a few seconds for the pod to initialize
    
    #Calling the function to get exact pod name.
    pod_names = get_pod_name_by_deployment_name(namespace, deployment_name)
    print(f"Pods starting with '{deployment_name}': {pod_names}")
    
    # Check pod health
    check_pod_health(namespace, pod_names)

    # Uncomment to delete the deployment
    #  delete_deployment(namespace, deployment_name)

if __name__ == "__main__":
    main()


# Reference: https://www.youtube.com/watch?v=S9lQ7VoaAyg&list=PLnsGW1CrMg9woZHOkG3iEUTNpovpKRHKC&index=4 
