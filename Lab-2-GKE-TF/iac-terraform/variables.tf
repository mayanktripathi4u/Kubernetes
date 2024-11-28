variable "project_id" {
  description = "The project id to host the cluster in"
  default = " "
}
variable "cluster_name" {
  description = "The name for the GKE CLuster"
  default = "demo-cluster-1"
}
variable "env_name" {
  description = "the environment for the GKE cluetr"
  default = "prod"
}
variable "region" {
  description = "the region to host the cluster in"
  default = "us-west1"
}
variable "kubernets_version" {
  description = "kubernetes version of master" # Check this from google cloud release notes for version nbr.
  default = "1.28.3-gke.1286000"
}
variable "network" {
  description = "the vpc network created to host the cluster in"
  default = "gke-network"
}
variable "subnetwork" {
  description = "the subnetwork created to host the cluster in"
  default = "gke-subnet"
}
variable "ip_range_pods_name" {
  description = "The secondary ip range to use for pods"
  default     = "ip-range-pods"
}
variable "ip_range_services_name" {
  description = "The secondary ip range to use for services"
  default     = "ip-range-services"
}