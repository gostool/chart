## rc
* 创建rc

k8s权威指南第四版 第一章

删除
```
kubectl delete -n default replicationcontroller redis-slave
```

## redis-master

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


## redis-slave

```
➜  k8s git:(dev) kubectl apply -f rc/redis-slave-controller.yaml
replicationcontroller/redis-slave created
➜  k8s git:(dev) kubectl get rc -l "app=redis-slave"
NAME          DESIRED   CURRENT   READY   AGE
redis-slave   2         2         2       27s
➜  k8s git:(dev) kubectl get pod -l "app=redis-slave"
NAME                READY   STATUS    RESTARTS   AGE
redis-slave-5km7z   1/1     Running   0          39s
redis-slave-bntrl   1/1     Running   0          39s
➜  k8s git:(dev)
```

问题： redis-slave 如何找到redis-master

```
root@redis-slave-5km7z:/data# redis-server -h
Usage: ./redis-server [/path/to/redis.conf] [options]
       ./redis-server - (read config from stdin)
       ./redis-server -v or --version
       ./redis-server -h or --help
       ./redis-server --test-memory <megabytes>

Examples:
       ./redis-server (run the server with default conf)
       ./redis-server /etc/redis/6379.conf
       ./redis-server --port 7777
       ./redis-server --port 7777 --slaveof 127.0.0.1 8888
       ./redis-server /etc/myredis.conf --loglevel verbose

Sentinel mode:
       ./redis-server /etc/sentinel.conf --sentinel
```

使用已知redis-service ip:
```
root@redis-slave-7b99r:/opt# curl -v 10.99.241.216:6379
* About to connect() to 10.99.241.216 port 6379 (#0)
*   Trying 10.99.241.216...
* connected
* Connected to 10.99.241.216 (10.99.241.216) port 6379 (#0)
> GET / HTTP/1.1
> User-Agent: curl/7.26.0
> Host: 10.99.241.216:6379
> Accept: */*
> 
root@redis-slave-5km7z:/data# redis-server --port 26379 --slaveof 10.99.241.216  6379
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 3.0.3 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                   
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 26379
 |    `-._   `._    /     _.-'    |     PID: 42
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           http://redis.io        
  `-._    `-._`-.__.-'_.-'    _.-'                                   

```

使用env:
```
root@redis-slave-5km7z:/data# env
DEIS_WORKFLOW_SERVICE_HOST=10.99.59.176
HOSTNAME=redis-slave-5km7z
REDIS_DOWNLOAD_URL=http://download.redis.io/releases/redis-3.0.3.tar.gz
KUBERNETES_PORT_443_TCP_PORT=443
KUBERNETES_PORT=tcp://10.96.0.1:443
TERM=xterm
DEIS_WORKFLOW_PORT_80_TCP_PORT=80
KUBERNETES_SERVICE_PORT=443
KUBERNETES_SERVICE_HOST=10.96.0.1
DEIS_WORKFLOW_PORT_80_TCP=tcp://10.99.59.176:80
GET_HOSTS_FROM=env
REDIS_MASTER_PORT_6379_TCP_ADDR=10.99.241.216
DEIS_WORKFLOW_PORT_80_TCP_ADDR=10.99.59.176
REDIS_MASTER_PORT_6379_TCP=tcp://10.99.241.216:6379
DEIS_WORKFLOW_PORT=tcp://10.99.59.176:80
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
REDIS_MASTER_SERVICE_PORT=6379
PWD=/data
DEIS_WORKFLOW_SERVICE_PORT_HTTP=80
REDIS_MASTER_SERVICE_HOST=10.99.241.216
SHLVL=1
HOME=/root
KUBERNETES_PORT_443_TCP_PROTO=tcp
REDIS_DOWNLOAD_SHA1=0e2d7707327986ae652df717059354b358b83358
REDIS_VERSION=3.0.3
KUBERNETES_SERVICE_PORT_HTTPS=443
REDIS_MASTER_PORT_6379_TCP_PORT=6379
REDIS_MASTER_PORT_6379_TCP_PROTO=tcp
REDIS_MASTER_PORT=tcp://10.99.241.216:6379
DEIS_WORKFLOW_PORT_80_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
DEIS_WORKFLOW_SERVICE_PORT=80
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
_=/usr/bin/env
root@redis-slave-5km7z:/data# redis-server --port 26379 --slaveof ${REDIS_MASTER_SERVICE_HOST}  ${REDIS_MASTER_SERVICE_PORT}
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 3.0.3 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                   
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 26379
 |    `-._   `._    /     _.-'    |     PID: 47
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           http://redis.io        
  `-._    `-._`-.__.-'_.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |                                  
  `-._    `-._`-.__.-'_.-'    _.-'                                   
      `-._    `-.__.-'    _.-'                                       
          `-._        _.-'                                           
              `-.__.-'                                               

