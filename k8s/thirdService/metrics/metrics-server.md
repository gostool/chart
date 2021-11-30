
## metrics-server

* [统计服务](https://github.com/kubernetes-sigs/metrics-server/)
* [helm](https://artifacthub.io/packages/helm/metrics-server/metrics-server)

minikube 默认不使用


```
helm repo add metrics-server https://kubernetes-sigs.github.io/metrics-server/
helm install metrics-server metrics-server/metrics-server
```


```
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```


## x509

[x509 issue](https://github.com/kubernetes-sigs/metrics-server/issues/131)

