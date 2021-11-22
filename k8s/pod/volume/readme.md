## empty dir

master: 节点. 创建empty-dir pod 同时在挂在目录创建a.log文件
```
(venv) ➜  k8s git:(dev) kubectl apply -f pod/volume/empty-dir.yaml
(venv) ➜  k8s git:(dev) kubectl get pod
NAME                                              READY   STATUS    RESTARTS   AGE
pod-volume-demo-emptydir                          1/1     Running   0          10m
(venv) ➜  k8s git:(dev) kubectl exec -it pod-volume-demo-emptydir  -- sh
/ # cd /cache/
/cache # date
Mon Nov 22 08:06:01 UTC 2021
/cache # date > a.log
/cache # ls -l
total 4
-rw-r--r--    1 root     root            29 Nov 22 08:06 a.log
command terminated with exit code 130
(venv) ➜  k8s git:(dev)
```


worker: 节点
```
(venv) ➜  ~ cd /var/lib/kubelet/pods/50cfdde7-b50b-4a2c-a9f4-01b07f6f2256/volumes/kubernetes.io\~empty-dir/cache-volume
(venv) ➜  cache-volume ll
total 12K
drwxrwxrwx 2 root root 4.0K Nov 22 15:56 .
drwxr-xr-x 3 root root 4.0K Nov 22 15:55 ..
-rw-r--r-- 1 root root   29 Nov 22 15:56 a.log
(venv) ➜  cache-volume cat a.log
Mon Nov 22 08:06:01 UTC 2021
(venv) ➜  cache-volume
```
删除pod后，目录也被删除


## hostpath