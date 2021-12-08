## traefik 

[教程](https://www.qikqiak.com/post/ingress-traefik1/)


helm install traefik
[文档](https://helm.traefik.io/traefik)
```
(venv) ➜  ~ helm repo add traefik https://helm.traefik.io/traefik
"traefik" has been added to your repositories
(venv) ➜  ~ helm repo update
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "metrics-server" chart repository
...Successfully got an update from the "nginx-stable" chart repository
...Successfully got an update from the "kubernetes-dashboard" chart repository
...Successfully got an update from the "k8s-dashboard" chart repository
...Successfully got an update from the "traefik" chart repository
...Successfully got an update from the "bitnami" chart repository
...Successfully got an update from the "138937-svc" chart repository
Update Complete. ⎈Happy Helming!⎈
(venv) ➜  ~ helm install traefik traefik/traefik
NAME: traefik
LAST DEPLOYED: Wed Dec  8 22:03:45 2021
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
(venv) ➜  ~ helm ls
NAME   	NAMESPACE	REVISION	UPDATED                                	STATUS  	CHART         	APP VERSION
traefik	default  	1       	2021-12-08 22:03:45.494206468 +0800 CST	deployed	traefik-10.7.1	2.5.4      
(venv) ➜  ~ 
```



## 访问


```
代理模式: http://172.16.181.180:31608/dashboard/
外网ip:  k8s.pyhuo.top:31608/dashboard/
```

