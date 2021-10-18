## nginx
[参考](https://shanyue.tech/k8s/pod.html#pod)
* 部署nginx pod
* 访问nginx pod
* deployment. (3个nginx pod)
* service. (服务托管-3个nginx)
* ingress. (外网访问)

## pod
nginx.yaml
```yml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  # 指定 label，便于检索
  labels:
    app: nginx
spec:
  containers:
  - name: nginx
    # 指定镜像
    image: nginx:alpine
    # 指定暴露端口
    ports:
    - containerPort: 80
```

### 部署nginx pod
使用 kubectly apply，部署 Pod
```
ubuntu@VM-4-8-ubuntu:~/apps/k8s$ kubectl apply -f nginx.yaml
pod/nginx created
```

校验部署状态，此时 STATUS 为 Running 表明部署成功
```
ubuntu@VM-4-8-ubuntu:~/apps/k8s$ kubectl get pods nginx -o wide
NAME    READY   STATUS    RESTARTS   AGE    IP           NODE       NOMINATED NODE   READINESS GATES
nginx   1/1     Running   0          108s   172.17.0.5   minikube   <none>           <none>
ubuntu@VM-4-8-ubuntu:~/apps/k8s$
```

获取更加详细的信息
```
ubuntu@VM-4-8-ubuntu:~/apps/k8s$ kubectl describe pod nginx
Name:         nginx
Namespace:    default
Priority:     0
Node:         minikube/192.168.49.2
Start Time:   Tue, 14 Sep 2021 14:46:54 +0800
Labels:       app=nginx
Annotations:  <none>
Status:       Running
IP:           172.17.0.5
IPs:
  IP:  172.17.0.5
Containers:
  nginx:
    Container ID:   docker://a60246e246eb9fb637731b65ae255e0a4a66bd69d8852c8bb2b40f2210060044
    Image:          nginx:alpine
    Image ID:       docker-pullable://nginx@sha256:686aac2769fd6e7bab67663fd38750c135b72d993d0bb0a942ab02ef647fc9c3
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Tue, 14 Sep 2021 14:47:06 +0800
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
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  2m30s  default-scheduler  Successfully assigned default/nginx to minikube
  Normal  Pulling    2m29s  kubelet            Pulling image "nginx:alpine"
  Normal  Pulled     2m19s  kubelet            Successfully pulled image "nginx:alpine" in 10.442083898s
  Normal  Created    2m19s  kubelet            Created container nginx
  Normal  Started    2m18s  kubelet            Started container nginx
ubuntu@VM-4-8-ubuntu:~/apps/k8s$
```

查看pod nginx. 
```
ubuntu@VM-4-8-ubuntu:~/apps/k8s$ kubectl get po,service -A
NAMESPACE              NAME                                             READY   STATUS    RESTARTS   AGE
default                pod/nginx                                        1/1     Running   0          3m52s
kube-system            pod/coredns-54d67798b7-vvqlm                     1/1     Running   0          3d15h
kube-system            pod/etcd-minikube                                1/1     Running   0          3d15h
kube-system            pod/kube-apiserver-minikube                      1/1     Running   0          3d15h
kube-system            pod/kube-controller-manager-minikube             1/1     Running   0          3d15h
kube-system            pod/kube-proxy-5hx2x                             1/1     Running   0          3d15h
kube-system            pod/kube-scheduler-minikube                      1/1     Running   0          3d15h
kube-system            pod/storage-provisioner                          1/1     Running   0          3d15h
kubernetes-dashboard   pod/dashboard-metrics-scraper-7886f6d855-w46vw   1/1     Running   0          3d15h
kubernetes-dashboard   pod/kubernetes-dashboard-66f6c8f7c5-hj59l        1/1     Running   0          3d15h

NAMESPACE              NAME                                TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                  AGE
default                service/kubernetes                  ClusterIP   10.96.0.1       <none>        443/TCP                  3d15h
kube-system            service/kube-dns                    ClusterIP   10.96.0.10      <none>        53/UDP,53/TCP,9153/TCP   3d15h
kubernetes-dashboard   service/dashboard-metrics-scraper   ClusterIP   10.103.45.85    <none>        8000/TCP                 3d15h
kubernetes-dashboard   service/kubernetes-dashboard        ClusterIP   10.98.102.237   <none>        80/TCP                   3d15h
```

### 访问nginx pod

登陆到ssh 访问nginx pod.
```
ubuntu@VM-4-8-ubuntu:~/apps/k8s$ minikube ssh
docker@minikube:~$ curl -v 172.17.0.5
*   Trying 172.17.0.5:80...
* TCP_NODELAY set
* Connected to 172.17.0.5 (172.17.0.5) port 80 (#0)
> GET / HTTP/1.1
> Host: 172.17.0.5
> User-Agent: curl/7.68.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: nginx/1.21.3
< Date: Tue, 14 Sep 2021 06:51:24 GMT
< Content-Type: text/html
< Content-Length: 615
< Last-Modified: Tue, 07 Sep 2021 15:50:58 GMT
< Connection: keep-alive
< ETag: "61378a62-267"
< Accept-Ranges: bytes
<
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
* Connection #0 to host 172.17.0.5 left intact
docker@minikube:~$
```
### 进入nginx pod

此时我们可以使用 kubectl exec 进入 Pod 的内部容器。如果 Pod 中有多个容器使用 kubectl exec -c 指定容器

```
ubuntu@VM-4-8-ubuntu:~/apps/k8s$ kubectl exec -it nginx sh
kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
/ # ps -ef | grep nginx
    1 root      0:00 nginx: master process nginx -g daemon off;
   32 nginx     0:00 nginx: worker process
   33 nginx     0:00 nginx: worker process
   45 root      0:00 grep nginx
/ # netstat -tan
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN
tcp        0      0 :::80                   :::*                    LISTEN
/ # wget -q -O - localhost
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

## Deployment
在k8s中管理 Pod 的称作 Controller，我们可以使用 Deployment 这种 Controller 来为 Pod 进行扩容，当然它还可以滚动升级，回滚，金丝雀等等关于部署的事情

我们编写一个 Deployment 的资源配置文件
* spec.template: 指定要部署的 Pod
* spec.replicas: 指定要部署的个数
* spec.selector: 定位需要管理的 Pod

```yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 3
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        ports:
        - containerPort: 80
```

nginx-deployment 部署的三个 pod 全部成功
```shell
ubuntu@VM-4-8-ubuntu:~/apps/k8s$ kubectl get pods -o wide -l 'app=nginx'
NAME                                READY   STATUS    RESTARTS   AGE   IP           NODE       NOMINATED NODE   READINESS GATES
nginx-deployment-7fb7fd49b4-7dm5w   1/1     Running   0          19m   172.17.0.6   minikube   <none>           <none>
nginx-deployment-7fb7fd49b4-h8ds7   1/1     Running   0          19m   172.17.0.8   minikube   <none>           <none>
nginx-deployment-7fb7fd49b4-v9xpn   1/1     Running   0          19m   172.17.0.7   minikube   <none>           <none>
ubuntu@VM-4-8-ubuntu:~/apps/k8s$ kubectl get deploy nginx-deployment
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   3/3     3            3           20m
ubuntu@VM-4-8-ubuntu:~/apps/k8s$
```

## Service
[原文](https://shanyue.tech/k8s/pod.html#deployment)
现在我们已经部署了一个 Deployment，其中有三个 Pod，就有三个 IP，那我们如何向这三个 Pod 请求服务呢，何况每当上线部署后，就会产生新的 Pod IP。即我们如何做服务发现

我们可以通过 Service 解决这个问题，做指定 Deployment 或者特定集合 Pod 的网络层抽象
配置文件如下

* spec.selector: 指定如何选择 Pod
* spec.ports: 指定如何暴露端口

nginx-service.yaml
```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
```

部署nginx service.

```
ubuntu@VM-4-8-ubuntu:~/apps/k8s$ kubectl apply -f nginx_service.yaml
service/nginx-service created
ubuntu@VM-4-8-ubuntu:~/apps/k8s$ kubectl get svc nginx-service -o wide
NAME            TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE   SELECTOR
nginx-service   ClusterIP   10.111.152.184   <none>        80/TCP    8s    app=nginx
ubuntu@VM-4-8-ubuntu:~/apps/k8s$
```

再集群中访问:
```
ubuntu@VM-4-8-ubuntu:~/apps/k8s$ minikube ssh
docker@minikube:~$ curl -v 10.111.152.184
*   Trying 10.111.152.184:80...
* TCP_NODELAY set
* Connected to 10.111.152.184 (10.111.152.184) port 80 (#0)
> GET / HTTP/1.1
> Host: 10.111.152.184
> User-Agent: curl/7.68.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: nginx/1.21.3
< Date: Tue, 14 Sep 2021 07:35:09 GMT
< Content-Type: text/html
< Content-Length: 615
< Last-Modified: Tue, 07 Sep 2021 15:50:58 GMT
< Connection: keep-alive
< ETag: "61378a62-267"
< Accept-Ranges: bytes
<
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
* Connection #0 to host 10.111.152.184 left intact
docker@minikube:~$
```


通过配置 Deployment 与 Service ，此时我们可以在集群中通过服务发现访问域名

## ingress
[官方-minikube-ingress](https://kubernetes.io/zh/docs/tasks/access-application-cluster/ingress-minikube/)
[官方](https://kubernetes.io/zh/docs/concepts/services-networking/ingress/)
[原文](https://shanyue.tech/k8s/ingress.html#%E4%BD%BF%E7%94%A8-helm-%E9%83%A8%E7%BD%B2-nginx-ingress-controller)

[nginx-ingress](https://github.com/helm/charts/tree/master/stable/nginx-ingress)

nginx-ingress 会配置一个 type 为 LoadBalancer 的 service， 
因此需要配置 EXTERNAL-IP 为k8s集群节点的 IP。 在这里 external-ip 会设置为 [192.168.49.2 ]
我们可以通过 kubectl get nodes 来获取 IP 地址

```
ubuntu@VM-4-8-ubuntu:~/apps/k8s$ kubectl get nodes -o wide
NAME       STATUS   ROLES                  AGE     VERSION   INTERNAL-IP    EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION       CONTAINER-RUNTIME
minikube   Ready    control-plane,master   3d16h   v1.20.2   192.168.49.2   <none>        Ubuntu 20.04.2 LTS   4.15.0-142-generic   docker://20.10.6
ubuntu@VM-4-8-ubuntu:~/apps/k8s$
```


使用 helm v3 部署，如果使用 helm v2 部署的话，把 release-name 使用 --name 指定

```
$ helm install nginx-ingress stable/nginx-ingress --set "controller.service.externalIPs[0]=192.168.49.2"
NAME: nginx-ingress
LAST DEPLOYED: 2019-10-18 21:21:44.115902395 +0800 CST m=+1.904554085
NAMESPACE: default
STATUS: deployed
NOTES:
The nginx-ingress controller has been installed.
It may take a few minutes for the LoadBalancer IP to be available.
You can watch the status by running 'kubectl --namespace default get services -o wide -w nginx-ingress-controller'

An example Ingress that makes use of the controller:

  apiVersion: extensions/v1beta1
  kind: Ingress
  metadata:
    annotations:
      kubernetes.io/ingress.class: nginx
    name: example
    namespace: foo
  spec:
    rules:
      - host: www.example.com
        http:
          paths:
            - backend:
                serviceName: exampleService
                servicePort: 80
              path: /
    # This section is only required if TLS is to be enabled for the Ingress
    tls:
        - hosts:
            - www.example.com
          secretName: example-tls

If TLS is enabled for the Ingress, a Secret containing the certificate and key must also be provided:

  apiVersion: v1
  kind: Secret
  metadata:
    name: example-tls
    namespace: foo
  data:
    tls.crt: <base64 encoded cert>
    tls.key: <base64 encoded key>
  type: kubernetes.io/tls
```




### 

```
ubuntu@VM-4-8-ubuntu:~/apps/k8s$ kubectl get service -A
NAMESPACE              NAME                                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
default                kubernetes                           ClusterIP   10.96.0.1        <none>        443/TCP                      3d17h
default                nginx-service                        ClusterIP   10.111.152.184   <none>        80/TCP                       61m
ingress-nginx          ingress-nginx-controller             NodePort    10.104.92.209    <none>        80:30119/TCP,443:30113/TCP   8m4s
ingress-nginx          ingress-nginx-controller-admission   ClusterIP   10.106.48.101    <none>        443/TCP                      8m4s
kube-system            kube-dns                             ClusterIP   10.96.0.10       <none>        53/UDP,53/TCP,9153/TCP       3d17h
kubernetes-dashboard   dashboard-metrics-scraper            ClusterIP   10.103.45.85     <none>        8000/TCP                     3d16h
kubernetes-dashboard   kubernetes-dashboard                 ClusterIP   10.98.102.237    <none>        80/TCP                       3d16h
```
NodePort 访问
```
ubuntu@VM-4-8-ubuntu:~/apps/k8s$ minikube service ingress-nginx-controller -n ingress-nginx  --url
http://192.168.49.2:30119
http://192.168.49.2:30113
ubuntu@VM-4-8-ubuntu:~/apps/k8s$ curl -v http://192.168.49.2:30113
* Rebuilt URL to: http://192.168.49.2:30113/
*   Trying 192.168.49.2...
* TCP_NODELAY set
* Connected to 192.168.49.2 (192.168.49.2) port 30113 (#0)
> GET / HTTP/1.1
> Host: 192.168.49.2:30113
> User-Agent: curl/7.58.0
> Accept: */*
>
< HTTP/1.1 400 Bad Request
< Date: Tue, 14 Sep 2021 08:36:08 GMT
< Content-Type: text/html
< Content-Length: 248
< Connection: close
<
<html>
<head><title>400 The plain HTTP request was sent to HTTPS port</title></head>
<body>
<center><h1>400 Bad Request</h1></center>
<center>The plain HTTP request was sent to HTTPS port</center>
<hr><center>nginx</center>
</body>
</html>
* Closing connection 0
ubuntu@VM-4-8-ubuntu:~/apps/k8s$
```

### 
将 Deployment 暴露出来：
[](https://kubernetes.io/zh/docs/tasks/access-application-cluster/ingress-minikube/)
```
ubuntu@VM-4-8-ubuntu:~/apps/k8s$ cat nginx_deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 3
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        ports:
        - containerPort: 80
ubuntu@VM-4-8-ubuntu:~/apps/k8s$ kubectl get deployment
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   2/2     2            2           97m
ubuntu@VM-4-8-ubuntu:~/apps/k8s$ kubectl expose deployment nginx-deployment --port=80 --type=NodePort
service/nginx-deployment exposed
ubuntu@VM-4-8-ubuntu:~/apps/k8s$ kubectl get service
NAME               TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
kubernetes         ClusterIP   10.96.0.1       <none>        443/TCP        3d17h
nginx-deployment   NodePort    10.105.168.67   <none>        80:30694/TCP   4s
ubuntu@VM-4-8-ubuntu:~/apps/k8s$
ubuntu@VM-4-8-ubuntu:~/apps/k8s$ minikube service nginx-deployment --url
http://192.168.49.2:30694
ubuntu@VM-4-8-ubuntu:~/apps/k8s$
```
在本机上访问:
```
ubuntu@VM-4-8-ubuntu:~/apps/k8s$ curl -v http://192.168.49.2:30694/
*   Trying 192.168.49.2...
* TCP_NODELAY set
* Connected to 192.168.49.2 (192.168.49.2) port 30694 (#0)
> GET / HTTP/1.1
> Host: 192.168.49.2:30694
> User-Agent: curl/7.58.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Server: nginx/1.21.3
< Date: Tue, 14 Sep 2021 08:42:52 GMT
< Content-Type: text/html
< Content-Length: 615
< Last-Modified: Tue, 07 Sep 2021 15:50:58 GMT
< Connection: keep-alive
< ETag: "61378a62-267"
< Accept-Ranges: bytes
<
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
* Connection #0 to host 192.168.49.2 left intact
ubuntu@VM-4-8-ubuntu:~/apps/k8s$
```

![访问nginx](https://oscimg.oschina.net/oscnet/up-5cc5610d47e76371fea22d88799c5391cf4.png)