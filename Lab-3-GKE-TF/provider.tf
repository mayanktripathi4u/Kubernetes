terraform {
  required_providers {
    google = {
        source = "hashicorp/google"
        version = "5.18.0"
    }
  }
}

provider "google" {
  project = "mygcp-project-abc"
  region = "us-central1"
  credentials = "./keys.json"
}