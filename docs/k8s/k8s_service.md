## Service(服务)

[service](https://kubernetes.io/zh/docs/concepts/services-networking/service/)

* NodePort: 直接映射到节点的真实端口
* LoadBalancer: 
* ClusterIP

## 虚拟 IP 和 Service 代理
[文档](https://kubernetes.io/zh/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies)

在 Kubernetes 集群中，每个 Node 运行一个 kube-proxy 进程。 kube-proxy 负责为 Service 实现了一种 VIP（虚拟 IP）的形式，而不是 ExternalName 的形式。



## 访问

```
 kubectl --namespace default port-forward --address 0.0.0.0  service/flower-service 8080:5555
```