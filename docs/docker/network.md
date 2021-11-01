## docker network
需要掌握2种网络模式:
* [host](https://docs.docker.com/network/host/)
* [brige](https://docs.docker.com/network/bridge/)


## host

容器使用网络模式，则该容器的网络堆栈不会与 Docker 主机隔离（容器共享主机的网络命名空间），并且容器不会分配自己的 IP 地址。

例如，如果您运行绑定到端口80host的容器并使用网络，则容器的应用程序可在主机IP地址的端口80使用。


练习host: https://docs.docker.com/network/network-tutorial-host/
练习brige: https://docs.docker.com/network/bridge/

### host

```
# 后台启动nginx 网络host
docker run --rm -d --network host --name my_nginx nginx
```


查看80端口
```
➜  bin sudo netstat -tulpn | grep :80
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      1984195/nginx: mast
tcp6       0      0 :::80                   :::*                    LISTEN      1984195/nginx: mast
➜  bin docker container stop my_nginx`
```

```
# 删除
docker container stop my_nginx
```




## brige
[文档](https://docs.docker.com/network/network-tutorial-standalone/)

```
➜  bin docker network ls
NETWORK ID     NAME         DRIVER    SCOPE
b280ef862068   alpine-net   bridge    local
5c1b7631264f   bridge       bridge    local
6ca6c8f47421   host         host      local
➜  bin
➜  bin docker network inspect bridge
[
    {
        "Name": "bridge",
        "Id": "5c1b7631264f2f6df04a972a34c5fd5d6c0ab892f1e29b8f31a781426606704e",
        "Created": "2021-09-10T19:07:38.963543289+08:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.17.0.0/16",
                    "Gateway": "172.17.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {},
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {}
    }
]
➜  bin docker network create --driver bridge alpine-net
➜  bin docker network inspect alpine-net
[
    {
        "Name": "alpine-net",
        "Id": "b280ef862068708b5e99143f5c587a6a050648d950b6b7953115e5143737dd45",
        "Created": "2021-10-19T18:27:20.618745587+08:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.18.0.0/16",
                    "Gateway": "172.18.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {},
        "Options": {},
        "Labels": {}
    }
]
➜  bin
```

网关:
* bridge: 172.17.0.1
* alpine-net: 172.18.0.1


启动容器:
* alpine-net:
	* alpine1:172.18.0.2
	* alpine2:172.18.0.3
	* alpine4:172.18.0.4
* bridge:
	* apline3:172.17.0.2
	* alpine4:172.17.0.3
```
docker run -dit --name alpine1 --network alpine-net alpine ash
docker run -dit --name alpine2 --network alpine-net alpine ash
docker run -dit --name alpine3 alpine ash
docker run -dit --name alpine4 --network alpine-net alpine ash
# 链接alpine4 到bridge网络空间
docker network connect bridge alpine4
```

查看网络:
```
➜  bin docker network inspect alpine-net
[
    {
        "Name": "alpine-net",
        "Id": "b280ef862068708b5e99143f5c587a6a050648d950b6b7953115e5143737dd45",
        "Created": "2021-10-19T18:27:20.618745587+08:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.18.0.0/16",
                    "Gateway": "172.18.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "012c718992268015b73cd38baa1a51e6071d48d87a57ef00c312ee298830c87c": {
                "Name": "alpine4",
                "EndpointID": "7c6adaa4ec499494a2e98c9d8f8f522784812b4ad6f84afe08e7badf3d4f9028",
                "MacAddress": "02:42:ac:12:00:04",
                "IPv4Address": "172.18.0.4/16",
                "IPv6Address": ""
            },
            "7b631ad8bedc1f874008a5f39b5f666e1c23d40885cf4815766b90f8a339d14f": {
                "Name": "alpine2",
                "EndpointID": "d2574dbbe351f2bc97fa55db629ff57d37d349033287f7d253cf263be32d5df5",
                "MacAddress": "02:42:ac:12:00:03",
                "IPv4Address": "172.18.0.3/16",
                "IPv6Address": ""
            },
            "edf6cc64c6986625957a57a66b84b271bb923ed7a64cf00b83ea672fcf889b16": {
                "Name": "alpine1",
                "EndpointID": "ca4caf56fa17194b509ab8d6339b74330dbbe2b00d4c49358e6974200f6d0ecf",
                "MacAddress": "02:42:ac:12:00:02",
                "IPv4Address": "172.18.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {}
    }
]
➜  bin
```

```
➜  bin docker network inspect bridge
[
    {
        "Name": "bridge",
        "Id": "5c1b7631264f2f6df04a972a34c5fd5d6c0ab892f1e29b8f31a781426606704e",
        "Created": "2021-09-10T19:07:38.963543289+08:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.17.0.0/16",
                    "Gateway": "172.17.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "03d84db3c9c1a2e161ecaa52e8dc36f889e5531be5136c3ff1718c32d6ed0afd": {
                "Name": "alpine4",
                "EndpointID": "cfedb61a43fc5eb62b8a56150d64c5972011127623d5b1d42e514b28aea46d73",
                "MacAddress": "02:42:ac:11:00:03",
                "IPv4Address": "172.17.0.3/16",
                "IPv6Address": ""
            },
            "a2d97da9b0e75325266f9645f53f123a5c52e38ee8ac3e3ab72b7f3b7612e282": {
                "Name": "alpine3",
                "EndpointID": "72bcf380b4703e712d613ce3911b83e0dc66da5f0ea57f71f949bd5b3a507856",
                "MacAddress": "02:42:ac:11:00:02",
                "IPv4Address": "172.17.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {}
    }
]
➜  bin
```


## 测试

alpine4: 可以同时ping 同两个网络
```
➜  bin docker container attach alpine4
/ # ping -c 2 172.18.0.1
PING 172.18.0.1 (172.18.0.1): 56 data bytes
64 bytes from 172.18.0.1: seq=0 ttl=64 time=0.125 ms
64 bytes from 172.18.0.1: seq=1 ttl=64 time=0.075 ms

--- 172.18.0.1 ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 0.075/0.100/0.125 ms
/ #
```