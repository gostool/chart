# 应用配置管理

背景问题: 
* 不可变基础设施(容器)的可变配置
* 敏感信息的存储和使用(密码/token)
* 集群中pod自我的身份认证
* 容器运行资源的配置管理
* 容器的运行安全管理
* 容器启动前置条件校验


## Pod的配置管理
* ConfigMap(可变配置)
* Secret(敏感信息)
* ServiceAccount(身份认证)
* Spec.Containers[].Resources.limits/requests(资源配置)
* Spec.Containers[].SecurityContext(安全管控)
* Spec.InitContainers(前置校验)


## 1. ConfigMap
* [文档](https://kubernetes.io/zh/docs/concepts/configuration/configmap/)


ConfigMap 是一种 API 对象，用来将非机密性的数据保存到键值对中。使用时， Pods 可以将其用作环境变量、命令行参数或者存储卷中的配置文件。
ConfigMap 将您的环境配置信息和容器镜解耦，便于应用配置的修改。
ConfigMap 并不提供保密或者加密功能。 如果你想存储的数据是机密的，请使用 Secret， 或者使用其他第三方工具来保证你的数据的私密性，而不是用 ConfigMap。
在 ConfigMap 中保存的数据不可超过1MiB.

### 1.1 ConfigMaps 和 Pods



