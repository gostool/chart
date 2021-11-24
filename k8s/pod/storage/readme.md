## Pod 使用 PersistentVolume 作为存储

[文档](https://kubernetes.io/zh/docs/tasks/configure-pod-container/configure-persistent-volume-storage/)



## pod

```
(venv) ➜  k8s git:(dev) kubectl get pv
NAME             CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS      CLAIM   STORAGECLASS   REASON   AGE
task-pv-volume   4Gi        RWO            Retain           Available           manual                  4s
(venv) ➜  k8s git:(dev) kubectl apply -f pod/storage/pv-claim.yaml
persistentvolumeclaim/task-pv-claim created
(venv) ➜  k8s git:(dev) kubectl get pvc
NAME            STATUS   VOLUME           CAPACITY   ACCESS MODES   STORAGECLASS   AGE
task-pv-claim   Bound    task-pv-volume   4Gi        RWO            manual         2s
```
pv -> Bound
```
(venv) ➜  k8s git:(dev) kubectl get pv
NAME             CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                   STORAGECLASS   REASON   AGE
task-pv-volume   4Gi        RWO            Retain           Bound    default/task-pv-claim   manual                  59s
(venv) ➜  k8s git:(dev)
```

```
kubectl exec -it task-pv-pod -- /bin/sh
```

```
kubectl delete pod task-pv-pod
kubectl delete pvc task-pv-claim
kubectl delete pv task-pv-volume
```


