
## helm

### 1.版本选择
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

### 2.配置阿里源

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
