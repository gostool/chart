
## k8s minikube node


node:
```
ubuntu@VM-4-8-ubuntu:~$ kubectl describe node
Name:               minikube
Roles:              control-plane,master
Labels:             beta.kubernetes.io/arch=amd64
                    beta.kubernetes.io/os=linux
                    kubernetes.io/arch=amd64
                    kubernetes.io/hostname=minikube
                    kubernetes.io/os=linux
                    minikube.k8s.io/commit=b017ea15ffbf8bcd6ce31e13ba16f59fd4091079
                    minikube.k8s.io/name=minikube
                    minikube.k8s.io/updated_at=2021_09_10T23_34_34_0700
                    minikube.k8s.io/version=v1.20.0
                    node-role.kubernetes.io/control-plane=
                    node-role.kubernetes.io/master=
Annotations:        kubeadm.alpha.kubernetes.io/cri-socket: /var/run/dockershim.sock
                    node.alpha.kubernetes.io/ttl: 0
                    volumes.kubernetes.io/controller-managed-attach-detach: true
CreationTimestamp:  Fri, 10 Sep 2021 23:34:31 +0800
Taints:             <none>
Unschedulable:      false
Lease:
  HolderIdentity:  minikube
  AcquireTime:     <unset>
  RenewTime:       Thu, 16 Sep 2021 10:29:20 +0800
Conditions:
  Type             Status  LastHeartbeatTime                 LastTransitionTime                Reason                       Message
  ----             ------  -----------------                 ------------------                ------                       -------
  MemoryPressure   False   Thu, 16 Sep 2021 10:24:39 +0800   Fri, 10 Sep 2021 23:34:26 +0800   KubeletHasSufficientMemory   kubelet has sufficient memory available
  DiskPressure     False   Thu, 16 Sep 2021 10:24:39 +0800   Fri, 10 Sep 2021 23:34:26 +0800   KubeletHasNoDiskPressure     kubelet has no disk pressure
  PIDPressure      False   Thu, 16 Sep 2021 10:24:39 +0800   Fri, 10 Sep 2021 23:34:26 +0800   KubeletHasSufficientPID      kubelet has sufficient PID available
  Ready            True    Thu, 16 Sep 2021 10:24:39 +0800   Fri, 10 Sep 2021 23:34:50 +0800   KubeletReady                 kubelet is posting ready status
Addresses:
  InternalIP:  192.168.49.2
  Hostname:    minikube
Capacity:
  cpu:                2
  ephemeral-storage:  82503044Ki
  hugepages-1Gi:      0
  hugepages-2Mi:      0
  memory:             3875260Ki
  pods:               110
Allocatable:
  cpu:                2
  ephemeral-storage:  82503044Ki
  hugepages-1Gi:      0
  hugepages-2Mi:      0
  memory:             3875260Ki
  pods:               110
System Info:
  Machine ID:                 822f5ed6656e44929f6c2cc5d6881453
  System UUID:                3eee4665-2f2b-4f82-864c-8c56997b684a
  Boot ID:                    bddd2a3a-f27c-4c3e-8c23-4d5fe237d35e
  Kernel Version:             4.15.0-142-generic
  OS Image:                   Ubuntu 20.04.2 LTS
  Operating System:           linux
  Architecture:               amd64
  Container Runtime Version:  docker://20.10.6
  Kubelet Version:            v1.20.2
  Kube-Proxy Version:         v1.20.2
PodCIDR:                      10.244.0.0/24
PodCIDRs:                     10.244.0.0/24
Non-terminated Pods:          (20 in total)
  Namespace                   Name                                          CPU Requests  CPU Limits  Memory Requests  Memory Limits  AGE
  ---------                   ----                                          ------------  ----------  ---------------  -------------  ---
  db                          redis-client                                  0 (0%)        0 (0%)      0 (0%)           0 (0%)         17h
  db                          redis-master-0                                0 (0%)        0 (0%)      0 (0%)           0 (0%)         16h
  db                          redis-replicas-0                              0 (0%)        0 (0%)      0 (0%)           0 (0%)         16h
  db                          redis-replicas-1                              0 (0%)        0 (0%)      0 (0%)           0 (0%)         16h
  db                          redis-replicas-2                              0 (0%)        0 (0%)      0 (0%)           0 (0%)         16h
  default                     deis-workflow-584dcf6dc7-wxqj6                0 (0%)        0 (0%)      0 (0%)           0 (0%)         16h
  default                     mongo-75f59d57f4-9x7qv                        100m (5%)     0 (0%)      100Mi (2%)       0 (0%)         20m
  default                     nginx-deployment-7fb7fd49b4-9gw57             0 (0%)        0 (0%)      0 (0%)           0 (0%)         41h
  default                     nginx-deployment-7fb7fd49b4-h8ds7             0 (0%)        0 (0%)      0 (0%)           0 (0%)         43h
  default                     nginx-deployment-7fb7fd49b4-v9xpn             0 (0%)        0 (0%)      0 (0%)           0 (0%)         43h
  ingress-nginx               ingress-nginx-controller-8589d6444d-h8j9s     100m (5%)     0 (0%)      90Mi (2%)        0 (0%)         42h
  kube-system                 coredns-54d67798b7-vvqlm                      100m (5%)     0 (0%)      70Mi (1%)        170Mi (4%)     5d10h
  kube-system                 etcd-minikube                                 100m (5%)     0 (0%)      100Mi (2%)       0 (0%)         5d10h
  kube-system                 kube-apiserver-minikube                       250m (12%)    0 (0%)      0 (0%)           0 (0%)         5d10h
  kube-system                 kube-controller-manager-minikube              200m (10%)    0 (0%)      0 (0%)           0 (0%)         5d10h
  kube-system                 kube-proxy-5hx2x                              0 (0%)        0 (0%)      0 (0%)           0 (0%)         5d10h
  kube-system                 kube-scheduler-minikube                       100m (5%)     0 (0%)      0 (0%)           0 (0%)         5d10h
  kube-system                 storage-provisioner                           0 (0%)        0 (0%)      0 (0%)           0 (0%)         5d10h
  kubernetes-dashboard        dashboard-metrics-scraper-7886f6d855-w46vw    0 (0%)        0 (0%)      0 (0%)           0 (0%)         5d10h
  kubernetes-dashboard        kubernetes-dashboard-66f6c8f7c5-hj59l         0 (0%)        0 (0%)      0 (0%)           0 (0%)         5d10h
Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  Resource           Requests    Limits
  --------           --------    ------
  cpu                950m (47%)  0 (0%)
  memory             360Mi (9%)  170Mi (4%)
  ephemeral-storage  100Mi (0%)  0 (0%)
  hugepages-1Gi      0 (0%)      0 (0%)
  hugepages-2Mi      0 (0%)      0 (0%)
Events:              <none>
ubuntu@VM-4-8-ubuntu:~$
```


