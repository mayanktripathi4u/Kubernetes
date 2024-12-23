- [Understand Docker before Kubernetes](#understand-docker-before-kubernetes)


# Understand Docker before Kubernetes
Lets consider an Org as ABC which has its website www.abc.com which is a large commerce company.
When you hot the said website, you will be able to see that there are some products which are displayed on the page, and when you  are thinking to buy kind of product, you are selecting that specific product, next this product goes to the cart, and from the cart once you are clicking on the cart that product goes to the payment page. Basically you will proceed with the payment page details and then the product once the payment is done you will be seeing the order details like order id, estimated delivery and so on.
So how much the user is flowing. The User's journey started from website and he's going to the cart joutney and then to the payment jounrey, and then to order journey, and once the order journey is done what will happen, someone will come to your address to deliver it. 

As the above example is related to Supply Chain Tech. And in this ABC supply chain tech, there is something like `item` and `inventory`, `Transportation`, `fulfillment` and `purchase order`. That's how the entire supply chain journey goes with, and if you notice we have 4 applications in our stack. 
Now what happened, just consider this journey, where there is a Java Application which was converted into a small .jar file with the help of a stack called, DevOps Tool called Maven, and this jar file in order to make sure this jar file is very strong, secured, robust and dependency free. This jar file was placed in a container and that container is called our Docker Container.

Whenever you have K8S software, it will comes with two main components as "Control Plane / Master Node" & "Data Plane / Worker Node".

Each components has some defined task which they perform collectively to accomplish the overall goal of K8S.

Lets take a 4+4 rule theory (just for understanding) designed for kubernetes to make sure that I am able to remember these concepts easily. 

In the Master Node / Control Panel, we do have 4 components, and these are `API Server`, `ETCD`, `Control Manager` and `Scheduler`. 
Similarly on the Worker Node / Data Plane side also we have 4 components with which this entire K8S cluster is running. These are `kubelet`, `kubeproxy`, `pod`, and `Container Runtime`.
For these I am remembering with 4+4 rule theory.

Lets understand deeply one by one, what exactly the each component is doing w.r.t Kubernetes.

Docker: If you have a Docker Software installed, now what will happen is in the docker software there are 10 containers, and there is someone who is managing this container networks. 
Each container talks to each other. The networking of the docker is managed by a component called Bridge Network; Host Network; Overlay Network in Docker. There are 3 types of network in Docker and the default network is the bridge network.

If you consider Docker in the same part of K8S on the Worker Node / Data Plane side, the component that is managing the entire networking of thos worker node is basically your KubeProxy.

In KubeProxy, it will help in Networking component, in assigining the IP address to the containers which are getting created, it will help you to understand, also help in load balancing functionality.

Back to Docker, another important component which maintains the container states, that is your Docker Shim. This Docker Shim bascially will manage the entire management of the containers like it will take the monitoring of the containers, it will take the spin-up; spin-down of the containers, it will also check the container statistics regularly. So this is kind of a controlling of the containers in the Docker. In the same way we can understand this `container runtime` under the worker node, this will manages and monitor the state of containers.

The next component is `Pod`, in above Java Application exacmple we see the transition of the Java File got converted into the jar, and then the jar was converted into a container and with the help of kubernetes this container is converted into a Pod.
This Pod is providing an extra layer of security; extra layer of isolation; extra feature on top of container - Seciruty; robustness; load balancing features.

The last component from worker node is Kubelet, which helps in communicating with the Master Node / Control Plane. It is the primary component in our worker node which decides what to do inside the worker node. Meaning, it i sthe priarmy factor which decides what the Pdo should behave, also collects all the data of the worker nodes and communicates with Master Node. 

Inshort - 
* KubeProxy is mainly utilized for networking inside the worker node. 
* Container Runtime monitorrs and checks the containers inside rhe worker node.
* Pod, feature by K8s which is helping my application to be more robust. Its a smallest component or smallest feature of the K8s, which helos in securing the application and container in a much larger extent, that is your pod.
* Kubelet, which communicates with Master Node, and decides the actions within worker nodes.

Now the Master Node also having 4 components based on our 4+4 rule theory.
the first componenet is API Server; second is ETCD, follwed by Control Manager and finally the Scheduler.

There is only one component which is talking with your kubelet to the API Server the Data Flow. The Data is always 2-way communication.

Consider you as a DevOps Engineer, who is trying to work with the K8S, and the moment you hit the command in the K8s, the K8s will talk with the external environments with the help of API Server. 

Any application in this world (considering K8S as a software), has a front-end and there's a backend. Now K8s is telling if you want to talk with me first talk to API server. If API server says yes then the process / communication proceeds, if says no then the connection get reject.

So the external world talk to the Kubernetes Cluster is with API Servers. 

Whenever you are sending the data to the K8S, it should store the data it somewhere which is ETCD in the master node. `ETCD` stands for `etc` folder inside your linux system; and `d` is for distributed system.

The configuration is this database is present in the master nodes `etc` folder and is a distributed system. 
Whenever you are trying to create a K8S cluster this database is converted as a leader and a worker databases, so you will have a multiple databases to store the data and there will be a leader who will be listening.

Once the data is stored in the format of key and value, there should be a processor who is processing that data and that processor is nothing but the control manager. It manages or controls the entire system. There are various kinds of controllers present, one of node controller --> auto-healing, scaling of nodes. Next is Replication Controller --> which takes care of the entire part of replications, like to maintain minimum number of pods required for my application based on the configuration set.
Next is Network Controller --> which takes care of entire networking part on the kubernetes cluster.
And finally there is a CCM, its basically a Cloud Control Manager, this CCM helps in designing the entire K8s components basically, lets say if you have any open-source Cloud, and want to integrate the K8s with your own cloud, then this CCM will help in integration of all those components and configurations.   



