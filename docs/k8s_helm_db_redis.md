## helm redis
* 添加仓库
* install

```
ubuntu@VM-4-8-ubuntu:~/apps/k8s/redis$ helm repo add bitnami https://charts.bitnami.com/bitnami
ubuntu@VM-4-8-ubuntu:~/apps/k8s/redis$ helm search repo bitnami/redis
NAME                 	CHART VERSION	APP VERSION	DESCRIPTION
bitnami/redis        	15.3.2       	6.2.5      	Open source, advanced key-value store. It is of...
bitnami/redis-cluster	6.3.6        	6.2.5      	Open source, advanced key-value store. It is of...
ubuntu@VM-4-8-ubuntu:~/apps/k8s/redis$
```

### install

```
ubuntu@VM-4-8-ubuntu:~/apps/k8s/redis$ helm install redis1 bitnami/redis -n db
NAME: redis1
LAST DEPLOYED: Wed Sep 15 15:56:14 2021
NAMESPACE: db
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
** Please be patient while the chart is being deployed **

Redis&trade; can be accessed on the following DNS names from within your cluster:

    redis1-master.db.svc.cluster.local for read/write operations (port 6379)
    redis1-replicas.db.svc.cluster.local for read-only operations (port 6379)



To get your password run:

    export REDIS_PASSWORD=$(kubectl get secret --namespace db redis1 -o jsonpath="{.data.redis-password}" | base64 --decode)

To connect to your Redis&trade; server:

1. Run a Redis&trade; pod that you can use as a client:

   kubectl run --namespace db redis-client --restart='Never'  --env REDIS_PASSWORD=$REDIS_PASSWORD  --image docker.io/bitnami/redis:6.2.5-debian-10-r34 --command -- sleep infinity

   Use the following command to attach to the pod:

   kubectl exec --tty -i redis-client \
   --namespace db -- bash

2. Connect using the Redis&trade; CLI:
   redis-cli -h redis1-master -a $REDIS_PASSWORD
   redis-cli -h redis1-replicas -a $REDIS_PASSWORD

To connect to your database from outside the cluster execute the following commands:

    kubectl port-forward --namespace db svc/redis1-master 6379:6379 &
    redis-cli -h 127.0.0.1 -p 6379 -a $REDIS_PASSWORD
ubuntu@VM-4-8-ubuntu:~/apps/k8s/redis$
```

查看pod, service
```
ubuntu@VM-4-8-ubuntu:~/apps/k8s/redis$ kubectl get pod,service -n db -o wide
NAME                    READY   STATUS    RESTARTS   AGE     IP            NODE       NOMINATED NODE   READINESS GATES
pod/redis1-master-0     1/1     Running   0          4m16s   172.17.0.9    minikube   <none>           <none>
pod/redis1-replicas-0   1/1     Running   0          4m16s   172.17.0.10   minikube   <none>           <none>
pod/redis1-replicas-1   1/1     Running   0          3m18s   172.17.0.11   minikube   <none>           <none>
pod/redis1-replicas-2   1/1     Running   0          2m52s   172.17.0.12   minikube   <none>           <none>

NAME                      TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE     SELECTOR
service/redis1-headless   ClusterIP   None             <none>        6379/TCP   4m17s   app.kubernetes.io/instance=redis1,app.kubernetes.io/name=redis
service/redis1-master     ClusterIP   10.107.214.190   <none>        6379/TCP   4m17s   app.kubernetes.io/component=master,app.kubernetes.io/instance=redis1,app.kubernetes.io/name=redis
service/redis1-replicas   ClusterIP   10.103.178.254   <none>        6379/TCP   4m17s   app.kubernetes.io/component=replica,app.kubernetes.io/instance=redis1,app.kubernetes.io/name=redis
ubuntu@VM-4-8-ubuntu:~/apps/k8s/redis$
```

```
ubuntu@VM-4-8-ubuntu:~/apps/k8s/redis$ helm list -n db
NAME  	NAMESPACE	REVISION	UPDATED                               	STATUS  	CHART       	APP VERSION
redis1	db       	1       	2021-09-15 15:56:14.62387165 +0800 CST	deployed	redis-15.3.2	6.2.5
ubuntu@VM-4-8-ubuntu:~/apps/k8s/redis$
```

## 访问redis 
参考提示. kubectl 启动一个redis-client

在master节点写入数据.在replicas节点读取数据.
```
ubuntu@VM-4-8-ubuntu:~/apps/k8s/redis$ kubectl run --namespace db redis-client --restart='Never'  --env REDIS_PASSWORD=$REDIS_PASSWORD  --image docker.io/bitnami/redis:6.2.5-debian-10-r34 --command -- sleep infinity
pod/redis-client created
ubuntu@VM-4-8-ubuntu:~/apps/k8s/redis$ kubectl get po -n db
NAME                READY   STATUS    RESTARTS   AGE
redis-client        1/1     Running   0          13s
redis1-master-0     1/1     Running   0          8m12s
redis1-replicas-0   1/1     Running   0          8m12s
redis1-replicas-1   1/1     Running   0          7m14s
redis1-replicas-2   1/1     Running   0          6m48s
ubuntu@VM-4-8-ubuntu:~/apps/k8s/redis$ kubectl exec --tty -i redis-client \
>    --namespace db -- bash
I have no name!@redis-client:/$
I have no name!@redis-client:/$ redis-cli -h redis1-master -a $REDIS_PASSWORD
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
redis1-master:6379> set a 1
OK
redis1-master:6379> get a
"1"
redis1-master:6379>
redis1-master:6379> exit
I have no name!@redis-client:/$ redis-cli -h redis1-replicas -a $REDIS_PASSWORD
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
redis1-replicas:6379> get a
"1"
redis1-replicas:6379>
```

### dashboard
通过dashboard 查看redis-service
![service](https://oscimg.oschina.net/oscnet/up-f48b626814823b4ca6c74a03c76b1bc17ff.png)

exec:

![](https://oscimg.oschina.net/oscnet/up-119a4ea6deed54f340082b126bbe323bf7d.png)

测试redis master/replicas:

![](https://oscimg.oschina.net/oscnet/up-f71d70fcd00a805ff39505c93a38524ac69.png)


### 删除
* helm delete
* dashboard

```
ubuntu@VM-4-8-ubuntu:~/apps/chart$ helm list -n db
NAME  	NAMESPACE	REVISION	UPDATED                                	STATUS  	CHART       	APP VERSION
redis1	db       	1       	2021-09-15 16:45:21.099117013 +0800 CST	deployed	redis-15.3.2	6.2.5
ubuntu@VM-4-8-ubuntu:~/apps/chart$ helm delete redis1 -n db
release "redis1" uninstalled
ubuntu@VM-4-8-ubuntu:~/apps/chart$ helm list -n db
NAME	NAMESPACE	REVISION	UPDATED	STATUS	CHART	APP VERSION
ubuntu@VM-4-8-ubuntu:~/apps/chart$ kubectl get po,service -n db
NAME               READY   STATUS    RESTARTS   AGE
pod/redis-client   1/1     Running   0          6m54s
ubuntu@VM-4-8-ubuntu:~/apps/chart$
```
redis-client 是使用kubectl run 启动的pod.直接在dashboard删除.