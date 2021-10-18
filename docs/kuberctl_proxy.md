

## kubectl proxy
* 访问Kubernetes API
* 访问dashboard


[proxy 命令](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#proxy)


在 localhost 和 Kubernetes API 服务器之间创建代理服务器或应用程序级网关。它还允许通过指定的 HTTP 路径提供静态内容。除了与静态内容路径匹配的路径外，所有传入数据都通过一个端口进入并转发到远程 Kubernetes API 服务器端口。

启动代理，把请求转发给Kubernetes API 
```
kubectl proxy --port=8888 --address=0.0.0.0 --accept-hosts='^.*' &
```


开启防火墙: 公网ip:8888. (不安全，不推荐，当前没有开启验证登陆)

使用代理访问: 内网ip:8888
![](https://oscimg.oschina.net/oscnet/up-ea6b39523148060630e1745a32226338a5c.png)