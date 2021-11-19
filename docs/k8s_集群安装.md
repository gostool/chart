### 查看ubuntu版本号

```yml
lsb_release -a
```

### 在Ubuntu上添加阿里云软件源
```yml
https://help.aliyun.com/document_detail/120851.html?spm=5176.21213303.J_6704733920.7.37d33edaSIcLbu&scm=20140722.S_help%40%40%E6%96%87%E6%A1%A3%40%40120851.S_0%2Bos.ID_120851-RL_ubuntu%20%E5%A6%82%E4%BD%95%E6%9B%B4%E6%8D%A2%E8%BD%AF%E4%BB%B6%E6%BA%90-OR_main-V_2-P0_0
https://developer.aliyun.com/mirror/ubuntu?spm=a2c6h.13651102.0.0.3e221b11PMxpIB
```

### 安装docker
```yml
1. Uninstall old versionsd
sudo apt-get remove docker docker-engine docker.io containerd runc

2. If you do not need to save your existing data, and want to start with a clean installation, refer to the uninstall Docker Engine section
2.1. Uninstall the Docker Engine, CLI, and Containerd packages:
 sudo apt-get purge docker-ce docker-ce-cli containerd.io
2.2. Images, containers, volumes, or customized configuration files on your host are not automatically removed. To delete all images, containers, and volumes:
 sudo rm -rf /var/lib/docker
 sudo rm -rf /var/lib/containerd

3.install docker
 https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository
```

### 安装k8s关键组件
```
1.apt-get update
2.apt-get install -y kubectl kubeadm kubelet
```

### 初始化master node
```shell
kubeadm init --pod-network-cidr=10.244.0.0/16
```

### 初始化master遇到的问题以及解决方法

```
1./etc/kubernetes/manifests/kube-apiserver.yaml already exists
解决方法：rm -rf /etc/kubernetes/manifests
```

2. 无法访问k8s.gcr.io,镜像拉不下来
解决方法1：
```
(venv) ➜  ~ kubeadm config images list
k8s.gcr.io/kube-apiserver:v1.22.3
k8s.gcr.io/kube-controller-manager:v1.22.3
k8s.gcr.io/kube-scheduler:v1.22.3
k8s.gcr.io/kube-proxy:v1.22.3
k8s.gcr.io/pause:3.5
k8s.gcr.io/etcd:3.5.0-0
k8s.gcr.io/coredns/coredns:v1.8.4
(venv) ➜  ~ docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/kube-apiserver:v1.22.3
(venv) ➜  ~ docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/kube-apiserver:v1.22.3 k8s.gcr.io/kube-apiserver:v1.22.3 
```
解决方法2: 通过配置文件修改拉取镜像的仓库：
```
(venv) ➜  config kubeadm config print init-defaults  >kubeadm.conf
(venv) ➜  config cat kubeadm.conf 
apiVersion: kubeadm.k8s.io/v1beta3
bootstrapTokens:
- groups:
  - system:bootstrappers:kubeadm:default-node-token
  token: abcdef.0123456789abcdef
  ttl: 24h0m0s
  usages:
  - signing(venv) ➜
  - authentication
kind: InitConfiguration
localAPIEndpoint:
  advertiseAddress: 1.2.3.4
  bindPort: 6443
nodeRegistration:
  criSocket: /var/run/dockershim.sock
  imagePullPolicy: IfNotPresent
  name: node
  taints: null
---
apiServer:
  timeoutForControlPlane: 4m0s
apiVersion: kubeadm.k8s.io/v1beta3
certificatesDir: /etc/kubernetes/pki
clusterName: kubernetes
controllerManager: {}
dns: {}
etcd:
  local:
    dataDir: /var/lib/etcd
imageRepository: registry.cn-hangzhou.aliyuncs.com/google_containers
kind: ClusterConfiguration
kubernetesVersion: 1.22.0
networking:
  dnsDomain: cluster.local
  serviceSubnet: 10.96.0.0/12
scheduler: {}
(venv) ➜  config kubeadm config images list --config kubeadm.conf
registry.cn-hangzhou.aliyuncs.com/google_containers/kube-apiserver:v1.22.0
registry.cn-hangzhou.aliyuncs.com/google_containers/kube-controller-manager:v1.22.0
registry.cn-hangzhou.aliyuncs.com/google_containers/kube-scheduler:v1.22.0
registry.cn-hangzhou.aliyuncs.com/google_containers/kube-proxy:v1.22.0
registry.cn-hangzhou.aliyuncs.com/google_containers/pause:3.5
registry.cn-hangzhou.aliyuncs.com/google_containers/etcd:3.5.0-0
registry.cn-hangzhou.aliyuncs.com/google_containers/coredns:v1.8.4
```
执行kubeadm init需要加上 --config kubeadm.conf



