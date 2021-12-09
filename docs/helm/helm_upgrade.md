##  upgrade 

### upgrade traefik

```
(venv) ➜  char git:(dev) ✗ helm ls -A
NAME   	NAMESPACE      	REVISION	UPDATED                                	STATUS  	CHART         	APP VERSION
traefik	traefik-ingress	1       	2021-12-09 10:54:31.455233115 +0800 CST	deployed	traefik-10.6.0	2.5.3
(venv) ➜  char git:(dev) ✗
```

```
(venv) ➜  char git:(dev) ✗ helm ls -A
NAME   	NAMESPACE      	REVISION	UPDATED                                	STATUS  	CHART         	APP VERSION
traefik	traefik-ingress	1       	2021-12-09 10:54:31.455233115 +0800 CST	deployed	traefik-10.6.0	2.5.3
(venv) ➜  char git:(dev) ✗ helm upgrade -f traefik/my-value.yaml traefik ./traefik -n traefik-ingress
Release "traefik" has been upgraded. Happy Helming!
NAME: traefik
LAST DEPLOYED: Thu Dec  9 14:54:13 2021
NAMESPACE: traefik-ingress
STATUS: deployed
REVISION: 2
TEST SUITE: None
(venv) ➜  char git:(dev) ✗ helm ls -A
NAME   	NAMESPACE      	REVISION	UPDATED                                	STATUS  	CHART         	APP VERSION
traefik	traefik-ingress	2       	2021-12-09 14:54:13.702322293 +0800 CST	deployed	traefik-10.6.0	2.5.3
(venv) ➜  char git:(dev) ✗
```

## 回滚 helm rollback



```
(venv) ➜  char git:(dev) ✗ helm ls -A
NAME   	NAMESPACE      	REVISION	UPDATED                                	STATUS  	CHART         	APP VERSION
traefik	traefik-ingress	2       	2021-12-09 14:54:13.702322293 +0800 CST	deployed	traefik-10.6.0	2.5.3
(venv) ➜  char git:(dev) ✗ helm rollback  traefik 1 -n traefik-ingress
Rollback was a success! Happy Helming!
(venv) ➜  char git:(dev) ✗ helm ls -A
NAME   	NAMESPACE      	REVISION	UPDATED                                	STATUS  	CHART         	APP VERSION
traefik	traefik-ingress	3       	2021-12-09 14:59:11.498227548 +0800 CST	deployed	traefik-10.6.0	2.5.3
(venv) ➜  char git:(dev) ✗
```