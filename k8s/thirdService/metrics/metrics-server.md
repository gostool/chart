
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

### x509

[x509 issue](https://github.com/kubernetes-sigs/metrics-server/issues/131)

```
        command:
        - /metrics-server
        - --kubelet-insecure-tls
        - --kubelet-preferred-address-types=InternalIP

```

在args中增加`--kubelet-insecure-tls`参数.


### 查看

```
(venv) ➜  k8s git:(dev) kubectl top
Display Resource (CPU/Memory) usage.

 The top command allows you to see the resource consumption for nodes or pods.

 This command requires Metrics Server to be correctly configured and working on the server.

Available Commands:
  node        Display resource (CPU/memory) usage of nodes
  pod         Display resource (CPU/memory) usage of pods

Usage:
  kubectl top [flags] [options]

Use "kubectl <command> --help" for more information about a given command.
Use "kubectl options" for a list of global command-line options (applies to all commands).
(venv) ➜  k8s git:(dev) kubectl top node
NAME          CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%
master-node   123m         6%     2104Mi          54%
worker01      71m          3%     1273Mi          33%
(venv) ➜  k8s git:(dev) kubectl top pod
NAME                     CPU(cores)   MEMORY(bytes)
nginx-6799fc88d8-nsqcz   0m           3Mi
task-pv-pod              0m           3Mi
(venv) ➜  k8s git:(dev)
```
