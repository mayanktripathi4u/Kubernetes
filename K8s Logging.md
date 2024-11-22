- [1. Verify if Cloud Logging is enabled](#1-verify-if-cloud-logging-is-enabled)
- [2. Verify Container Logs are Being Sent to Cloud Logging](#2-verify-container-logs-are-being-sent-to-cloud-logging)
- [3. Check the Logs in Google Cloud Logging](#3-check-the-logs-in-google-cloud-logging)
- [Final Take](#final-take)


In Google Kubernetes Engine (GKE), logs from containers running on the cluster are typically sent to Cloud Logging, which is Google Cloud’s centralized logging service.

# 1. Verify if Cloud Logging is enabled
By default, GKE automatically configures logging for your Kubernetes workloads, and container logs should be sent to Cloud Logging (Google Cloud’s centralized logging platform) if the proper configuration is in place.

Here’s a checklist to verify if logging is enabled:
* Ensure Google Cloud Operations is enabled for the GKE cluster
  * When you create a GKE cluster, Cloud Logging and Cloud Monitoring are usually enabled by default. However, it’s a good idea to verify this:
  * Go to the GKE Cluster settings:
    * Open the Google Cloud Console.
    * Navigate to Kubernetes Engine > Clusters.
    * Select your cluster.
    * In the cluster details, ensure that Cloud Logging is enabled under the Operations section (if not, you can enable it here).

* Check the Logging Configuration in the GKE Cluster
GKE integrates with Google Cloud Operations by default to send logs to Cloud Logging. If this configuration is missing or misconfigured, the logs might not be sent. Follow these steps to verify:
  * Open the Google Cloud Console.
  * Navigate to Kubernetes Engine > Clusters.
  * Click on your cluster to view its details.
  * Look for Cloud Logging and ensure it's enabled under the Operations section. If not, you might need to enable Cloud Logging and Cloud Monitoring from the GKE settings.

# 2. Verify Container Logs are Being Sent to Cloud Logging
In GKE, by default, logs from containers are sent to Cloud Logging through the `Fluentd` agent, which is configured by default on your nodes. Here’s how you can verify that logs are being collected and sent to Cloud Logging:

* Check the logs from the GKE nodes themselves
  * SSH into one of your GKE nodes (if you’re running on Google Cloud Compute Engine nodes). Use the following command:
```bash
gcloud compute ssh <your-node-name> --zone <your-zone>
```
  * Once inside the node, check the Fluentd logs, which are responsible for collecting and forwarding container logs to Cloud Logging:
```bash
sudo journalctl -u google-fluentd
```
    If Fluentd is running properly, you should see logs related to the collection and forwarding of logs from containers to Cloud Logging.

* Check the Kubernetes Logging Configuration
If you want to ensure that your pods are configured correctly for logging, you should look at the `stdout` and `stderr` streams for each container. Kubernetes automatically sends logs from these streams to Cloud Logging if `Fluentd` is running properly.

  * Verify Kubernetes Logging (stdout/stderr): Logs from running containers are collected from the container's stdout and stderr streams. If your application logs to either of these streams, they should be captured by Kubernetes and forwarded to Cloud Logging.
  * You can check the logs of your containers directly via kubectl:
```bash
kubectl logs <pod-name>
```
  If you don’t see the logs in Cloud Logging, make sure that the application inside the container is writing to stdout or stderr correctly.

* Ensure Fluentd is Installed and Configured Properly
In GKE, the Fluentd agent is typically installed by default, but it’s worth verifying if it is configured to forward logs to Cloud Logging.

  * Check for Fluentd Pods (`DaemonSet`): Kubernetes usually runs Fluentd as a DaemonSet on each node. You can verify this by running:
```bash
kubectl get daemonset -n kube-system
```

This should list the fluentd DaemonSet. If it’s missing, Fluentd might not be running on your nodes, which means logs won't be forwarded to Cloud Logging.

If it’s missing or misconfigured, you can manually enable the Cloud Logging agent or reconfigure it. Usually, Fluentd logs are forwarded via a DaemonSet in the `kube-system namespace`, like this:
```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/heapster/master/deploy/kube-fluentd-operator.yaml
```

# 3. Check the Logs in Google Cloud Logging
You can confirm that your logs are being sent to Cloud Logging:

* Open the Google Cloud Console.
* Go to Logging > Logs Explorer.
* In the Logs Explorer, set up a query for your logs. You can filter by resource type (e.g., Kubernetes Container) or project.
  * For a specific namespace and pod:
```bash
resource.type="k8s_container"
resource.labels.cluster_name="your-cluster-name"
resource.labels.namespace_name="your-namespace"
```
* If your logs appear here, everything is working correctly. If you don’t see any logs, you’ll need to investigate further, as detailed below.

4. Troubleshooting: Where Logs Could Be Missing or Misconfigured
If logs are not appearing in Cloud Logging, consider the following common issues:

* Container Log Output
Ensure that your containerized application is logging to stdout or stderr. Kubernetes collects these streams by default. If your app writes logs to files, you’ll need to ensure they are properly forwarded or configured.

* Fluentd Issues
  If Fluentd is not running properly or configured incorrectly, logs will not be forwarded to Cloud Logging. Verify that Fluentd is running as a DaemonSet on all nodes and that it's forwarding logs correctly

* Cloud Logging Configuration
    Ensure that Cloud Logging is enabled for your GKE cluster. This should be automatically enabled, but if it’s missing, you may need to manually enable it via the Google Cloud Console or during cluster creation.

* Check IAM Permissions
    Ensure that your Kubernetes nodes and Fluentd have the necessary IAM permissions to write logs to Cloud Logging. The role roles/logging.logWriter is required for Fluentd to write logs to Cloud Logging.

# Final Take
By default, GKE should automatically send container logs to Cloud Logging, but if logs are missing, ensure the following:

* Google Cloud Operations (Cloud Logging) is enabled on your GKE cluster.
* The Fluentd DaemonSet is running and forwarding logs correctly from your containers.
* Your containerized application is logging to stdout and stderr.
* Cloud Logging is properly configured and your IAM roles are correct.

Once you verify these configurations, you should be able to see your logs in Cloud Logging via the Logs Explorer in the Google Cloud Console.