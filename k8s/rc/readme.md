## rc
* 创建rc

k8s权威指南第四版 第一章

```
➜  rc git:(dev) kubectl apply -f redis-master-controller.yaml
replicationcontroller/redis-master created
➜  rc git:(dev) kubectl get rc
NAME           DESIRED   CURRENT   READY   AGE
redis-master   1         1         0       3s
➜  rc git:(dev) kubectl describe rc
Name:         redis-master
Namespace:    default
Selector:     app=redis-master
Labels:       name=redis-master
Annotations:  <none>
Replicas:     1 current / 1 desired
Pods Status:  0 Running / 1 Waiting / 0 Succeeded / 0 Failed
Pod Template:
  Labels:  app=redis-master
  Containers:
   master:
    Image:        kubeguide/redis-master
    Port:         6379/TCP
    Host Port:    0/TCP
    Environment:  <none>
    Mounts:       <none>
  Volumes:        <none>
Events:
  Type    Reason            Age   From                    Message
  ----    ------            ----  ----                    -------
  Normal  SuccessfulCreate  12s   replication-controller  Created pod: redis-master-rdrps
➜  rc git:(dev)
```