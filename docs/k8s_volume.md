## Volumes(卷)

[文档](https://kubernetes.io/zh/docs/concepts/storage/volumes/)


 Container 中的文件在磁盘上是临时存放的，这给 Container 中运行的较重要的应用 程序带来一些问题。
 问题之一是当容器崩溃时文件丢失。kubelet 会重新启动容器，但容器会以干净的状态重启。 
 第二个问题会在同一 Pod 中运行多个容器并共享文件时出现。 
 Kubernetes 卷（Volume） 这一抽象概念能够解决这两个问题。

 Docker 也有 卷（Volume） 的概念，但对它只有少量且松散的管理。 
 Docker 卷是磁盘上或者另外一个容器内的一个目录。 Docker 提供卷驱动程序，但是其功能非常有限。

## 卷类型

* 本地存储
	* emptyDir:
	* hostpath
* 网络存储
	* 云厂商
* Projected Volume: secret/configmap/serviceAccountToken
* PVC/PV



当 Pod 分派到某个 Node 上时，emptyDir 卷会被创建，并且在 Pod 在该节点上运行期间，卷一直存在。 
就像其名称表示的那样，卷最初是空的。 
尽管 Pod 中的容器挂载 emptyDir 卷的路径可能相同也可能不同，这些容器都可以读写 emptyDir 卷中相同的文件。 
当 Pod 因为某些原因被从节点上删除时，emptyDir 卷中的数据也会被永久删除。


## 存储和计算分离

## PV/PVC

PV: 存放存储的实际信息承载体. (具体怎么实现)
PVC: 简化User对存储的需要. (接口)