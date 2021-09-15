## port-forward 模式访问

* 安装deis-workflow 
* 在k8s集群外访问
* 在公网访问.(防火墙开启)

install:
```
ubuntu@VM-4-8-ubuntu:~/apps/chart$ helm install deis-workflow ./deis-workflow-0.1.0.tgz
NAME: deis-workflow
LAST DEPLOYED: Wed Sep 15 18:24:02 2021
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=deis-workflow,app.kubernetes.io/instance=deis-workflow" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
ubuntu@VM-4-8-ubuntu:~/apps/chart$ export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=deis-workflow,app.kubernetes.io/instance=deis-workflow" -o jsonpath="{.items[0].metadata.name}")
ubuntu@VM-4-8-ubuntu:~/apps/chart$  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
ubuntu@VM-4-8-ubuntu:~/apps/chart$  echo "Visit http://127.0.0.1:8080 to use your application"
Visit http://127.0.0.1:8080 to use your application
```
port-forward模式访问:
```
ubuntu@VM-4-8-ubuntu:~/apps/chart$  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
Forwarding from 127.0.0.1:8080 -> 80
Forwarding from [::1]:8080 -> 80
debug2: client_check_window_change: changed
debug2: channel 0: request window-change confirm 0
debug2: client_check_window_change: changed
debug2: channel 0: request window-change confirm 0
Handling connection for 8080
Handling connection for 8080
```

在宿主机本身访问:
```
ubuntu@VM-4-8-ubuntu:~$ curl -v localhost:8080/index.html
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 8080 (#0)
> GET /index.html HTTP/1.1
> Host: localhost:8080
> User-Agent: curl/7.58.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Server: nginx/1.16.0
< Date: Wed, 15 Sep 2021 10:36:02 GMT
< Content-Type: text/html
< Content-Length: 612
< Last-Modified: Tue, 23 Apr 2019 10:18:21 GMT
< Connection: keep-alive
< ETag: "5cbee66d-264"
< Accept-Ranges: bytes
<
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
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
* Connection #0 to host localhost left intact
ubuntu@VM-4-8-ubuntu:~$
```


在公网访问:
```
kubectl --namespace default port-forward --address 0.0.0.0 $POD_NAME  8080:$CONTAINER_PORT
```