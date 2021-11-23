## Volumes(卷)

[文档](https://kubernetes.io/zh/docs/concepts/storage/volumes/)

[阿里云学习文档](https://edu.aliyun.com/lesson_1651_18381?spm=5176.10731542.0.0.54767abdF6t4Wb#_18381)


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

## 处于released状态下的pv如何复用

这里有一个点需要特别说明一下：当 PV 已经处在 released 状态下，它是没有办法直接回到 available 状态，也就是说接下来无法被一个新的 PVC 去做绑定。如果我们想把已经 released 的 PV 复用，我们这个时候通常应该怎么去做呢？

- 第一种方式：我们可以新建一个 PV 对象，然后把之前的 released 的 PV 的相关字段的信息填到新的 PV 对象里面，这样的话，这个 PV 就可以结合新的 PVC 了；
- 第二种是我们在删除 pod 之后，不要去删除 PVC 对象，这样给 PV 绑定的 PVC 还是存在的，下次 pod 使用的时候，就可以直接通过 PVC 去复用。K8s中的 StatefulSet 管理的 Pod 带存储的迁移就是通过这种方式。