## service:

```
ubuntu@VM-4-8-ubuntu:~$ kubectl get service
NAME               TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
deis-workflow      ClusterIP   10.99.59.176    <none>        80/TCP         16h
kubernetes         ClusterIP   10.96.0.1       <none>        443/TCP        5d10h
mongo              ClusterIP   10.111.58.141   <none>        27017/TCP      19m
nginx-deployment   NodePort    10.105.168.67   <none>        80:30694/TCP   41h
ubuntu@VM-4-8-ubuntu:~$
```

* ClusterIP: 10.99.59.176
* NodePort: 10.105.168.67

```
ubuntu@VM-4-8-ubuntu:~$ kubectl describe service deis-workflow
Name:              deis-workflow
Namespace:         default
Labels:            app.kubernetes.io/instance=deis-workflow
                   app.kubernetes.io/managed-by=Helm
                   app.kubernetes.io/name=deis-workflow
                   app.kubernetes.io/version=1.16.0
                   helm.sh/chart=deis-workflow-0.1.0
Annotations:       meta.helm.sh/release-name: deis-workflow
                   meta.helm.sh/release-namespace: default
Selector:          app.kubernetes.io/instance=deis-workflow,app.kubernetes.io/name=deis-workflow
Type:              ClusterIP
IP Families:       <none>
IP:                10.99.59.176
IPs:               10.99.59.176
Port:              http  80/TCP
TargetPort:        http/TCP
Endpoints:         172.17.0.14:80
Session Affinity:  None
Events:            <none>
ubuntu@VM-4-8-ubuntu:~$
```