3.kubelet无法启动的问题:原因是docker的驱动和kubelet驱动不一致造成的
```
(venv) ➜  ~ kubeadm init --kubernetes-version=1.22.3 --pod-network-cidr=10.244.0.0/16
查看kubelet日志
(venv) ➜ journalctl -xeu kubelet
```yml
Nov 16 21:44:19 master-node kubelet[3960643]: Flag --network-plugin has been deprecated, will be removed along with dockershim.
Nov 16 21:44:19 master-node kubelet[3960643]: Flag --network-plugin has been deprecated, will be removed along with dockershim.
Nov 16 21:44:19 master-node kubelet[3960643]: I1116 21:44:19.681095 3960643 server.go:440] "Kubelet version" kubeletVersion="v1.22.3"
Nov 16 21:44:19 master-node kubelet[3960643]: I1116 21:44:19.681800 3960643 server.go:868] "Client rotation is on, will bootstrap in background"
Nov 16 21:44:19 master-node kubelet[3960643]: I1116 21:44:19.684825 3960643 certificate_store.go:130] Loading cert/key pair from "/var/lib/kubelet/pki/kubelet-client-current.pem".
Nov 16 21:44:19 master-node kubelet[3960643]: I1116 21:44:19.686071 3960643 dynamic_cafile_content.go:155] "Starting controller" name="client-ca-bundle::/etc/kubernetes/pki/ca.crt"
Nov 16 21:44:19 master-node kubelet[3960643]: I1116 21:44:19.768093 3960643 server.go:687] "--cgroups-per-qos enabled, but --cgroup-root was not specified.  defaulting to /"
Nov 16 21:44:19 master-node kubelet[3960643]: I1116 21:44:19.768389 3960643 container_manager_linux.go:280] "Container manager verified user specified cgroup-root exists" cgroupRoot=[]
Nov 16 21:44:19 master-node kubelet[3960643]: I1116 21:44:19.768521 3960643 container_manager_linux.go:285] "Creating Container Manager object based on Node Config" nodeConfig={RuntimeCgroupsName: SystemCgroupsName: KubeletCgroupsName: ContainerRuntime:docker CgroupsPerQOS:true CgroupRoot:/ CgroupDriver:systemd KubeletRootDir:/var/lib/ku>
Nov 16 21:44:19 master-node kubelet[3960643]: I1116 21:44:19.768637 3960643 topology_manager.go:133] "Creating topology manager with policy per scope" topologyPolicyName="none" topologyScopeName="container"
Nov 16 21:44:19 master-node kubelet[3960643]: I1116 21:44:19.768658 3960643 container_manager_linux.go:320] "Creating device plugin manager" devicePluginEnabled=true
Nov 16 21:44:19 master-node kubelet[3960643]: I1116 21:44:19.768705 3960643 state_mem.go:36] "Initialized new in-memory state store"
Nov 16 21:44:19 master-node kubelet[3960643]: I1116 21:44:19.768782 3960643 kubelet.go:314] "Using dockershim is deprecated, please consider using a full-fledged CRI implementation"
Nov 16 21:44:19 master-node kubelet[3960643]: I1116 21:44:19.768821 3960643 client.go:78] "Connecting to docker on the dockerEndpoint" endpoint="unix:///var/run/docker.sock"
Nov 16 21:44:19 master-node kubelet[3960643]: I1116 21:44:19.768844 3960643 client.go:97] "Start docker client with request timeout" timeout="2m0s"
Nov 16 21:44:19 master-node kubelet[3960643]: I1116 21:44:19.778679 3960643 docker_service.go:566] "Hairpin mode is set but kubenet is not enabled, falling back to HairpinVeth" hairpinMode=promiscuous-bridge
Nov 16 21:44:19 master-node kubelet[3960643]: I1116 21:44:19.778710 3960643 docker_service.go:242] "Hairpin mode is set" hairpinMode=hairpin-veth
Nov 16 21:44:19 master-node kubelet[3960643]: I1116 21:44:19.778856 3960643 cni.go:239] "Unable to update cni config" err="no networks found in /etc/cni/net.d"
Nov 16 21:44:19 master-node kubelet[3960643]: I1116 21:44:19.781353 3960643 cni.go:239] "Unable to update cni config" err="no networks found in /etc/cni/net.d"
Nov 16 21:44:19 master-node kubelet[3960643]: I1116 21:44:19.781491 3960643 cni.go:239] "Unable to update cni config" err="no networks found in /etc/cni/net.d"
Nov 16 21:44:19 master-node kubelet[3960643]: I1116 21:44:19.781541 3960643 docker_service.go:257] "Docker cri networking managed by the network plugin" networkPluginName="cni"
Nov 16 21:44:19 master-node kubelet[3960643]: I1116 21:44:19.791460 3960643 docker_service.go:264] "Docker Info" dockerInfo=&{ID:QCRC:2DJR:L4EA:57BX:XTHO:3WNC:Q6HH:B3OK:S23C:PL4K:476B:L2XZ Containers:0 ContainersRunning:0 ContainersPaused:0 ContainersStopped:0 Images:7 Driver:overlay2 DriverStatus:[[Backing Filesystem extfs] [Supports d_>
Nov 16 21:44:19 master-node kubelet[3960643]: E1116 21:44:19.791512 3960643 server.go:294] "Failed to run kubelet" err="failed to run Kubelet: misconfiguration: kubelet cgroup driver: \"systemd\" is different from docker cgroup driver: \"cgroupfs\""
Nov 16 21:44:19 master-node systemd[1]: kubelet.service: Main process exited, code=exited, status=1/FAILURE
```

[配置cgroups的驱动](https://kubernetes.io/zh/docs/tasks/administer-cluster/kubeadm/configure-cgroup-driver/)

解决方法： 
```sh
(venv) ➜  config cat /etc/systemd/system/kubelet.service.d/10-kubeadm.conf 
# Note: This dropin only works with kubeadm and kubelet v1.11+
[Service]
Environment="KUBELET_KUBECONFIG_ARGS=--bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf --kubeconfig=/etc/kubernetes/kubelet.conf"
Environment="KUBELET_CONFIG_ARGS=--config=/var/lib/kubelet/config.yaml"
# This is a file that "kubeadm init" and "kubeadm join" generates at runtime, populating the KUBELET_KUBEADM_ARGS variable dynamically
#EnvironmentFile=-/var/lib/kubelet/kubeadm-flags.env
EnvironmentFile=-/root/apps/config/kubeadm-flags.env
# This is a file that the user can use for overrides of the kubelet args as a last resort. Preferably, the user should use
# the .NodeRegistration.KubeletExtraArgs object in the configuration files instead. KUBELET_EXTRA_ARGS should be sourced from this file.
EnvironmentFile=-/etc/default/kubelet
ExecStart=
ExecStart=/usr/bin/kubelet $KUBELET_KUBECONFIG_ARGS $KUBELET_CONFIG_ARGS $KUBELET_KUBEADM_ARGS $KUBELET_EXTRA_ARGS
(venv) ➜  config 
```


```
(venv) ➜  config cat /var/lib/kubelet/kubeadm-flags.env
KUBELET_KUBEADM_ARGS="--network-plugin=cni --pod-infra-container-image=k8s.gcr.io/pause:3.5"
(venv) ➜  config cat /root/apps/config/kubeadm-flags.env
KUBELET_KUBEADM_ARGS="--cgroup-driver=cgroupfs --network-plugin=cni --pod-infra-container-image=k8s.gcr.io/pause:3.5"
(venv) ➜  config 
```

```yml
(venv) ➜  config vi /etc/systemd/system/kubelet.service.d
(venv) ➜  config systemctl status kubelet
Warning: The unit file, source configuration file or drop-ins of kubelet.service changed on disk. Run 'systemctl daemon-reload' to reload units.
● kubelet.service - kubelet: The Kubernetes Node Agent
     Loaded: loaded (/lib/systemd/system/kubelet.service; enabled; vendor preset: enabled)
    Drop-In: /etc/systemd/system/kubelet.service.d
             └─10-kubeadm.conf
     Active: activating (auto-restart) (Result: exit-code) since Tue 2021-11-16 23:06:12 CST; 1s ago
       Docs: https://kubernetes.io/docs/home/
    Process: 4010751 ExecStart=/usr/bin/kubelet $KUBELET_KUBECONFIG_ARGS $KUBELET_CONFIG_ARGS $KUBELET_KUBEADM_ARGS $KUBELET_EXTRA_ARGS (code=exited, status=1/FAILURE)
   Main PID: 4010751 (code=exited, status=1/FAILURE)
(venv) ➜  config systemctl daemon-reload
(venv) ➜  config systemctl status kubelet
● kubelet.service - kubelet: The Kubernetes Node Agent
     Loaded: loaded (/lib/systemd/system/kubelet.service; enabled; vendor preset: enabled)
    Drop-In: /etc/systemd/system/kubelet.service.d
             └─10-kubeadm.conf
     Active: active (running) since Tue 2021-11-16 23:06:32 CST; 4s ago
       Docs: https://kubernetes.io/docs/home/
   Main PID: 4010976 (kubelet)
      Tasks: 13 (limit: 4654)
     Memory: 32.8M
     CGroup: /system.slice/kubelet.service
             └─4010976 /usr/bin/kubelet --bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf --kubeconfig=/etc/kubernetes/kubelet.conf --config=/var/lib/kubelet/config.yaml --cgroup-driver=cgroupfs --network-plugin=cni>

Nov 16 23:06:36 master-node kubelet[4010976]: E1116 23:06:36.029918 4010976 kubelet.go:2412] "Error getting node" err="node \"master-node\" not found"
Nov 16 23:06:36 master-node kubelet[4010976]: E1116 23:06:36.130638 4010976 kubelet.go:2412] "Error getting node" err="node \"master-node\" not found"
Nov 16 23:06:36 master-node kubelet[4010976]: E1116 23:06:36.231394 4010976 kubelet.go:2412] "Error getting node" err="node \"master-node\" not found"
Nov 16 23:06:36 master-node kubelet[4010976]: E1116 23:06:36.332223 4010976 kubelet.go:2412] "Error getting node" err="node \"master-node\" not found"
Nov 16 23:06:36 master-node kubelet[4010976]: E1116 23:06:36.432353 4010976 kubelet.go:2412] "Error getting node" err="node \"master-node\" not found"
Nov 16 23:06:36 master-node kubelet[4010976]: E1116 23:06:36.533269 4010976 kubelet.go:2412] "Error getting node" err="node \"master-node\" not found"
Nov 16 23:06:36 master-node kubelet[4010976]: E1116 23:06:36.633694 4010976 kubelet.go:2412] "Error getting node" err="node \"master-node\" not found"
Nov 16 23:06:36 master-node kubelet[4010976]: E1116 23:06:36.734472 4010976 kubelet.go:2412] "Error getting node" err="node \"master-node\" not found"
Nov 16 23:06:36 master-node kubelet[4010976]: E1116 23:06:36.835369 4010976 kubelet.go:2412] "Error getting node" err="node \"master-node\" not found"
Nov 16 23:06:36 master-node kubelet[4010976]: E1116 23:06:36.937934 4010976 kubelet.go:2412] "Error getting node" err="node \"master-node\" not found"
(venv) ➜  config
```

### kubeadmin 启动 
```yml
env) ➜  config kubeadm init --kubernetes-version=1.22.3 --pod-network-cidr=10.244.0.0/16 
[init] Using Kubernetes version: v1.22.3
[preflight] Running pre-flight checks
[preflight] Pulling images required for setting up a Kubernetes cluster
[preflight] This might take a minute or two, depending on the speed of your internet connection
[preflight] You can also perform this action in beforehand using 'kubeadm config images pull'
[certs] Using certificateDir folder "/etc/kubernetes/pki"
[certs] Generating "ca" certificate and key
[certs] Generating "apiserver" certificate and key
[certs] apiserver serving cert is signed for DNS names [kubernetes kubernetes.default kubernetes.default.svc kubernetes.default.svc.cluster.local master-node] and IPs [10.96.0.1 172.16.181.180]
[certs] Generating "apiserver-kubelet-client" certificate and key
[certs] Generating "front-proxy-ca" certificate and key
[certs] Generating "front-proxy-client" certificate and key
[certs] Generating "etcd/ca" certificate and key
[certs] Generating "etcd/server" certificate and key
[certs] etcd/server serving cert is signed for DNS names [localhost master-node] and IPs [172.16.181.180 127.0.0.1 ::1]
[certs] Generating "etcd/peer" certificate and key
[certs] etcd/peer serving cert is signed for DNS names [localhost master-node] and IPs [172.16.181.180 127.0.0.1 ::1]
[certs] Generating "etcd/healthcheck-client" certificate and key
[certs] Generating "apiserver-etcd-client" certificate and key
[certs] Generating "sa" key and public key
[kubeconfig] Using kubeconfig folder "/etc/kubernetes"
[kubeconfig] Writing "admin.conf" kubeconfig file
[kubeconfig] Writing "kubelet.conf" kubeconfig file
[kubeconfig] Writing "controller-manager.conf" kubeconfig file
[kubeconfig] Writing "scheduler.conf" kubeconfig file
[kubelet-start] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[kubelet-start] Starting the kubelet
[control-plane] Using manifest folder "/etc/kubernetes/manifests"
[control-plane] Creating static Pod manifest for "kube-apiserver"
[control-plane] Creating static Pod manifest for "kube-controller-manager"
[control-plane] Creating static Pod manifest for "kube-scheduler"
[etcd] Creating static Pod manifest for local etcd in "/etc/kubernetes/manifests"
[wait-control-plane] Waiting for the kubelet to boot up the control plane as static Pods from directory "/etc/kubernetes/manifests". This can take up to 4m0s
[apiclient] All control plane components are healthy after 10.002778 seconds
[upload-config] Storing the configuration used in ConfigMap "kubeadm-config" in the "kube-system" Namespace
[kubelet] Creating a ConfigMap "kubelet-config-1.22" in namespace kube-system with the configuration for the kubelets in the cluster
[upload-certs] Skipping phase. Please see --upload-certs
[mark-control-plane] Marking the node master-node as control-plane by adding the labels: [node-role.kubernetes.io/master(deprecated) node-role.kubernetes.io/control-plane node.kubernetes.io/exclude-from-external-load-balancers]
[mark-control-plane] Marking the node master-node as control-plane by adding the taints [node-role.kubernetes.io/master:NoSchedule]
[bootstrap-token] Using token: nychyl.bcrlo4v9j3h4su48
[bootstrap-token] Configuring bootstrap tokens, cluster-info ConfigMap, RBAC Roles
[bootstrap-token] configured RBAC rules to allow Node Bootstrap tokens to get nodes
[bootstrap-token] configured RBAC rules to allow Node Bootstrap tokens to post CSRs in order for nodes to get long term certificate credentials
[bootstrap-token] configured RBAC rules to allow the csrapprover controller automatically approve CSRs from a Node Bootstrap Token
[bootstrap-token] configured RBAC rules to allow certificate rotation for all node client certificates in the cluster
[bootstrap-token] Creating the "cluster-info" ConfigMap in the "kube-public" namespace
[kubelet-finalize] Updating "/etc/kubernetes/kubelet.conf" to point to a rotatable kubelet client certificate and key
[addons] Applied essential addon: CoreDNS
[addons] Applied essential addon: kube-proxy

Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 172.16.181.180:6443 --token nychyl.bcrlo4v9j3h4su48 \
	--discovery-token-ca-cert-hash sha256:25de9d76a53cd75bb75aec2c08044dc5f3ee2f6ef0172965847969888c84675e 
