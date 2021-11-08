## 设计理念
* 设计理念与分布式系统
* API设计原则
* 架构设计原则
* 引导（Bootstrapping）原则
* 核心技术概念和API对象
* Pod
* 复制控制器（Replication Controller，RC）
* 副本集（Replica Set，RS）
* 部署(Deployment)
* 服务（Service）
* 任务（Job）
* 后台支撑服务集（DaemonSet）
* 有状态服务集（StatefulSet)
* 集群联邦（Federation）
* 存储卷（Volume）
* 持久存储卷（Persistent Volume，PV）
* 持久存储卷声明（Persistent Volume Claim，PVC）
* 节点（Node）
* 密钥对象（Secret）
* 用户帐户（User Account）
* 服务帐户（Service Account）
* 名字空间（Namespace)


## API设计原则

Kubernetes集群系统每支持一项新功能，引入一项新技术，一定会新引入对应的API对象，支持对该功能的管理操作。
理解掌握的API，就好比抓住了K8s系统的牛鼻子。

Kubernetes系统API的设计有以下几条原则：
* 所有API应该是声明式的
* API对象是彼此互补而且可组合的
* 高层API以操作意图为基础设计
* 低层API根据高层API的控制需要设计
* 尽量避免简单封装，不要有在外部API无法显式知道的内部隐藏的机制
* API操作复杂度与对象数量成正比
* API对象状态不能依赖于网络连接状态
* 尽量避免让操作机制依赖于全局状态，因为在分布式系统中要保证全局状态的同步是非常困难的

## 控制机制设计原则
* 控制逻辑应该只依赖于当前状态
* 假设任何错误的可能，并做容错处理
* 尽量避免复杂状态机，控制逻辑不要依赖无法监控的内部状态
* 假设任何操作都可能被任何操作对象拒绝，甚至被错误解析
* 每个模块都可以在出错后自动恢复
* 每个模块都可以在必要时优雅地降级服务

