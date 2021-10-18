## deployment
* relicas:3
* pod: myapp
* image: nginx

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  # pod 选择器
  selector:
    matchLabels:
      app: myapp
  # 期望pod数量
  replicas: 3
  # pod 模版
  template:
    metadata:
      # 标签
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        # pod 镜像
        image: nginx:alpine
        resources:
          limits:
            memory: "128Mi"
            # 单位后缀 m 表示千分之一核，也就是说 1 Core = 1000m
            # 10% * 3 = 30%
            cpu: "100m"
        ports:
        - containerPort: 80

```

## 查看状态
* READY: 当前实际的pod数量/期望pod的数量
* UP-TO-DATE: 到达期望版本的pod数量
* AVAILABLE: 运行中并可用的pod
* AGE: deployment创建的时长

```
➜  depolyment git:(dev) git pull
remote: Enumerating objects: 15, done.
remote: Counting objects: 100% (15/15), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 11 (delta 7), reused 9 (delta 5), pack-reused 0
Unpacking objects: 100% (11/11), done.
From github.com:gostool/chart
   0dcc4b8..a01c157  dev        -> origin/dev
Updating 0dcc4b8..a01c157
Fast-forward
 k8s/depolyment/readme.md | 19 +++++++++++++++++++
 k8s/depolyment/tpl.yaml  | 11 ++++++++++-
 2 files changed, 29 insertions(+), 1 deletion(-)
 create mode 100644 k8s/depolyment/readme.md
➜  depolyment git:(dev) kubectl apply -f tpl.yaml
deployment.apps/myapp configured
➜  depolyment git:(dev) kubectl get deployment -o wide
NAME            READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS      IMAGES         SELECTOR
deis-workflow   1/1     1            1           26d   deis-workflow   nginx:1.16.0   app.kubernetes.io/instance=deis-workflow,app.kubernetes.io/name=deis-workflow
myapp           3/3     3            3           25m   myapp           nginx:alpine   app=myapp
mychart         1/1     1            1           17d   mychart         nginx:1.16.1   app.kubernetes.io/instance=mychart,app.kubernetes.io/name=mychart
➜  depolyment git:(dev)
```


## 更新镜像
* nginx 升级到1.16.1
* [set image](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#-em-image-em-)
* [参考](https://edu.aliyun.com/lesson_1651_17057?spm=5176.10731542.0.0.4e477abdAjSJSN#_17057)
```
kubectl set image deployment.v1.apps/myapp myapp=nginx:1.16.1
	    设置镜像   资料类型             
					                deployment名字
										    需要更新的容器名字=新的镜像
```


```
➜  depolyment git:(dev) kubectl set image deployment.v1.apps/myapp myapp=nginx:1.16.1
deployment.apps/myapp image updated
➜  depolyment git:(dev) kubectl get deployment -o wide
NAME            READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS      IMAGES         SELECTOR
deis-workflow   1/1     1            1           26d   deis-workflow   nginx:1.16.0   app.kubernetes.io/instance=deis-workflow,app.kubernetes.io/name=deis-workflow
myapp           3/3     1            3           30m   myapp           nginx:1.16.1   app=myapp
mychart         1/1     1            1           17d   mychart         nginx:1.16.1   app.kubernetes.io/instance=mychart,app.kubernetes.io/name=mychart
➜  depolyment git:(dev)
```

## 回滚镜像
* rollout:
* history: 查看版本

```
➜  depolyment git:(dev) kubectl get deployment -o wide
NAME            READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS      IMAGES         SELECTOR
deis-workflow   1/1     1            1           26d   deis-workflow   nginx:1.16.0   app.kubernetes.io/instance=deis-workflow,app.kubernetes.io/name=deis-workflow
myapp           3/3     3            3           24m   myapp           nginx:1.16.1   app=myapp
mychart         1/1     1            1           17d   mychart         nginx:1.16.1   app.kubernetes.io/instance=mychart,app.kubernetes.io/name=mychart
➜  depolyment git:(dev) kubectl rollout history deployment/myapp
deployment.apps/myapp
REVISION  CHANGE-CAUSE
1         <none>
2         <none>

➜  depolyment git:(dev) kubectl rollout history deployment/myapp --revision=1
deployment.apps/myapp with revision #1
Pod Template:
  Labels:	app=myapp
	pod-template-hash=758c55b554
  Containers:
   myapp:
    Image:	nginx:alpine
    Port:	80/TCP
    Host Port:	0/TCP
    Limits:
      cpu:	100m
      memory:	128Mi
    Environment:	<none>
    Mounts:	<none>
  Volumes:	<none>

➜  depolyment git:(dev) kubectl rollout undo deployment/myapp  --to-revision=1
deployment.apps/myapp rolled back
➜  depolyment git:(dev) kubectl get deployment -o wide
NAME            READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS      IMAGES         SELECTOR
deis-workflow   1/1     1            1           26d   deis-workflow   nginx:1.16.0   app.kubernetes.io/instance=deis-workflow,app.kubernetes.io/name=deis-workflow
myapp           3/3     3            3           25m   myapp           nginx:alpine   app=myapp
mychart         1/1     1            1           17d   mychart         nginx:1.16.1   app.kubernetes.io/instance=mychart,app.kubernetes.io/name=mychart
➜  depolyment git:(dev)
```