(venv) ➜  config 

```
### master node 上运行
```yml
(venv) ➜  ~ kubectl get nodes
NAME          STATUS     ROLES                  AGE     VERSION
master-node   NotReady   control-plane,master   17h     v1.22.3
worker01      NotReady   <none>                 2m16s   v1.22.3


(venv) ➜  ~ kubectl get pod --namespace=kube-system
NAME                                  READY   STATUS              RESTARTS   AGE
coredns-78fcd69978-czndn              0/1     Pending             0          17h
coredns-78fcd69978-hj2qq              0/1     Pending             0          17h
etcd-master-node                      1/1     Running             3          17h
kube-apiserver-master-node            1/1     Running             3          17h
kube-controller-manager-master-node   1/1     Running             3          17h
kube-proxy-29jmt                      1/1     Running             0          17h
kube-proxy-8lprx                      0/1     ContainerCreating   0          2m59s
kube-scheduler-master-node            1/1     Running             3          17h
(venv) ➜  ~ 
(venv) ➜  ~ 
(venv) ➜  ~ kubectl describe pod kube-proxy-8lprx --namespace=kube-system 
Name:                 kube-proxy-8lprx
Namespace:            kube-system
Priority:             2000001000
Priority Class Name:  system-node-critical
Node:                 worker01/172.16.181.181
Start Time:           Wed, 17 Nov 2021 16:46:46 +0800
Labels:               controller-revision-hash=674d79d6f9
                      k8s-app=kube-proxy
                      pod-template-generation=1
