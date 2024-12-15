# Multi-Node Kubernetes Setup using Kubeadm

* AWS Account
* Pre-requisite
  * Atleast two Ubunti 18.04 or higher servers available for creating the cluster.
  * Each server has at least 2 GB of RAM and 2 CPU Cores.
  * The servers have network connectivity to each other.
  * Have root access to each server.
* Create an EC2 Instances
  * First Instance: 
    * Name: Master_Node
    * Ubuntu
    * Instance Type: t2-medium
    * Key-Pair (Optional)
    * Configure Storage: 8 GB
    * Launch
  * Second Instance:
    * Name: Worker_Node_1
    * Ubuntu
    * Instance Type: t2-medium
    * Key-Pair (Optional)
    * Configure Storage: 8 GB
    * Launch
  * Third Instance:
    * Name: Worker_Node_2
    * Ubuntu
    * Instance Type: t2-medium
    * Key-Pair (Optional)
    * Configure Storage: 8 GB
    * Launch
  * Installation
    * COnnect to Master_Node EC2 Instance
    * COmmands
```bash
sudo apy-get update
sudo apt install apt-transport-https curl -y
```
    * Install **containerd** using command
```bash
sudo mkdir -p /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpc | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install containerd.io -y

```
    * Create containerd configuration
```bash
sudo mkdir -p /etc/containerd

sudo containerd config default | sudo tee /etc/containerd/config.toml

# Update the SystemdCgroup to True, default it was false.
sudo sed -i -e 's/SystemdCgroup = false/SystemdCgroup = true/g' /etc/containerd/config.toml

# Restart the Containerd
sudo systemctl restart containerd
```
  * 
* Install Kubernetes
  * to install K8S, use the commands
```bash
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list

sudo apt-get update

sudo apt-get install -y kubelet kubeadm kubectl

sudo apt-mark hold kubelet kubeadm kubectl

sudo systemctl enable --now kubelet
```
  * and more commands...... [refer](https://www.youtube.com/watch?v=7W6D8iHEnpg&list=PLj-3PZlPbUVT9FLR0MufSw3isCxEDScO8&index=11) for more commands.

Repeat the same for other 2 EC2 Instances for Worker Nodes.
