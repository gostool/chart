## chart开发提示和技巧

[chart开发提示和技巧](https://helm.sh/zh/docs/howto/charts_tips_and_tricks/)

* go模版引擎
* 渲染变量


渲染额外的配置文件
```yml
# external configuration file conf/app.conf
firstName={{ .Values.firstName }}
lastName={{ .Values.lastName }}

# values
firstName: Peter
lastName: Parker

# template
{{ tpl (.Files.Get "conf/app.conf") . }}

# output
firstName=Peter
lastName=Parker
```


## Chart.yaml 文件

Chart.yaml文件是chart必需的。包含了以下字段
```yml
apiVersion: chart API 版本 （必需）
name: chart名称 （必需）
version: 语义化2 版本（必需）
kubeVersion: 兼容Kubernetes版本的语义化版本（可选）
description: 一句话对这个项目的描述（可选）
type: chart类型 （可选）
keywords:
  - 关于项目的一组关键字（可选）
home: 项目home页面的URL （可选）
sources:
  - 项目源码的URL列表（可选）
dependencies: # chart 必要条件列表 （可选）
  - name: chart名称 (nginx)
    version: chart版本 ("1.2.3")
    repository: （可选）仓库URL ("https://example.com/charts") 或别名 ("@repo-name")
    condition: （可选） 解析为布尔值的yaml路径，用于启用/禁用chart (e.g. subchart1.enabled )
    tags: # （可选）
      - 用于一次启用/禁用 一组chart的tag
    import-values: # （可选）
      - ImportValue 保存源值到导入父键的映射。每项可以是字符串或者一对子/父列表项
    alias: （可选） chart中使用的别名。当你要多次添加相同的chart时会很有用
maintainers: # （可选）
  - name: 维护者名字 （每个维护者都需要）
    email: 维护者邮箱 （每个维护者可选）
    url: 维护者URL （每个维护者可选）
icon: 用做icon的SVG或PNG图片URL （可选）
appVersion: 包含的应用版本（可选）。不需要是语义化，建议使用引号
deprecated: 不被推荐的chart （可选，布尔值）
annotations:
  example: 按名称输入的批注列表 （可选）.
```

## helm create mychart
* 创建chart
* 安装

```
ubuntu@VM-4-8-ubuntu:~/apps/chart/k8s/char$ helm create mychart
ubuntu@VM-4-8-ubuntu:~/apps/chart/k8s/char$ tree mychart/
mychart/
├── Chart.yaml
├── templates
│   ├── NOTES.txt
│   ├── _helpers.tpl
│   ├── deployment.yaml
│   ├── hpa.yaml
│   ├── ingress.yaml
│   ├── service.yaml
│   ├── serviceaccount.yaml
│   └── tests
│       └── test-connection.yaml
└── values.yaml

2 directories, 10 files
ubuntu@VM-4-8-ubuntu:~/apps/chart/k8s/char$ helm ls
NAME         	NAMESPACE	REVISION	UPDATED                                	STATUS  	CHART              	APP VERSION
deis-workflow	default  	1       	2021-09-15 18:24:02.256027486 +0800 CST	deployed	deis-workflow-0.1.0	1.16.0
ubuntu@VM-4-8-ubuntu:~/apps/chart/k8s/char$ helm  install mychart ./mychart/
NAME: mychart
LAST DEPLOYED: Fri Sep 24 17:25:56 2021
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=mychart,app.kubernetes.io/instance=mychart" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
ubuntu@VM-4-8-ubuntu:~/apps/chart/k8s/char$ helm ls
NAME         	NAMESPACE	REVISION	UPDATED                                	STATUS  	CHART              	APP VERSION
deis-workflow	default  	1       	2021-09-15 18:24:02.256027486 +0800 CST	deployed	deis-workflow-0.1.0	1.16.0
mychart      	default  	1       	2021-09-24 17:25:56.633330062 +0800 CST	deployed	mychart-0.1.0      	1.16.0
ubuntu@VM-4-8-ubuntu:~/apps/chart/k8s/char$ export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=mychart,app.kubernetes.io/instance=mychart" -o jsonpath="{.items[0].metadata.name}")
ubuntu@VM-4-8-ubuntu:~/apps/chart/k8s/char$ export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
ubuntu@VM-4-8-ubuntu:~/apps/chart/k8s/char$  echo "Visit http://127.0.0.1:8080 to use your application"
Visit http://127.0.0.1:8080 to use your application
ubuntu@VM-4-8-ubuntu:~/apps/chart/k8s/char$ kubectl --namespace default --address 0.0.0.0  port-forward $POD_NAME 8080:$CONTAINER_PORT
Forwarding from 0.0.0.0:8080 -> 80
Handling connection for 8080
Handling connection for 8080
^C
ubuntu@VM-4-8-ubuntu:~/apps/chart/k8s/char$
```


修改Chart.yaml 版本号. helm update

```sh
ubuntu@VM-4-8-ubuntu:~/apps/chart/k8s/char$ git pull
remote: Enumerating objects: 11, done.
remote: Counting objects: 100% (11/11), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 6 (delta 4), reused 6 (delta 4), pack-reused 0
Unpacking objects: 100% (6/6), done.
From github.com:gostool/chart
   e70fbb1..d7a2fd3  dev        -> origin/dev
Updating e70fbb1..d7a2fd3
Fast-forward
 k8s/char/mychart/Chart.yaml | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
ubuntu@VM-4-8-ubuntu:~/apps/chart/k8s/char$  helm upgrade mychart ./mychart/
Release "mychart" has been upgraded. Happy Helming!
NAME: mychart
LAST DEPLOYED: Fri Sep 24 17:34:10 2021
NAMESPACE: default
STATUS: deployed
REVISION: 3
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=mychart,app.kubernetes.io/instance=mychart" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward --address 0.0.0.0 $POD_NAME 8080:$CONTAINER_PORT
  echo "Visit http://ip:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
ubuntu@VM-4-8-ubuntu:~/apps/chart/k8s/char$ helm ls
NAME         	NAMESPACE	REVISION	UPDATED                                	STATUS  	CHART              	APP VERSION
deis-workflow	default  	1       	2021-09-15 18:24:02.256027486 +0800 CST	deployed	deis-workflow-0.1.0	1.16.0
mychart      	default  	3       	2021-09-24 17:34:10.682504572 +0800 CST	deployed	mychart-0.1.0      	1.16.1
ubuntu@VM-4-8-ubuntu:~/apps/chart/k8s/char$
```