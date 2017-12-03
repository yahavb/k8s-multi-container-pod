# k8s-multi-container-pod
Design considerations for multi-containers Kubernetes pods
Two or more containers in a pod require a communication method between the containers. The prime example is when all containers needed to be restarted when one container fails abnormally. 
https://kubernetes.io/docs/tasks/access-application-cluster/communicate-containers-same-pod-shared-volume/ suggests a shared-folder-based method for implementing a the multi-container pod lifecycle. Such method enables a container reboot. In case of many containers in a pod, the synchronization task becomes messy.  

The following example uses a centralized approach where an entire pod can be terminated by one of the running containers when it observed an issue. One of the possible solutions is to run a sidecar kubectl container and allows direct access to the API server thru the 127.0.0.1 interface. e.g., when kubectl is enabled.
```$ kubectl proxy --port=8080 &
$ curl http://localhost:8080/api/
{
  "versions": [
    "v1"
  ]
}
```

https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/#accessing-the-api-from-a-pod discusses in greater detail more about this approach. 
However, sidecar container increases the overhead as it duplicates the `kubectl` footprint in the node. 

The example below proposes a single dedicated pod that accessible throughout the namespace via a k8s service. 
The current case supports delete-pod call but is not limited to that action.  
