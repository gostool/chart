
## 为容器管理资源
* 请求: 哪里有
* 约束: app 吃多少

[文档](https://kubernetes.io/zh/docs/concepts/configuration/manage-resources-containers/)

当你定义 Pod 时可以选择性地为每个 容器设定所需要的资源数量。 最常见的可设定资源是 CPU 和内存（RAM）大小；此外还有其他类型的资源。

当你为 Pod 中的 Container 指定了资源 请求 时，调度器就利用该信息决定将 Pod 调度到哪个节点上。 当你还为 Container 指定了资源 约束 时，kubelet 就可以确保运行的容器不会使用超出所设约束的资源。 kubelet 还会为容器预留所 请求 数量的系统资源，供其使用

## 请求和约束

如果 Pod 运行所在的节点具有足够的可用资源，容器可能（且可以）使用超出对应资源 request 属性所设置的资源量。不过，容器不可以使用超出其资源 limit 属性所设置的资源量。

例如，如果你将容器的 memory 的请求量设置为 256 MiB，而该容器所处的 Pod 被调度到一个具有 8 GiB 内存的节点上，并且该节点上没有其他 Pods 运行，那么该容器就可以尝试使用更多的内存。

如果你将某容器的 memory 约束设置为 4 GiB，kubelet （和 容器运行时） 就会确保该约束生效。 容器运行时会禁止容器使用超出所设置资源约束的资源。 例如：当容器中进程尝试使用超出所允许内存量的资源时，系统内核会将尝试申请内存的进程终止， 并引发内存不足（OOM）错误。

约束值可以以被动方式来实现（系统会在发现违例时进行干预），或者通过强制生效的方式实现 （系统会避免容器用量超出约束值）。不同的容器运行时采用不同方式来实现相同的限制。



note:
```
如果某 Container 设置了自己的内存限制但未设置内存请求，Kubernetes 自动为其设置与内存限制相匹配的请求值。类似的，如果某 Container 设置了 CPU 限制值但未设置 CPU 请求值，则 Kubernetes 自动为其设置 CPU 请求 并使之与 CPU 限制值匹配。
```

##  资源类型
CPU 和内存都是资源类型。每种资源类型具有其基本单位。 CPU 表达的是计算处理能力，其单位是 Kubernetes CPUs。 内存的单位是字节。 如果你使用的是 Kubernetes v1.14 或更高版本，则可以指定巨页（Huge Page）资源。 巨页是 Linux 特有的功能，节点内核在其中分配的内存块比默认页大小大得多。

Pod 和 容器的资源请求和约束
Pod 中的每个容器都可以指定以下的一个或者多个值
* spec.containers[].resources.limits.cpu
* spec.containers[].resources.limits.memory
* spec.containers[].resources.limits.hugepages-<size>
* spec.containers[].resources.requests.cpu
* spec.containers[].resources.requests.memory
* spec.containers[].resources.requests.hugepages-<size>



## Kubernetes 中的资源单位
* CPU 的含义
* 内存的含义

```
CPU 资源的约束和请求以 CPU 为单位。
Kubernetes 中的一个 CPU 等于云平台上的 1 个 vCPU/核和裸机 Intel 处理器上的 1 个超线程。
你也可以表达带小数 CPU 的请求。spec.containers[].resources.requests.cpu 为 0.5 的 Container 肯定能够获得请求 1 CPU 的容器的一半 CPU 资源。表达式 0.1 等价于表达式 100m， 可以看作 “100 millicpu”。有些人说成是“一百毫 cpu”，其实说的是同样的事情。 具有小数点（如 0.1）的请求由 API 转换为 100m；最大精度是 1m。 因此，或许你应该优先考虑使用 100m 的形式。
CPU 总是按绝对数量来请求的，不可以使用相对数量； 0.1 的 CPU 在单核、双核、48 核的机器上的意义是一样的。
```

```
内存的约束和请求以字节为单位。你可以使用以下后缀之一以一般整数或定点数字形式来表示内存： E、P、T、G、M、k。你也可以使用对应的 2 的幂数：Ei、Pi、Ti、Gi、Mi、Ki。 例如，以下表达式所代表的是大致相同的值：

128974848、129e6、129M、123Mi
```