Annotations:          <none>
Status:               Pending
IP:                   172.16.181.181
IPs:
  IP:           172.16.181.181
Controlled By:  DaemonSet/kube-proxy
Containers:
  kube-proxy:
    Container ID:  
    Image:         k8s.gcr.io/kube-proxy:v1.22.3
    Image ID:      
    Port:          <none>
    Host Port:     <none>
    Command:
      /usr/local/bin/kube-proxy
      --config=/var/lib/kube-proxy/config.conf
      --hostname-override=$(NODE_NAME)
    State:          Waiting
      Reason:       ContainerCreating
    Ready:          False
    Restart Count:  0
    Environment:
      NODE_NAME:   (v1:spec.nodeName)
    Mounts:
      /lib/modules from lib-modules (ro)
      /run/xtables.lock from xtables-lock (rw)
      /var/lib/kube-proxy from kube-proxy (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-vfxw8 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-proxy:
    Type:      ConfigMap (a volume populated by a ConfigMap)
    Name:      kube-proxy
    Optional:  false
  xtables-lock:
    Type:          HostPath (bare host directory volume)
    Path:          /run/xtables.lock
    HostPathType:  FileOrCreate
  lib-modules:
    Type:          HostPath (bare host directory volume)
    Path:          /lib/modules
    HostPathType:  
  kube-api-access-vfxw8:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              kubernetes.io/os=linux
Tolerations:                 op=Exists
                             node.kubernetes.io/disk-pressure:NoSchedule op=Exists
                             node.kubernetes.io/memory-pressure:NoSchedule op=Exists
                             node.kubernetes.io/network-unavailable:NoSchedule op=Exists
                             node.kubernetes.io/not-ready:NoExecute op=Exists
                             node.kubernetes.io/pid-pressure:NoSchedule op=Exists
                             node.kubernetes.io/unreachable:NoExecute op=Exists
                             node.kubernetes.io/unschedulable:NoSchedule op=Exists
Events:
  Type     Reason                  Age                   From               Message
  ----     ------                  ----                  ----               -------
  Normal   Scheduled               5m6s                  default-scheduler  Successfully assigned kube-system/kube-proxy-8lprx to worker01
  Warning  FailedCreatePodSandBox  15s (x11 over 4m49s)  kubelet            Failed to create pod sandbox: rpc error: code = Unknown desc = failed pulling image "k8s.gcr.io/pause:3.5": Error response from daemon: Get "https://k8s.gcr.io/v2/": net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)
