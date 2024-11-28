terraform {
  backend "gcs" {
    bucket = "gketerraformlab"
    prefix = "terraform/state"
  }
}