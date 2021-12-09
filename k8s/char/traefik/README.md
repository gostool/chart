# Traefik

[Traefik](https://traefik.io/) is a modern HTTP reverse proxy and load balancer made to deploy
microservices with ease.

## Introduction

This chart bootstraps Traefik version 2 as a Kubernetes ingress controller,
using Custom Resources `IngressRoute`: <https://docs.traefik.io/providers/kubernetes-crd/>.

### Philosophy

The Traefik HelmChart is focused on Traefik deployment configuration.

To keep this HelmChart as generic as possible we tend
to avoid integrating any third party solutions nor any specific use cases.

Accordingly, the encouraged approach to fulfill your needs:
1. override the default Traefik configuration values ([yaml file or cli](https://helm.sh/docs/chart_template_guide/values_files/))
2. append your own configurations (`kubectl apply -f myconf.yaml`)
3. extend this HelmChart ([as a Subchart](https://helm.sh/docs/chart_template_guide/subcharts_and_globals/))

## Installing

### Prerequisites

With the command `helm version`, make sure that you have:
- Helm v3 [installed](https://helm.sh/docs/using_helm/#installing-helm)

Add Traefik's chart repository to Helm:

```bash
helm repo add traefik https://helm.traefik.io/traefik
```

You can update the chart repository by running:

```bash
helm repo update
```

### Kubernetes Version Support

Due to changes in CRD version support, the following versions of the chart are usable and supported on the following kubernetes versions:

|                         |  Kubernetes v1.15 and below | Kubernetes v1.16-v1.21 | Kubernetes v1.22 and above |
|-------------------------|-----------------------------|------------------------|----------------------------|
| Chart v9.20.2 and below | [x]                         | [x]                    |                            |
| Chart 10.0.0 and above  |                             | [x]                    | [x]                        |

### Deploying Traefik

```bash
helm install traefik traefik/traefik
```

#### Warning

Helm v2 support was removed in the chart version 10.0.0.

### Exposing the Traefik dashboard

This HelmChart does not expose the Traefik dashboard by default, for security concerns.
Thus, there are multiple ways to expose the dashboard.
For instance, the dashboard access could be achieved through a port-forward :

```
kubectl port-forward $(kubectl get pods --selector "app.kubernetes.io/name=traefik" --output=name) 9000:9000
```

Another way would be to apply your own configuration, for instance,
by defining and applying an IngressRoute CRD (`kubectl apply -f dashboard.yaml`):

```yaml
# dashboard.yaml
apiVersion: traefik.containo.us/v1alpha1
kind: IngressRoute
metadata:
  name: dashboard
spec:
  entryPoints:
    - web
  routes:
    - match: Host(`traefik.localhost`) && (PathPrefix(`/dashboard`) || PathPrefix(`/api`))
      kind: Rule
      services:
        - name: api@internal
          kind: TraefikService
```

## Contributing

If you want to contribute to this chart, please read the [Contributing Guide](../CONTRIBUTING.md).


## 实践记录

[教程](https://network.51cto.com/art/202111/689466.htm)

### 1.获取chart 10.6.0 版本
```
helm pull traefik/traefik  --version 10.6.0 --untar
```

### 2.helm install
```
(venv) ➜  char git:(dev) helm install traefik traefik/ -n traefik-ingress -f traefik/my-value.yaml
NAME: traefik
LAST DEPLOYED: Thu Dec  9 10:54:31 2021
NAMESPACE: traefik-ingress
STATUS: deployed
REVISION: 1
TEST SUITE: None
(venv) ➜  char git:(dev) helm ls
NAME	NAMESPACE	REVISION	UPDATED	STATUS	CHART	APP VERSION
```

### 3.查看svc和其他组件
svc:
* dashboard: ip:9000 -> 公网ip:30466
* 80:                   公网ip:30525
* 443:                  公网ip:30758


```
(venv) ➜  char git:(dev) kubectl get all -n traefik-ingress -o wide
NAME                           READY   STATUS              RESTARTS   AGE   IP       NODE       NOMINATED NODE   READINESS GATES
pod/traefik-5bd4d8d6cd-b765z   0/1     ContainerCreating   0          13s   <none>   worker01   <none>           <none>

NAME              TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)                                     AGE   SELECTOR
service/traefik   NodePort   10.106.81.178   <none>        9000:30466/TCP,80:30525/TCP,443:30758/TCP   13s   app.kubernetes.io/instance=traefik,app.kubernetes.io/name=traefik

NAME                      READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS   IMAGES          SELECTOR
deployment.apps/traefik   0/1     1            0           13s   traefik      traefik:2.5.3   app.kubernetes.io/instance=traefik,app.kubernetes.io/name=traefik

NAME                                 DESIRED   CURRENT   READY   AGE   CONTAINERS   IMAGES          SELECTOR
replicaset.apps/traefik-5bd4d8d6cd   1         1         0       13s   traefik      traefik:2.5.3   app.kubernetes.io/instance=traefik,app.kubernetes.io/name=traefik,pod-template-hash=5bd4d8d6cd
(venv) ➜  char git:(dev) kubectl get all -n traefik-ingress -o wide
NAME                           READY   STATUS    RESTARTS   AGE   IP             NODE       NOMINATED NODE   READINESS GATES
pod/traefik-5bd4d8d6cd-b765z   1/1     Running   0          61s   10.244.1.116   worker01   <none>           <none>

NAME              TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)                                     AGE   SELECTOR
service/traefik   NodePort   10.106.81.178   <none>        9000:30466/TCP,80:30525/TCP,443:30758/TCP   61s   app.kubernetes.io/instance=traefik,app.kubernetes.io/name=traefik

NAME                      READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS   IMAGES          SELECTOR
deployment.apps/traefik   1/1     1            1           61s   traefik      traefik:2.5.3   app.kubernetes.io/instance=traefik,app.kubernetes.io/name=traefik

NAME                                 DESIRED   CURRENT   READY   AGE   CONTAINERS   IMAGES          SELECTOR
replicaset.apps/traefik-5bd4d8d6cd   1         1         1       61s   traefik      traefik:2.5.3   app.kubernetes.io/instance=traefik,app.kubernetes.io/name=traefik,pod-template-hash=5bd4d8d6cd
(venv) ➜  char git:(dev)
```

### 4.访问svc. 
使用公务ip或域名访问30466

先在内网测试:
```
venv) ➜  char git:(dev) kubectl get svc -n traefik-ingress
NAME      TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)                                     AGE
traefik   NodePort   10.106.81.178   <none>        9000:30466/TCP,80:30525/TCP,443:30758/TCP   4m20s
(venv) ➜  char git:(dev) curl -v 10.106.81.178:9000
*   Trying 10.106.81.178:9000...
* TCP_NODELAY set
* Connected to 10.106.81.178 (10.106.81.178) port 9000 (#0)
> GET / HTTP/1.1
> Host: 10.106.81.178:9000
> User-Agent: curl/7.68.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 301 Moved Permanently
< Location: http://10.106.81.178:9000/dashboard/
< Date: Thu, 09 Dec 2021 02:59:05 GMT
< Content-Length: 17
< Content-Type: text/plain; charset=utf-8
<
* Connection #0 to host 10.106.81.178 left intact
Moved Permanently# 
(venv) ➜  char git:(dev)
```

云主机开放对应端口:
```
(venv) ➜  char git:(dev) curl -v http://k8s.pyhuo.top:30466
*   Trying 8.142.109.91:30466...
* TCP_NODELAY set
* Connected to k8s.pyhuo.top (8.142.109.91) port 30466 (#0)
> GET / HTTP/1.1
> Host: k8s.pyhuo.top:30466
> User-Agent: curl/7.68.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 301 Moved Permanently
< Location: http://k8s.pyhuo.top:30466/dashboard/
< Date: Thu, 09 Dec 2021 06:23:05 GMT
< Content-Length: 17
< Content-Type: text/plain; charset=utf-8
<
* Connection #0 to host k8s.pyhuo.top left intact
Moved Permanently# 
(venv) ➜  char git:(dev)
```

## 部署whoami 测试

```
```