## ingress-controllers(Ingress 控制器)

为了让 Ingress 资源工作，集群必须有一个正在运行的 Ingress 控制器。

与作为 kube-controller-manager 可执行文件的一部分运行的其他类型的控制器不同， Ingress 控制器不是随集群自动启动的。 基于此页面，你可选择最适合你的集群的 ingress 控制器实现



Kubernetes 作为一个项目，目前支持和维护 AWS， GCE 和 nginx Ingress 控制器。

其他控制器
说明： 本部分链接到提供 Kubernetes 所需功能的第三方项目。Kubernetes 项目作者不负责这些项目。此页面遵循CNCF 网站指南，按字母顺序列出项目。要将项目添加到此列表中，请在提交更改之前阅读内容指南。
* HAProxy Ingress 针对 HAProxy 的 Ingress 控制器。
用于 Kubernetes 的 HAProxy Ingress 控制器 也是一个针对 HAProxy 的 Ingress 控制器。
* Istio Ingress 是一个基于 Istio 的 Ingress 控制器。
用于 Kubernetes 的 Kong Ingress 控制器 是一个用来驱动 Kong Gateway 的 Ingress 控制器。
用于 Kubernetes 的 NGINX Ingress 控制器 能够与 NGINX Web 服务器（作为代理） 一起使用。
* Traefik Kubernetes Ingress 提供程序 是一个用于 Traefik 代理的 Ingress 控制器。

[nginx-ingress](https://kubernetes.github.io/ingress-nginx/deploy/)
[NGINX Ingress Controller](https://github.com/kubernetes/ingress-nginx/blob/main/README.md#readme)


## install ingress-nginx
[helm install](https://kubernetes.github.io/ingress-nginx/deploy/)
```
helm upgrade --install ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace
```


```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.1.0/deploy/static/provider/cloud/deploy.yaml
```