(venv) ➜  ~ 

(venv) ➜  ~ kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
Warning: policy/v1beta1 PodSecurityPolicy is deprecated in v1.21+, unavailable in v1.25+
podsecuritypolicy.policy/psp.flannel.unprivileged created
clusterrole.rbac.authorization.k8s.io/flannel created
clusterrolebinding.rbac.authorization.k8s.io/flannel created
serviceaccount/flannel created
configmap/kube-flannel-cfg created
daemonset.apps/kube-flannel-ds created
```

### k8s集群搭建完成
```yml
(venv) ➜  ~ kubectl get pod --namespace=kube-system                              
NAME                                  READY   STATUS    RESTARTS   AGE
coredns-78fcd69978-czndn              1/1     Running   0          18h
coredns-78fcd69978-hj2qq              1/1     Running   0          18h
etcd-master-node                      1/1     Running   3          18h
kube-apiserver-master-node            1/1     Running   3          18h
kube-controller-manager-master-node   1/1     Running   3          18h
kube-flannel-ds-tw6j5                 1/1     Running   0          8m14s
kube-flannel-ds-w2dfl                 1/1     Running   0          8m14s
kube-proxy-29jmt                      1/1     Running   0          18h
kube-proxy-8lprx                      1/1     Running   0          35m
kube-scheduler-master-node            1/1     Running   3          18h
(venv) ➜  ~ kubectl get nodes
NAME          STATUS   ROLES                  AGE   VERSION
master-node   Ready    control-plane,master   18h   v1.22.3
worker01      Ready    <none>                 36m   v1.22.3
(venv) ➜  ~ 
```
