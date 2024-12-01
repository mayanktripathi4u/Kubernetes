# Deploy Python Application using Docker in Google Cloud

Pre-Requisite
* Docker / Docker Desktop installed on your machine.
* Flask installed
* Flask App is ready (regardless of the size it could be a as simple as it could be)
* Google Cloud Account.
* 

# Steps - Deploy a Python application as a Docker Container to the Google Cloud.
1. Flask App 
2. Make sure its running on local.
3. Change the host from local to "0.0.0.0".
4. Create a `Dockerfile` in the same folder as of the app.
5. Navigate to Google Cloud.
6. Enable API for `Cloud Run` and `Cloud Artifcat Registry`.
7. Create Artifcats Registery (either via Console or Shell).
```bash
gcloud artifacts repositories create todorepo --repository-format=docker --location=us-central1 --description="ToDo Repo" --immutable-tags --async
```
8. Next will upload the docker image as artifact which we can then use in a service. 
9. However before that we will use below command
```bash
gcloud auth configure-docker us-central1-docker.pkg.dev
```
which is is used to configure Docker to authenticate with Google Cloud's Artifact Registry (specifically for the us-central1 region) so that you can push or pull Docker images from a private registry hosted by Google Cloud.

   * `gcloud`: This is the command-line tool for interacting with Google Cloud services.
   * `auth configure-docker`: This command configures Docker to use Google Cloud credentials for authentication. Specifically, it sets up Docker to use gcloud's authentication mechanisms to interact with Google Container Registry (GCR) or Google Artifact Registry.
   * `us-central1-docker.pkg.dev`: This specifies the endpoint of the Google Cloud Artifact Registry in the us-central1 region, which is where your Docker images are stored. In this case, it's the registry endpoint for images stored in Artifact Registry.
* It updates Docker's authentication configuration to allow you to push/pull images to/from the Artifact Registry in the `us-central1` region (or the region defined in the gcloud command).
* This typically involves configuring Docker to use credentials from your `gcloud` session, which are linked to your Google Cloud project, to authenticate requests to the registry.
* After running this command, you can perform Docker operations (like `docker push` or `docker pull`) using Google Cloud’s Artifact Registry without needing to manually handle authentication tokens.
10. Navigate to the path where `Dockerfile` is located.
11. Now run the below `gcloud` command
```bash
gcloud builds submit --tag us-central1-docker.pkg.dev/my-gcp-project-id/todorepo/tododockerimage:todotag
```
12. First it will ask for enabling google cloud build if not already enabled. Next it might fail if it does not have sufficient permissions. If fails

Fail Reason: Service Account does not have storage.objects.get access  
```bash
<project_number>...-compute@developer.gserviceaccount.com
```
13. Navigate to GCP IAM, look for above SA, and grant role `Storage Object Viewer`.
14. Re-Run the step 11 for `gcloud builds submit ...`
With this the image is going to be pushed to repository. In the Repository then we are going to see the image. This image will then be used by a Service that we're goign to submit to Cloud Run.
15. Navigate to Cloud Artifact Reistery, and could see an image.
16. Next navigate to `Cloud Run`, and lets create it from Console / GUI.
    * Container Image URL --> Select > Artifact Registery > Choose appropriate image.
    * Configure --> Service Name: <meaningfule name> say `todoimage`
    * Authentication --> For test purpose "Allow unauthenticated innovations".
    * Click Create.
17. This should then deploy the Application successfully. Again its important that the application listens on port 8080, as we have this setup, it should work immediately once the URL is displayed on Cloud Run. Once available visit it, its a public application. 

# Steps - Docker Container locally
Alternate approach is we can build docker container locally, so for this start the docker desktop, from the directory path where `Dockerfile` is present run the below command.

```bash
docker build . --tag us-central1-docker.pkg.dev/my-gcp-project-id/todorepo/tododockerimage:todotag
```
Once completed, push this image to Cloud Artifact Registry.
```bash
docker push us-central1-docker.pkg.dev/my-gcp-project-id/todorepo/tododockerimage:todotag
```