## 查看 nginx-deployment
rc:3

```
ubuntu@VM-4-8-ubuntu:~$ kubectl get pod
NAME                                READY   STATUS    RESTARTS   AGE
nginx-deployment-7fb7fd49b4-9gw57   1/1     Running   0          41h
nginx-deployment-7fb7fd49b4-h8ds7   1/1     Running   0          43h
nginx-deployment-7fb7fd49b4-v9xpn   1/1     Running   0          43h
ubuntu@VM-4-8-ubuntu:~$
```

```
ubuntu@VM-4-8-ubuntu:~$ kubectl describe service nginx-deployment
Name:                     nginx-deployment
Namespace:                default
Labels:                   <none>
Annotations:              <none>
Selector:                 app=nginx
Type:                     NodePort
IP Families:              <none>
IP:                       10.105.168.67
IPs:                      10.105.168.67
Port:                     <unset>  80/TCP
TargetPort:               80/TCP
NodePort:                 <unset>  30694/TCP
Endpoints:                172.17.0.6:80,172.17.0.7:80,172.17.0.8:80
Session Affinity:         None
External Traffic Policy:  Cluster
Events:                   <none>
ubuntu@VM-4-8-ubuntu:~$
```

```
ubuntu@VM-4-8-ubuntu:~$ kubectl describe pod nginx-deployment-7fb7fd49b4-9gw57
Name:         nginx-deployment-7fb7fd49b4-9gw57
Namespace:    default
Priority:     0
Node:         minikube/192.168.49.2
Start Time:   Tue, 14 Sep 2021 16:49:19 +0800
Labels:       app=nginx
              pod-template-hash=7fb7fd49b4
Annotations:  <none>
Status:       Running
IP:           172.17.0.6
IPs:
  IP:           172.17.0.6
Controlled By:  ReplicaSet/nginx-deployment-7fb7fd49b4
Containers:
  nginx:
    Container ID:   docker://9be65e54769ee5399c3be4b2df7699a833adba066d861fc99a87523bbaf38142
    Image:          nginx:alpine
    Image ID:       docker-pullable://nginx@sha256:686aac2769fd6e7bab67663fd38750c135b72d993d0bb0a942ab02ef647fc9c3
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Tue, 14 Sep 2021 16:49:21 +0800
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-x5c76 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  default-token-x5c76:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-x5c76
    Optional:    false
QoS Class:       BestEffort
Node-Selectors:  <none>
Tolerations:     node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                 node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:          <none>
ubuntu@VM-4-8-ubuntu:~$
```


```
ubuntu@VM-4-8-ubuntu:~$ kubectl describe pod nginx-deployment-7fb7fd49b4-h8ds7
Name:         nginx-deployment-7fb7fd49b4-h8ds7
Namespace:    default
Priority:     0
Node:         minikube/192.168.49.2
Start Time:   Tue, 14 Sep 2021 15:03:52 +0800
Labels:       app=nginx
              pod-template-hash=7fb7fd49b4
Annotations:  <none>
Status:       Running
IP:           172.17.0.8
IPs:
  IP:           172.17.0.8
Controlled By:  ReplicaSet/nginx-deployment-7fb7fd49b4
Containers:
  nginx:
    Container ID:   docker://70e3d1813107ac8815f66df3a930de5ee2ca2e80a1b16bc3ffdcddd3170991bf
    Image:          nginx:alpine
    Image ID:       docker-pullable://nginx@sha256:686aac2769fd6e7bab67663fd38750c135b72d993d0bb0a942ab02ef647fc9c3
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Tue, 14 Sep 2021 15:03:53 +0800
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-x5c76 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  default-token-x5c76:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-x5c76
    Optional:    false
QoS Class:       BestEffort
Node-Selectors:  <none>
Tolerations:     node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                 node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:          <none>
ubuntu@VM-4-8-ubuntu:~$
```





