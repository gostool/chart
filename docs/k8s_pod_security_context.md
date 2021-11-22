## pod Security Context 介绍
[文档](https://kubernetes.io/zh/docs/tasks/configure-pod-container/security-context/)
Security Context 主要用于限制容器行为，保障系统和其他容器安全

1.容器级别的Security Context 仅对指定容器生效.
2.pod级别的Security Context 仅对指定Pod中的所有容器生效
3.Pod Security Context (PSC) 对集群所有Pod生效


安全上下文（Security Context）定义 Pod 或 Container 的特权与访问控制设置。 安全上下文包括但不限于：

* 自主访问控制（Discretionary Access Control）：基于 用户 ID（UID）和组 ID（GID）. 来判定对对象（例如文件）的访问权限。
* 安全性增强的 Linux（SELinux）： 为对象赋予安全性标签。
* 以特权模式或者非特权模式运行。
* Linux 权能: 为进程赋予 root 用户的部分特权而非全部特权。
* AppArmor：使用程序框架来限制个别程序的权能。
* Seccomp：过滤进程的系统调用。
* AllowPrivilegeEscalation：控制进程是否可以获得超出其父进程的特权。 此布尔值直接控制是否为容器进程设置 no_new_privs标志。 当容器以特权模式运行或者具有 CAP_SYS_ADMIN 权能时，AllowPrivilegeEscalation 总是为 true。
* readOnlyRootFilesystem：以只读方式加载容器的根文件系统。
以上条目不是安全上下文设置的完整列表 -- 请参阅 SecurityContext 了解其完整列表。

关于在 Linux 系统中的安全机制的更多信息，可参阅 Linux 内核安全性能力概述。

