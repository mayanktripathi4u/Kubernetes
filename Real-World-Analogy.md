# Real-World Analogy
Imagine you are at a concert hall where a large performance is being organized. You (the user) want to book a performance (deploy an app). Let’s look at how the various parts of the system (Kubernetes components) work together to make this happen.

## Key Players:
* You (the User): Want to deploy an application (or request a service).
* Concert Director (API Server): The central point of contact for all requests.
* Stage Manager (Scheduler): Decides where each performance (container) should happen.
* Storage (etcd): Keeps all the records of the concert's schedule, performers, and resources.
* Performers (Containers): The actual apps or services that will run the performance.
* Backstage Crew (Kubelet): Ensures performers (containers) are ready and performing on stage (nodes).
* Audience (Kube Proxy): The audience is routed to the right performance (containers) based on their requests.
* Ticketing System (Controller Manager): Ensures that if one performer (container) fails, a replacement is arranged automatically.
* Technical Crew (Cloud Controller Manager - CCM): Deals with infrastructure-related resources like cloud-specific services (e.g., load balancers, storage).

## Now, let’s connect the dots technically.
1. You (the User) → kubectl → API Server
* You interact with Kubernetes using the command-line tool `kubectl` or via APIs.
* `kubectl` sends requests to the API Server, like “Create a Pod,” “Deploy an app,” or “Scale my app.”
* The `API Server` is the front door to Kubernetes and acts as the central point of communication. It authenticates, validates, and processes requests. All your interactions happen here.
  * API Server: Acts as the entry point for commands and acts as the bridge between the control plane and data plane.
2. API Server → etcd
* The API Server stores the cluster state (what should be running, how many replicas, etc.) in etcd, which is a key-value store.
* etcd is like a permanent record book where Kubernetes stores all its configuration data, including the desired state of your applications.
  * etcd: Stores cluster data (e.g., pod definitions, configurations) to ensure Kubernetes remembers the "desired state."
3. API Server → Controller Manager
* The `Controller Manager` constantly monitors the desired state stored in etcd.
* If a `Pod` or `container` is missing or unhealthy (e.g., a container crashes), the Controller Manager takes action to correct this — like spinning up new Pods to match the desired state.
  * Controller Manager: Monitors the state of the system and ensures that the actual state matches the desired state (e.g., creating new Pods if the current Pods are under-represented).
4. Controller Manager → Scheduler
* The Controller Manager will use the Scheduler to place Pods onto available Nodes (the worker machines).
* The Scheduler is like the stage manager deciding which Node (or machine) is best suited to run your Pods based on resources (CPU, memory) and other factors like node affinity.
  * Scheduler: Determines where to run a new Pod, based on resource availability on each Node.
5. Scheduler → Kubelet
* Once the Scheduler selects a Node to run the Pod, it sends instructions to the `Kubelet` running on that Node.
* The Kubelet is like a backstage crew responsible for ensuring that containers are running on the Node according to the specifications set by Kubernetes (i.e., starting containers, ensuring they're healthy, and stopping them if needed).
  * Kubelet: The agent running on each Node that ensures containers are running properly, maintaining the desired state locally.
6. Kubelet → Container Runtime (containerd)
* The Kubelet works with a container runtime (such as `containerd` or `Docker`) to start, stop, and manage containers inside the Pods.
* `containerd` is the container engine responsible for managing the container lifecycle on the Node (downloading the container image, starting it, and stopping it).
  * containerd: Manages the container lifecycle (pull images, run containers, manage networks).
7. Pod → Kube Proxy
* The Pod contains the application (in the form of a container). If you need to interact with your app (for example, accessing a web service), you don’t interact directly with the Pod.
* Instead, the Kube Proxy manages network traffic and ensures that requests are routed to the correct Pod (or container) based on the service's IP address and ports.
  * Kube Proxy: Handles network routing within the cluster to ensure requests reach the right Pods (containers).
8. Kube Proxy → External Traffic
* If your app needs to be accessed externally (e.g., by a user on the internet), the Kube Proxy ensures that incoming traffic is properly forwarded from the external world to your Pod.
* This can be handled by a Load Balancer or Ingress Controller in the case of web apps.
  * Kube Proxy (or Load Balancer/Ingress Controller): Routes external traffic to the correct internal Pod.
9. Cloud Controller Manager (CCM)
* The Cloud Controller Manager (CCM) integrates Kubernetes with cloud infrastructure like AWS, Google Cloud, or Azure.
* For example, it manages cloud-specific resources like Load Balancers, Storage, and Networking to ensure that Kubernetes can scale with cloud infrastructure.
    * CCM: Manages cloud-specific resources (e.g., provisioning load balancers, setting up persistent storage) in a cloud environment.
10. Control Plane vs. Data Plane
* Control Plane: This is the brain of Kubernetes — it includes the API Server, Controller Manager, Scheduler, etcd, and Cloud Controller Manager (CCM). It makes decisions about how the system should run and manages the state of the cluster.
* Data Plane: This is where the actual work happens — it includes the Nodes and the Kubelet, the Pods, the Container Runtime, and the Kube Proxy. It’s responsible for running containers and handling the application workloads.
  * Control Plane: Makes global decisions about the cluster (e.g., scheduling, health checks, scaling).
  * Data Plane: Runs the application workloads, manages containers and networking at the Node level.

# Full Flow: Request to Deploy an Application
Let's say you want to deploy an app:

1. User (via kubectl) sends a request to Kubernetes to deploy an app.
2. API Server receives the request and stores the desired state (e.g., 3 replicas of a web service) in etcd.
3. Controller Manager sees that 3 replicas are needed and checks the current state.
4. Scheduler selects a Node with enough resources (CPU, memory) to run the Pod.
5. Kubelet on the selected Node receives the Pod creation request and instructs the containerd to pull the container image and start the container inside the Pod.
6. Kube Proxy configures networking so that the app is accessible (both internally and externally) to clients.
7. If you need to expose the app externally, Kube Proxy routes the external traffic to the Pod.


# Terms
* API Server: The entry point for all user requests.
* etcd: A distributed key-value store where Kubernetes stores its configuration data.
* Controller Manager: Ensures the desired state of the system is maintained.
* Scheduler: Decides which Node a Pod should run on.
* Kubelet: Ensures containers run correctly on a Node.
* containerd: The container runtime that handles the actual container management.
* Kube Proxy: Routes traffic to Pods and services.
* Cloud Controller Manager (CCM): Manages cloud-specific infrastructure integration.

Together, these components allow Kubernetes to manage your containerized applications effectively, ensuring they are deployed, maintained, and scaled as needed.