## Pause容器背景
[Pause容器背景](https://jimmysong.io/kubernetes-handbook/concepts/pause-container.html)

[pause docker](https://github.com/kubernetes/kubernetes/tree/master/build/pause)

像 Pod 这样一个东西，本身是一个逻辑概念。那在机器上，它究竟是怎么实现的呢？这就是我们要解释的一个问题。

既然说 Pod 要解决这个问题，核心就在于如何让一个 Pod 里的多个容器之间最高效的共享某些资源和数据。

因为容器之间原本是被 Linux Namespace 和 cgroups 隔开的，所以现在实际要解决的是怎么去打破这个隔离，然后共享某些事情和某些信息。这就是 Pod 的设计要解决的核心问题所在。

所以说具体的解法分为两个部分：网络和存储。

Pause容器就是为解决Pod中的网络问题而生的



