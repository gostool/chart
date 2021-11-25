## ip 地址分配
* eth0: 10.0.4.8
* docker0: 172.17.0.1
* 192.168.49.1: minikube

```
➜  discovery ip addr
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 52:54:00:64:f3:7f brd ff:ff:ff:ff:ff:ff
    inet 10.0.4.8/22 brd 10.0.7.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::5054:ff:fe64:f37f/64 scope link
       valid_lft forever preferred_lft forever
3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default
    link/ether 02:42:8d:27:46:88 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:8dff:fe27:4688/64 scope link
       valid_lft forever preferred_lft forever
31: br-c0e233ad035d: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 02:42:ec:cd:ef:75 brd ff:ff:ff:ff:ff:ff
    inet 192.168.49.1/24 brd 192.168.49.255 scope global br-c0e233ad035d
       valid_lft forever preferred_lft forever
    inet6 fe80::42:ecff:fecd:ef75/64 scope link
       valid_lft forever preferred_lft forever
35: vethe9eed05@if34: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c0e233ad035d state UP group default
    link/ether e2:72:7e:d0:f5:b2 brd ff:ff:ff:ff:ff:ff link-netnsid 1
    inet6 fe80::e072:7eff:fed0:f5b2/64 scope link
       valid_lft forever preferred_lft forever
➜  discovery
```

docker network:
* host: localhost
* bridge: 172.17.0.1
* minikube: 192.168.49.1

```
➜  discovery docker network ls
NETWORK ID     NAME       DRIVER    SCOPE
5c1b7631264f   bridge     bridge    local
6ca6c8f47421   host       host      local
c0e233ad035d   minikube   bridge    local
d7fdc8dc51f4   none       null      local
➜  discovery
```

```
➜  discovery docker network inspect bridge
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
➜  discovery
```


```
➜  discovery docker network inspect minikube
[
    {
        "Name": "minikube",
        "Id": "c0e233ad035d186c7f2c580c512ff791e06229a4dabac0404e3114c039754fc7",
        "Created": "2021-09-10T23:33:46.204306993+08:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "192.168.49.0/24",
                    "Gateway": "192.168.49.1"
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
            "7c7cfd1ae0b1105b025169db776a1d87442022ed8d7514563509d9015493f1aa": {
                "Name": "minikube",
                "EndpointID": "56e1253dbfd8730ba8eadc388f089b90613a5b82c83cc03df5901fce47e59ec1",
                "MacAddress": "02:42:c0:a8:31:02",
                "IPv4Address": "192.168.49.2/24",
                "IPv6Address": ""
            }
        },
        "Options": {
            "--icc": "",
            "--ip-masq": "",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {
            "created_by.minikube.sigs.k8s.io": "true"
        }
    }
]
```

### pod

Pod 的IP地址是Docker Daemon根据docker0网桥的IP地址段分配的.

Service:
* Cluster IP: kubernets系统中的虚拟IP地址, 有系统动态分配

由于service对象在cluster IP Range池中分配的到的IP只能在内部访问，
所以其他pod都可以无障碍的访问到它. 


