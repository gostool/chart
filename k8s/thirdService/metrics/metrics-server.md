
## metrics-server

* [统计服务](https://github.com/kubernetes-sigs/metrics-server/)
* [helm](https://artifacthub.io/packages/helm/metrics-server/metrics-server)

需要手动开启
```
venv) ➜  ~ kubectl top nodes
error: Metrics API not available
(venv) ➜  ~
```

### helm 安装 metrics-server

拉取镜像失败.
```
helm repo add metrics-server https://kubernetes-sigs.github.io/metrics-server/
helm install metrics-server metrics-server/metrics-server
```

### kubectl 使用yaml 在线安装
```
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

下载yaml后，手动修改镜像.

## x509

[x509 issue](https://github.com/kubernetes-sigs/metrics-server/issues/131)

```
        command:
        - /metrics-server
        - --kubelet-insecure-tls
        - --kubelet-preferred-address-types=InternalIP

```

在args中增加`--kubelet-insecure-tls`参数.