## RC
Replication Controller
[rc](https://kubernetes.io/zh/docs/concepts/workloads/controllers/replicationcontroller/)

当 Pod 数量过多时，ReplicationController 会终止多余的 Pod。当 Pod 数量太少时，ReplicationController 将会启动新的 Pod。 与手动创建的 Pod 不同，由 ReplicationController 创建的 Pod 在失败、被删除或被终止时会被自动替换



删除RC, 并不会影响通过该rc创建的pod. 可以先更新到replicas到0.
```
kubectl apply -f xx rc.yaml #可能无法更新.
```
