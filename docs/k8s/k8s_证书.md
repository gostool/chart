## 证书问题

### PKI 证书和要求
[pki](https://kubernetes.io/zh/docs/setup/best-practices/certificates/)


Kubernetes 需要 PKI 证书才能进行基于 TLS 的身份验证。
如果你是使用 kubeadm 安装的 Kubernetes， 则会自动生成集群所需的证书。
你还可以生成自己的证书。 例如，不将私钥存储在 API 服务器上，可以让私钥更加安全。
此页面说明了集群必需的证书。


### 集群是如何使用证书的

Kubernetes 需要 PKI 才能执行以下操作：

* Kubelet 的客户端证书，用于 API 服务器身份验证
* API 服务器端点的证书
* 集群管理员的客户端证书，用于 API 服务器身份认证
* API 服务器的客户端证书，用于和 Kubelet 的会话
* API 服务器的客户端证书，用于和 etcd 的会话
* 控制器管理器的客户端证书/kubeconfig，用于和 API 服务器的会话
* 调度器的客户端证书/kubeconfig，用于和 API 服务器的会话
* 前端代理 的客户端及服务端证书
