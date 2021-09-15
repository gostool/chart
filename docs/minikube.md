

# minikube

## [官网](https://minikube.sigs.k8s.io/docs/start/)

## 1.下载 Minikube
使用阿里镜像
[国内参考](https://www.jianshu.com/p/8b72a9d1dc6c)
[参考](https://zhuanlan.zhihu.com/p/407145134)
mac
```
curl -Lo minikube https://kubernetes.oss-cn-hangzhou.aliyuncs.com/minikube/releases/v1.20.0/minikube-darwin-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
```

Linux
```
curl -Lo minikube https://kubernetes.oss-cn-hangzhou.aliyuncs.com/minikube/releases/v1.20.0/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
```

## 2.启动
* 启动集群
* 启动dashboard

```
➜  k8s minikube version
minikube version: v1.20.0
commit: b017ea15ffbf8bcd6ce31e13ba16f59fd4091079
➜  k8s minikube start
😄  minikube v1.20.0 on Ubuntu 16.04
✨  Automatically selected the docker driver. Other choices: ssh, none
❗  docker is currently using the aufs storage driver, consider switching to overlay2 for better performance
👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
    > registry.cn-hangzhou.aliyun...: 358.10 MiB / 358.10 MiB  100.00% 5.08 MiB
    > registry.cn-hangzhou.aliyun...: 358.10 MiB / 358.10 MiB  100.00% 5.21 MiB
🔥  Creating docker container (CPUs=2, Memory=3900MB) ...
    > kubectl.sha256: 64 B / 64 B [--------------------------] 100.00% ? p/s 0s
    > kubelet.sha256: 64 B / 64 B [--------------------------] 100.00% ? p/s 0s
    > kubeadm.sha256: 64 B / 64 B [--------------------------] 100.00% ? p/s 0s
    > kubeadm: 37.40 MiB / 37.40 MiB [---------------] 100.00% 2.79 MiB p/s 14s
    > kubelet: 108.73 MiB / 108.73 MiB [-------------] 100.00% 7.35 MiB p/s 15s
    > kubectl: 38.37 MiB / 38.37 MiB [---------------] 100.00% 2.19 MiB p/s 18s

    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
🔎  Verifying Kubernetes components...
    ▪ Using image registry.cn-hangzhou.aliyuncs.com/google_containers/storage-provisioner:v5 (global image repository)
🌟  Enabled addons: default-storageclass, storage-provisioner
💡  kubectl not found. If you need it, try: 'minikube kubectl -- get pods -A'
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
➜  k8s
➜  k8s minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
➜  k8s
```
查看集群配置:
```
➜  ~ kubectl config view
apiVersion: v1
clusters:
- cluster:
    certificate-authority: /home/yunjing/.minikube/ca.crt
    extensions:
    - extension:
        last-update: Wed, 08 Sep 2021 10:26:25 CST
        provider: minikube.sigs.k8s.io
        version: v1.20.0
      name: cluster_info
    server: https://192.168.49.2:8443
  name: minikube
contexts:
- context:
    cluster: minikube
    extensions:
    - extension:
        last-update: Wed, 08 Sep 2021 10:26:25 CST
        provider: minikube.sigs.k8s.io
        version: v1.20.0
      name: context_info
    namespace: default
    user: minikube
  name: minikube
current-context: minikube
kind: Config
preferences: {}
users:
- name: minikube
  user:
    client-certificate: /home/yunjing/.minikube/profiles/minikube/client.crt
    client-key: /home/yunjing/.minikube/profiles/minikube/client.key
➜  ~
```


## 3.kuberctl
[kuberctl](https://minikube.sigs.k8s.io/docs/handbook/kubectl/)


```shell
ln -s $(which minikube) /usr/local/bin/kubectl
```

## 4.run
* echoserver
* deployment
* service
* pod

echo:
```
➜  ~ minikube kubectl -- create deployment hello-minikube --image=registry.cn-hangzhou.aliyuncs.com/google-containers/echoserver:1.4
deployment.apps/hello-minikube created
➜  ~
➜  ~ kubectl get pod
NAME                             READY   STATUS              RESTARTS   AGE
hello-minikube-5447d597b-rm6ts   0/1     ContainerCreating   0          19s
➜  ~
➜  ~ kubectl describe pod hello-minikube-5447d597b-rm6ts
Name:         hello-minikube-5447d597b-rm6ts
Namespace:    default
Priority:     0
Node:         minikube/192.168.49.2
Start Time:   Tue, 07 Sep 2021 17:20:02 +0800
Labels:       app=hello-minikube
              pod-template-hash=5447d597b
Annotations:  <none>
Status:       Running
IP:           172.17.0.3
IPs:
  IP:           172.17.0.3
Controlled By:  ReplicaSet/hello-minikube-5447d597b
Containers:
  echoserver:
    Container ID:   docker://4b0bfa522fa1f25ba24740eb7bc0bcaeba00b86d5832e59ca7bcd38c8f8ac3ab
    Image:          registry.cn-hangzhou.aliyuncs.com/google-containers/echoserver:1.4
    Image ID:       docker-pullable://registry.cn-hangzhou.aliyuncs.com/google-containers/echoserver@sha256:e192c933c53a9fdff8c85d91530895fa5f59a749c536abc5171c146cecdc5bdc
    Port:           <none>
    Host Port:      <none>
    State:          Running
      Started:      Tue, 07 Sep 2021 17:20:23 +0800
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-zk8h5 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  default-token-zk8h5:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-zk8h5
    Optional:    false
QoS Class:       BestEffort
Node-Selectors:  <none>
Tolerations:     node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                 node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  48s   default-scheduler  Successfully assigned default/hello-minikube-5447d597b-rm6ts to minikube
  Normal  Pulling    44s   kubelet            Pulling image "registry.cn-hangzhou.aliyuncs.com/google-containers/echoserver:1.4"
  Normal  Pulled     32s   kubelet            Successfully pulled image "registry.cn-hangzhou.aliyuncs.com/google-containers/echoserver:1.4" in 12.630009575s
  Normal  Created    28s   kubelet            Created container echoserver
  Normal  Started    27s   kubelet            Started container echoserver
➜  ~1
```
创建service:
```
➜  ~ minikube kubectl -- expose deployment hello-minikube --type=NodePort --port=8800
service/hello-minikube exposed
➜  ~ kubectl get pod,service
NAME                                 READY   STATUS    RESTARTS   AGE
pod/hello-minikube-5447d597b-rm6ts   1/1     Running   0          118s

NAME                     TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)          AGE
service/hello-minikube   NodePort    10.98.4.41   <none>        8800:30051/TCP   4s
service/kubernetes       ClusterIP   10.96.0.1    <none>        443/TCP          12m
➜  ~
```



nginx 创建/删除
```
➜  ~ kubectl run my-nginx --image=nginx --port=8800
➜  ~ kubectl get pod
NAME       READY   STATUS    RESTARTS   AGE
my-nginx   1/1     Running   0          3m40s
➜  ~ kubectl delete pods my-nginx
pod "my-nginx" deleted
➜  ~
➜  ~ kubectl get pod
NAME       READY   STATUS        RESTARTS   AGE
my-nginx   0/1     Terminating   0          4m24s
➜  ~
➜  ~ kubectl describe pod my-nginx
Name:                      my-nginx
Namespace:                 default
Priority:                  0
Node:                      minikube/192.168.49.2
Start Time:                Tue, 07 Sep 2021 17:11:58 +0800
Labels:                    run=my-nginx
Annotations:               <none>
Status:                    Terminating (lasts 2s)
Termination Grace Period:  30s
IP:                        172.17.0.3
IPs:
  IP:  172.17.0.3
Containers:
  my-nginx:
    Container ID:
    Image:          nginx
    Image ID:
    Port:           8800/TCP
    Host Port:      0/TCP
    State:          Waiting
      Reason:       ContainerCreating
    Last State:     Terminated
      Reason:       ContainerStatusUnknown
      Message:      The container could not be located when the pod was deleted.  The container used to be Running
      Exit Code:    137
      Started:      Mon, 01 Jan 0001 00:00:00 +0000
      Finished:     Mon, 01 Jan 0001 00:00:00 +0000
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-zk8h5 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  default-token-zk8h5:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-zk8h5
    Optional:    false
QoS Class:       BestEffort
Node-Selectors:  <none>
Tolerations:     node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                 node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  4m19s  default-scheduler  Successfully assigned default/my-nginx to minikube
  Normal  Pulling    4m15s  kubelet            Pulling image "nginx"
  Normal  Pulled     3m29s  kubelet            Successfully pulled image "nginx" in 45.74205135s
  Normal  Created    3m26s  kubelet            Created container my-nginx
  Normal  Started    3m25s  kubelet            Started container my-nginx
  Normal  Killing    32s    kubelet            Stopping container my-nginx
➜  ~
```

## dashboard
* 启动dashboard
```
nohup minikube dashboard --url=true >/dev/null 2>&1&
```

## proxy
* 代理请求到 8000端口

后台启动kubectl proxy
```
nohup kubectl proxy  --port=8000 --address='0.0.0.0' --accept-hosts='^.*'  >/dev/null 2>&1&
```
