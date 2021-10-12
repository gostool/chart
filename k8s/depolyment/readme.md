## deployment


## 查看状态
* READY
* UP-TO-DATE
* AVAILABLE: 运行中并可用的pod
* AGE: deployment创建的时长
```
➜  depolyment git:(dev) kubectl get deployment -o wide
NAME            READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS      IMAGES         SELECTOR
deis-workflow   1/1     1            1           26d   deis-workflow   nginx:1.16.0   app.kubernetes.io/instance=deis-workflow,app.kubernetes.io/name=deis-workflow
myapp           2/3     3            2           15m   myapp           nginx:alpine   app=myapp
mychart         1/1     1            1           17d   mychart         nginx:1.16.1   app.kubernetes.io/instance=mychart,app.kubernetes.io/name=mychart
➜  depolyment git:(dev)

```


