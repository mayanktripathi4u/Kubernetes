terraform {
  required_providers {
    google = {
        source = "hashicorp/google"
        version = ">= 5.9.0, < 6"
    }
    kubernetes = {
        source = "hashicorp/kubernetes"
    }
  }
  required_version = ">= 0.13"
}