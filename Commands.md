- [Kubernetes Commands](#kubernetes-commands)
- [Create Resources](#create-resources)
  - [`kubectl apply -f <file-or-dir>`](#kubectl-apply--f-file-or-dir)
  - [`kubectl create <resource-type> <name> [flags]`](#kubectl-create-resource-type-name-flags)
- [Resources Information](#resources-information)
  - [`kubectl get <resource-type>`](#kubectl-get-resource-type)
  - [`kubectl describe <resource-type> <name>`](#kubectl-describe-resource-type-name)
- [Logs / Debug](#logs--debug)
  - [`kubectl logs <pod-name>`](#kubectl-logs-pod-name)
  - [`kubectl exec <pod-name> -- <command>`](#kubectl-exec-pod-name----command)
  - [`kubectl rollout status <resource-type>/<name>`](#kubectl-rollout-status-resource-typename)
- [Manage](#manage)
  - [`kubectl port-forward <pod-name> <local-port>:<pod-port>`](#kubectl-port-forward-pod-name-local-portpod-port)
  - [`kubectl scale <resource-type>/<name> --replicas=<num>`](#kubectl-scale-resource-typename---replicasnum)
- [Delete / Cleanup](#delete--cleanup)
  - [`kubectl delete <resource-type> <name>`](#kubectl-delete-resource-type-name)
- [Key Differences](#key-differences)


# Kubernetes Commands
comprehensive list of common Kubernetes (kubectl) commands with brief explanations, syntax, examples, and use cases for each:

# Create Resources

## `kubectl apply -f <file-or-dir>`
Create or update resources from a YAML or JSON file.

Example: `kubectl apply -f deployment.yaml`

Use Case: Ideal for managing Kubernetes resources via version-controlled configuration files.

## `kubectl create <resource-type> <name> [flags]`
Create a new resource (e.g., deployment, service, pod).

Example: `kubectl create deployment my-app --image=my-app:v1`

Use Case: Used for quickly creating Kubernetes resources from the command line.


# Resources Information
## `kubectl get <resource-type>`
Retrieve information about a Kubernetes resource.

Example:
```bash
kubectl get pods
kubectl get nodes
kubectl get deployments -o wide
```

Use Case: Used to inspect the current state of resources (e.g., pods, deployments).

## `kubectl describe <resource-type> <name>`
 Show detailed information about a specific resource.

Example: `kubectl describe pod my-pod`

Use Case: Useful for troubleshooting and inspecting the configuration and status of resources.

# Logs / Debug
## `kubectl logs <pod-name>`
View logs of a pod container.

Example:
```bash
kubectl logs my-pod
kubectl logs my-pod -c my-container
```

Use Case: Useful for debugging and checking logs of running containers.

## `kubectl exec <pod-name> -- <command>`
Execute a command inside a container of a pod.

Example:
```bash
kubectl exec my-pod -- ls /app
kubectl exec -it my-pod -- /bin/bash
```

Use Case: Allows for interactive troubleshooting inside containers.

## `kubectl rollout status <resource-type>/<name>`
Show the status of a rollout (e.g., deployment, statefulset).

Example: `kubectl rollout status deployment/my-app`

Use Case: Check the progress of a deployment or update, especially useful after rolling updates.



# Manage
## `kubectl port-forward <pod-name> <local-port>:<pod-port>`
Forward one or more local ports to a pod.

Example: `kubectl port-forward my-pod 8080:80`

Use Case: Useful for accessing services in pods locally (e.g., for testing a web application running in a pod).

## `kubectl scale <resource-type>/<name> --replicas=<num>`
Scale a deployment or replica set to the desired number of replicas

Example: `kubectl scale deployment my-app --replicas=3 `

Use Case: Scaling deployments up or down based on traffic or load


# Delete / Cleanup
## `kubectl delete <resource-type> <name>`
Delete a Kubernetes resource.

Example: 
```bash
kubectl delete pod my-pod
kubectl delete deployment my-deployment
```

Use Case: Used to remove resources from the cluster.




# Key Differences
| Feature	| kubectl create deployment	| kubectl apply -f |
| ----------| --------------------------| ---------------- | 
| Purpose	| Create a new deployment.	| Create or update resources based on configuration files.| 
| Usage Context	| Quick, one-time creation of a resource.	| Ongoing management of resources using declarative files.| 
| Behavior	| Creates a new deployment; fails if the resource exists.	| Creates or updates a resource depending on its existence.| 
| State Management	| Doesn’t track desired state.	| Tracks and ensures the current state matches the desired state.| 
| Version Control	| Not intended for version-controlled management.	| Ideal for version-controlled, declarative management.| 
| Idempotency	| Not idempotent (will fail if the resource already exists).	| Idempotent (applies the same configuration without errors).| 
| | |  | 