47:S 13 Oct 03:03:57.224 # Server started, Redis version 3.0.3
47:S 13 Oct 03:03:57.224 # WARNING you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled.
47:S 13 Oct 03:03:57.224 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
47:S 13 Oct 03:03:57.224 * DB loaded from disk: 0.000 seconds
47:S 13 Oct 03:03:57.224 * The server is now ready to accept connections on port 26379
47:S 13 Oct 03:03:57.225 * Connecting to MASTER 10.99.241.216:6379
47:S 13 Oct 03:03:57.225 * MASTER <-> SLAVE sync started
47:S 13 Oct 03:03:57.225 * Non blocking connect for SYNC fired the event.
47:S 13 Oct 03:03:57.226 * Master replied to PING, replication can continue...
47:S 13 Oct 03:03:57.226 * Partial resynchronization not possible (no cached master)
47:S 13 Oct 03:03:57.227 * Full resync from master: da321ac143bd618b21ac1bd25ede1cd4ced7f393:841
47:S 13 Oct 03:03:57.247 * MASTER <-> SLAVE sync: receiving 43 bytes from master
47:S 13 Oct 03:03:57.248 * MASTER <-> SLAVE sync: Flushing old data
47:S 13 Oct 03:03:57.248 * MASTER <-> SLAVE sync: Loading DB in memory
47:S 13 Oct 03:03:57.249 * MASTER <-> SLAVE sync: Finished with success

```

php-front:
```
➜  k8s git:(dev) kubectl apply -f rc/redis-master-controller.yaml
replicationcontroller/redis-master created
➜  k8s git:(dev) kubectl apply -f rc/redis-slave-controller.yaml
replicationcontroller/redis-slave created
➜  k8s git:(dev) kubectl apply -f rc/frontend-controller.yaml
replicationcontroller/frontend created
➜  k8s git:(dev) kubectl get rc -o wide
NAME           DESIRED   CURRENT   READY   AGE   CONTAINERS   IMAGES                             SELECTOR
frontend       3         3         1       8s    frontend     kubeguide/guestbook-php-frontend   app=frontend
redis-master   1         1         1       35s   master       kubeguide/redis-master             app=redis-master
redis-slave    2         2         2       25s   slave        kubeguide/guestbook-redis-slave    app=redis-slave
➜  k8s git:(dev)
```

```
php:      app1,      app2,       app3
          |         /     \        |  
          |        /       \       |
db:
        write                     read
          |                         |
          |               sync      |
       redis-master      -->     redis-slave1 redis-slave2
```创建php front:
```
➜  k8s git:(dev) kubectl apply -f rc/frontend-controller.yaml -n php
replicationcontroller/frontend created
```

检查redis主从，php状态
```
➜  k8s git:(dev) kubectl get rc -n php
NAME           DESIRED   CURRENT   READY   AGE
frontend       3         3         0       6s
redis-master   1         1         1       3m5s
redis-slave    2         2         2       93s
➜  k8s git:(dev)
```


访问:
```
export POD_NAME=$(kubectl get pods --namespace default -l "app=frontend" -o jsonpath="{.items[0].metadata.name}")
kubectl --namespace default  port-forward --address 0.0.0.0 ${POD_NAME}  8080:80
```


