## dashboard

[helm](https://artifacthub.io/packages/helm/k8s-dashboard/kubernetes-dashboard	)

[github](https://github.com/kubernetes/dashboard)


## 版本: 5.0.4
```
helm install my-kubernetes-dashboard k8s-dashboard/kubernetes-dashboard --version 5.0.4
```


## token 默认900s过期

[github源码](https://github.com/kubernetes/dashboard/blob/master/src/app/backend/auth/api/types.go#L29)



