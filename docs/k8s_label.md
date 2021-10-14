## Label(标签)
[label对象](https://kubernetes.io/zh/docs/concepts/overview/working-with-objects/labels/)

Label以key/val键值对的形式附加到各种对象(Pod, Service, RC, Node)。

### 形式
* 等值
* 不包含
* 集合

```
"app=nginx"
"env!=production"
"name in (redis-master, redis-slave)"
```

## 示范
* pod/label.yaml
* pod/redis-master.yaml
* pod/redis-slave.yaml

pod:
* mylabel
* redis-master-fzp74
* redis-slave-b6wpq

### 查看三个pod的标签:
```
➜  k8s git:(dev) kubectl describe pod mylabel
Name:         mylabel
Namespace:    default
Priority:     0
Node:         minikube/192.168.49.2
Start Time:   Thu, 14 Oct 2021 14:56:49 +0800
Labels:       env=test
              name=mylabel
              role=test
Annotations:  <none>
....
➜  k8s git:(dev) kubectl describe pod redis-master-fzp74
Name:         redis-master-fzp74
Namespace:    default
Priority:     0
Node:         minikube/192.168.49.2
Start Time:   Wed, 13 Oct 2021 15:27:12 +0800
Labels:       app=redis-master
Annotations:  <none>
➜  k8s git:(dev) kubectl describe pod redis-slave-b6wpq
Name:         redis-slave-b6wpq
Namespace:    default
Priority:     0
Node:         minikube/192.168.49.2
Start Time:   Wed, 13 Oct 2021 15:28:29 +0800
Labels:       app=redis-slave
```


### 使用label 获取pod
* 等于
* 不等于
* in
* 多个匹配. (todo)

```
➜  k8s git:(dev) kubectl get pod -l "name=mylabel"
NAME      READY   STATUS    RESTARTS   AGE
mylabel   1/1     Running   0          7m37s
➜  k8s git:(dev) kubectl get pod -l "name!=mylabel"
NAME                             READY   STATUS    RESTARTS   AGE
deis-workflow-584dcf6dc7-wxqj6   1/1     Running   0          28d
frontend-m5ch7                   1/1     Running   0          23h
frontend-ntxsw                   1/1     Running   0          23h
frontend-tcrr5                   1/1     Running   0          23h
myapp-758c55b554-8h4d6           1/1     Running   0          44h
myapp-758c55b554-mn6vr           1/1     Running   0          44h
myapp-758c55b554-ts6lb           1/1     Running   0          44h
nginx                            1/1     Running   0          43h
redis-master-fzp74               1/1     Running   0          23h
redis-slave-b6wpq                1/1     Running   0          23h
redis-slave-wh4ps                1/1     Running   0          23h
➜  k8s git:(dev) kubectl get pod -l "app in (redis-master, redis-slave)"
NAME                 READY   STATUS    RESTARTS   AGE
redis-master-fzp74   1/1     Running   0          23h
redis-slave-b6wpq    1/1     Running   0          23h
redis-slave-wh4ps    1/1     Running   0          23h
➜  k8s git:(dev)
```

