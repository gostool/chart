## Service 对象
实现服务实例间的负载均衡和不同服务间的服务发现.
同时又为从集群外部访问集群创建了 Ingress 对象。


## service

创建service, 通过选择器关联到pod

使用redis-master-service.yaml 演示:

```
kubectl apply -f redis-master-service.yaml
service/redis-master created
➜  service git:(dev)
➜  service git:(dev) kubectl get svc -o wide
NAME            TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE   SELECTOR
redis-master    ClusterIP   10.99.241.216   <none>        6379/TCP   38s   app=redis-master
➜  service git:(dev)
➜  service git:(dev) kubectl describe service redis-master
Name:              redis-master
Namespace:         default
Labels:            name=redis-master
Annotations:       <none>
Selector:          app=redis-master
Type:              ClusterIP
IP Families:       <none>
IP:                10.99.241.216
IPs:               10.99.241.216
Port:              <unset>  6379/TCP
TargetPort:        6379/TCP
Endpoints:         172.17.0.5:6379
Session Affinity:  None
Events:            <none>
➜  service git:(dev)
```
service(10.99.241.216:6379) ->  pod(172.17.0.5:6379)

```
➜  service git:(dev) kubectl get pod -l "app=redis-master"
NAME                 READY   STATUS    RESTARTS   AGE
redis-master-rdrps   1/1     Running   0          22m
➜  service git:(dev) kubectl describe pod redis-master-rdrps
Name:         redis-master-rdrps
Namespace:    default
Priority:     0
Node:         minikube/192.168.49.2
Start Time:   Wed, 13 Oct 2021 10:22:31 +0800
Labels:       app=redis-master
Annotations:  <none>
Status:       Running
IP:           172.17.0.5
IPs:
  IP:           172.17.0.5
Controlled By:  ReplicationController/redis-master
Containers:
  master:
    Container ID:   docker://3347be80b5f18346f1be70c214271721bcb5425380165859316aa1e17b8ec218
    Image:          kubeguide/redis-master
    Image ID:       docker-pullable://kubeguide/redis-master@sha256:e11eae36476b02a195693689f88a325b30540f5c15adbf531caaecceb65f5b4d
    Port:           6379/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Wed, 13 Oct 2021 10:23:07 +0800
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
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  22m   default-scheduler  Successfully assigned default/redis-master-rdrps to minikube
  Normal  Pulling    22m   kubelet            Pulling image "kubeguide/redis-master"
  Normal  Pulled     21m   kubelet            Successfully pulled image "kubeguide/redis-master" in 34.930811242s
  Normal  Created    21m   kubelet            Created container master
  Normal  Started    21m   kubelet            Started container master
➜  service git:(dev)
```