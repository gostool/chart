# helm  
想成功和正确地使用Helm，需要一个k8s集群.
[官方快速开始](https://helm.sh/zh/docs/intro/quickstart/)

[官方chart](https://artifacthub.io/packages/helm/bitnami/redis)


* 选择正确的版本
* 配置源
* 基本命令

## 版本选择
[参考](https://helm.sh/zh/docs/topics/version_skew/)

k8s: 1.20
helm: 选择3.5.x

```
ubuntu@VM-4-8-ubuntu:~/apps/linux-amd64$ kubectl version
Client Version: version.Info{Major:"1", Minor:"20", GitVersion:"v1.20.2", GitCommit:"faecb196815e248d3ecfb03c680a4507229c2a56", GitTreeState:"clean", BuildDate:"2021-01-13T13:28:09Z", GoVersion:"go1.15.5", Compiler:"gc", Platform:"linux/amd64"}
Server Version: version.Info{Major:"1", Minor:"20", GitVersion:"v1.20.2", GitCommit:"faecb196815e248d3ecfb03c680a4507229c2a56", GitTreeState:"clean", BuildDate:"2021-01-13T13:20:00Z", GoVersion:"go1.15.5", Compiler:"gc", Platform:"linux/amd64"}
ubuntu@VM-4-8-ubuntu:~/apps/linux-amd64$ minikube version
minikube version: v1.20.0
commit: b017ea15ffbf8bcd6ce31e13ba16f59fd4091079
ubuntu@VM-4-8-ubuntu:~/apps/linux-amd64$ kubectl version -o json
{
  "clientVersion": {
    "major": "1",
    "minor": "20",
    "gitVersion": "v1.20.2",
    "gitCommit": "faecb196815e248d3ecfb03c680a4507229c2a56",
    "gitTreeState": "clean",
    "buildDate": "2021-01-13T13:28:09Z",
    "goVersion": "go1.15.5",
    "compiler": "gc",
    "platform": "linux/amd64"
  },
  "serverVersion": {
    "major": "1",
    "minor": "20",
    "gitVersion": "v1.20.2",
    "gitCommit": "faecb196815e248d3ecfb03c680a4507229c2a56",
    "gitTreeState": "clean",
    "buildDate": "2021-01-13T13:20:00Z",
    "goVersion": "go1.15.5",
    "compiler": "gc",
    "platform": "linux/amd64"
  }
}
ubuntu@VM-4-8-ubuntu:~/apps/linux-amd64$
```

## 配置阿里源

* 添加阿里源
* 测试

```
ubuntu@VM-4-8-ubuntu:~/apps/linux-amd64$ ./helm repo add stable https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts
"stable" has been added to your repositories
ubuntu@VM-4-8-ubuntu:~/apps/linux-amd64$ ./helm repo list
NAME  	URL
stable	https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts
ubuntu@VM-4-8-ubuntu:~/apps/linux-amd64$
```


```
ubuntu@VM-4-8-ubuntu:~/apps/linux-amd64$ ./helm search repo mysql
NAME                         	CHART VERSION	APP VERSION	DESCRIPTION
stable/mysql                 	0.3.5        	           	Fast, reliable, scalable, and easy to use open-...
stable/percona               	0.3.0        	           	free, fully compatible, enhanced, open source d...
stable/percona-xtradb-cluster	0.0.2        	5.7.19     	free, fully compatible, enhanced, open source d...
stable/gcloud-sqlproxy       	0.2.3        	           	Google Cloud SQL Proxy
stable/mariadb               	2.1.6        	10.1.31    	Fast, reliable, scalable, and easy to use open-...
```

## helm 基本命令
* 查看: helm search
* 下载: helm pull
* 安装: helm install
* 删除: helm delete
* rollback 恢复

### helm mysql 下载/安装/删除/恢复

下载并解压:
```
➜  char git:(dev) ✗ helm pull bitnami/mysql --untar
➜  char git:(dev) ✗ tree mysql 
mysql
├── Chart.lock
├── Chart.yaml
├── README.md
├── charts
│   └── common
│       ├── Chart.yaml
│       ├── README.md
│       ├── templates
│       │   ├── _affinities.tpl
│       │   ├── _capabilities.tpl
│       │   ├── _errors.tpl
│       │   ├── _images.tpl
│       │   ├── _ingress.tpl
│       │   ├── _labels.tpl
│       │   ├── _names.tpl
│       │   ├── _secrets.tpl
│       │   ├── _storage.tpl
│       │   ├── _tplvalues.tpl
│       │   ├── _utils.tpl
│       │   ├── _warnings.tpl
│       │   └── validations
│       │       ├── _cassandra.tpl
│       │       ├── _mariadb.tpl
│       │       ├── _mongodb.tpl
│       │       ├── _postgresql.tpl
│       │       ├── _redis.tpl
│       │       └── _validations.tpl
│       └── values.yaml
├── ci
│   └── values-production-with-rbac.yaml
├── templates
│   ├── NOTES.txt
│   ├── _helpers.tpl
│   ├── extra-list.yaml
│   ├── metrics-svc.yaml
│   ├── networkpolicy.yaml
│   ├── primary
│   │   ├── configmap.yaml
│   │   ├── initialization-configmap.yaml
│   │   ├── pdb.yaml
│   │   ├── statefulset.yaml
│   │   ├── svc-headless.yaml
│   │   └── svc.yaml
│   ├── role.yaml
│   ├── rolebinding.yaml
│   ├── secondary
│   │   ├── configmap.yaml
│   │   ├── pdb.yaml
│   │   ├── statefulset.yaml
│   │   ├── svc-headless.yaml
│   │   └── svc.yaml
│   ├── secrets.yaml
│   ├── serviceaccount.yaml
│   └── servicemonitor.yaml
├── values.schema.json
└── values.yaml

8 directories, 48 files
➜  char git:(dev) ✗
```

```
ubuntu@VM-4-8-ubuntu:~/apps/chart$ helm install mysql  bitnami/mysql -n db
NAME: mysql
LAST DEPLOYED: Wed Sep 15 17:15:19 2021
NAMESPACE: db
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
** Please be patient while the chart is being deployed **

Tip:

  Watch the deployment status using the command: kubectl get pods -w --namespace db

Services:

  echo Primary: mysql.db.svc.cluster.local:3306

Execute the following to get the administrator credentials:

  echo Username: root
  MYSQL_ROOT_PASSWORD=$(kubectl get secret --namespace db mysql -o jsonpath="{.data.mysql-root-password}" | base64 --decode)

To connect to your database:

  1. Run a pod that you can use as a client:

      kubectl run mysql-client --rm --tty -i --restart='Never' --image  docker.io/bitnami/mysql:8.0.26-debian-10-r31 --namespace db --command -- bash

  2. To connect to primary service (read/write):

      mysql -h mysql.db.svc.cluster.local -uroot -p"$MYSQL_ROOT_PASSWORD"



To upgrade this helm chart:

  1. Obtain the password as described on the 'Administrator credentials' section and set the 'root.password' parameter as shown below:

      ROOT_PASSWORD=$(kubectl get secret --namespace db mysql -o jsonpath="{.data.mysql-root-password}" | base64 --decode)
      helm upgrade --namespace db mysql bitnami/mysql --set auth.rootPassword=$ROOT_PASSWORD
```

list:
```
ubuntu@VM-4-8-ubuntu:~/apps/chart$ helm list -n db
NAME 	NAMESPACE	REVISION	UPDATED                                	STATUS  	CHART      	APP VERSION
mysql	db       	1       	2021-09-15 17:15:19.396058159 +0800 CST	deployed	mysql-8.8.7	8.0.26
```

delete:
```
ubuntu@VM-4-8-ubuntu:~/apps/chart$ helm delete mysql -n db
release "mysql" uninstalled
ubuntu@VM-4-8-ubuntu:~/apps/chart$e
```

后期改一下
rollback: 
chart:redis  
版本:1
```
ubuntu@VM-4-8-ubuntu:~/apps/chart/k8s/char$ helm  list -n db
NAME 	NAMESPACE	REVISION	UPDATED                                	STATUS  	CHART       	APP VERSION
mysql	db       	1       	2021-09-24 16:55:19.537550603 +0800 CST	deployed	mysql-8.8.7 	8.0.26
ubuntu@VM-4-8-ubuntu:~/apps/chart/k8s/char$ helm uninstall mysql --keep-history -n db
release "mysql" uninstalled
ubuntu@VM-4-8-ubuntu:~/apps/chart/k8s/char$ helm list -n db
NAME 	NAMESPACE	REVISION	UPDATED                                	STATUS  	CHART       	APP VERSION
ubuntu@VM-4-8-ubuntu:~/apps/chart/k8s/char$ helm rollback mysql 1 -n db
Rollback was a success! Happy Helming!
ubuntu@VM-4-8-ubuntu:~/apps/chart/k8s/char$ helm list -n db
NAME 	NAMESPACE	REVISION	UPDATED                                	STATUS  	CHART       	APP VERSION
mysql	db       	2       	2021-09-24 16:56:34.311259388 +0800 CST	deployed	mysql-8.8.7 	8.0.26
ubuntu@VM-4-8-ubuntu:~/apps/chart/k8s/char$
```