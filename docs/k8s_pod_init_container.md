## init 容器

[文档](https://kubernetes.io/zh/docs/concepts/workloads/pods/init-containers/)

init 容器是一种特殊容器，在 Pod 内的应用容器启动之前运行。Init 容器可以包括一些应用镜像中不存在的实用工具和安装脚本

每个 Pod 中可以包含多个容器， 应用运行在这些容器里面，同时 Pod 也可以有一个或多

Init 容器与普通的容器非常像，除了如下两点:
* 它们总是运行到完成
* 每个都必须在下一个启动之前成功完成

如果 Pod 的 Init 容器失败，kubelet 会不断地重启该 Init 容器直到该容器成功为止.

eg: 运行python web app 时，先执行python version 查看版本号，确保python 已经安装.