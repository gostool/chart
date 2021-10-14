## install
* 源码
* [国外kubeadmin](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
* [国内阿里镜像 kubeadmin](https://www.cnblogs.com/xiao987334176/p/11317844.html)


```
➜  apps cat /etc/apt/sources.list.d/kubernetes.list
deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main
```
修改阿里源:
```
➜  apps cat /etc/apt/sources.list.d/kubernetes.list
deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://mirrors.aliyun.com/kubernetes/apt/  kubernetes-xenial main
➜  apps
```

开始安装:
```
sudo apt update
export VERSION=1.20.2-00
sudo apt install -y kubelet=${VERSION} kubeadm=${VERSION} kubectl=${VERSION}
sudo apt-mark hold kubelet=${VERSION} kubeadm=${VERSION} kubectl=${VERSION}

```

安装日志:
```
➜  apps sudo apt update
Get:1 https://mirrors.aliyun.com/kubernetes/apt kubernetes-xenial InRelease [9383 B]
Hit:2 http://mirrors.tencentyun.com/ubuntu bionic InRelease
Hit:3 http://mirrors.tencentyun.com/ubuntu bionic-security InRelease
Hit:4 http://mirrors.tencentyun.com/ubuntu bionic-updates InRelease
Hit:5 https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu bionic InRelease
Hit:6 https://download.docker.com/linux/ubuntu bionic InRelease
Ign:7 https://mirrors.aliyun.com/kubernetes/apt kubernetes-xenial/main amd64 Packages
Get:7 https://mirrors.aliyun.com/kubernetes/apt kubernetes-xenial/main amd64 Packages [50.0 kB]
Fetched 59.4 kB in 3s (19.6 kB/s)
debug2: channel 0: window 999370 sent adjust 49206
Reading package lists... Done
Building dependency tree
Need to get 68.6 MB of archives.
After this operation, 293 MB of additional disk space will be used.
Get:1 http://mirrors.tencentyun.com/ubuntu bionic/main amd64 conntrack amd64 1:1.4.4+snapshot20161117-6ubuntu2 [30.6 kB]
Get:2 http://mirrors.tencentyun.com/ubuntu bionic/main amd64 socat amd64 1.7.3.2-2ubuntu2 [342 kB]
Get:3 https://mirrors.aliyun.com/kubernetes/apt kubernetes-xenial/main amd64 cri-tools amd64 1.13.0-01 [8775 kB]
Get:4 https://mirrors.aliyun.com/kubernetes/apt kubernetes-xenial/main amd64 kubernetes-cni amd64 0.8.7-00 [25.0 MB]
Get:5 https://mirrors.aliyun.com/kubernetes/apt kubernetes-xenial/main amd64 kubelet amd64 1.20.2-00 [18.9 MB]
Get:6 https://mirrors.aliyun.com/kubernetes/apt kubernetes-xenial/main amd64 kubectl amd64 1.20.2-00 [7940 kB]
Get:7 https://mirrors.aliyun.com/kubernetes/apt kubernetes-xenial/main amd64 kubeadm amd64 1.20.2-00 [7706 kB]
Fetched 68.6 MB in 7s (10.2 MB/s)
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
	LANGUAGE = (unset),
	LC_ALL = (unset),
	LC_CTYPE = "zh_CN.UTF-8",
	LANG = "en_US.utf8"
    are supported and installed on your system.
perl: warning: Falling back to a fallback locale ("en_US.utf8").
locale: Cannot set LC_CTYPE to default locale: No such file or directory
locale: Cannot set LC_ALL to default locale: No such file or directory
Selecting previously unselected package conntrack.
(Reading database ... 82166 files and directories currently installed.)
Preparing to unpack .../0-conntrack_1%3a1.4.4+snapshot20161117-6ubuntu2_amd64.deb ...
Unpacking conntrack (1:1.4.4+snapshot20161117-6ubuntu2) ...
Selecting previously unselected package cri-tools.
Preparing to unpack .../1-cri-tools_1.13.0-01_amd64.deb ...
Unpacking cri-tools (1.13.0-01) ...
Selecting previously unselected package kubernetes-cni.
Preparing to unpack .../2-kubernetes-cni_0.8.7-00_amd64.deb ...
Unpacking kubernetes-cni (0.8.7-00) ...
Selecting previously unselected package socat.
Preparing to unpack .../3-socat_1.7.3.2-2ubuntu2_amd64.deb ...
Unpacking socat (1.7.3.2-2ubuntu2) ...
Selecting previously unselected package kubelet.
Preparing to unpack .../4-kubelet_1.20.2-00_amd64.deb ...
Unpacking kubelet (1.20.2-00) ...
Selecting previously unselected package kubectl.
Preparing to unpack .../5-kubectl_1.20.2-00_amd64.deb ...
Unpacking kubectl (1.20.2-00) ...
Selecting previously unselected package kubeadm.
Preparing to unpack .../6-kubeadm_1.20.2-00_amd64.deb ...
Unpacking kubeadm (1.20.2-00) ...
Setting up conntrack (1:1.4.4+snapshot20161117-6ubuntu2) ...
Setting up kubernetes-cni (0.8.7-00) ...
Setting up cri-tools (1.13.0-01) ...
Setting up socat (1.7.3.2-2ubuntu2) ...
Setting up kubelet (1.20.2-00) ...
Created symlink /etc/systemd/system/multi-user.target.wants/kubelet.service → /lib/systemd/system/kubelet.service.
Setting up kubectl (1.20.2-00) ...
Setting up kubeadm (1.20.2-00) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
➜  apps sudo apt-mark hold kubelet=${VERSION} kubeadm=${VERSION} kubectl=${VERSION}
kubelet set on hold.
kubeadm set on hold.
kubectl set on hold.
➜  apps
```


kubeadm:
```
➜  apps kubeadm version
kubeadm version: &version.Info{Major:"1", Minor:"20", GitVersion:"v1.20.2", GitCommit:"faecb196815e248d3ecfb03c680a4507229c2a56", GitTreeState:"clean", BuildDate:"2021-01-13T13:25:59Z", GoVersion:"go1.15.5", Compiler:"gc", Platform:"linux/amd64"}
➜  apps
```


[参考](https://www.cnblogs.com/xiao987334176/p/11317844.html)


## 编译
* 本地编译
* docker编译，需要能访问外网

编译cmd/kubelet:
```
➜  k8s.io cd kubernetes
➜  kubernetes make clean
➜  kubernetes KUBE_BUILD_PLATFORMS=linux/amd64 make all WHAT=cmd/kubelet GOFLAGS=-v GOGCFLAGS="-N -l"
k8s.io/kubernetes/vendor/github.com/spf13/pflag
k8s.io/kubernetes/hack/make-rules/helpers/go2make
+++ [1014 18:16:08] Building go targets for linux/amd64:
    ./vendor/k8s.io/code-generator/cmd/prerelease-lifecycle-gen
k8s.io/kubernetes/vendor/golang.org/x/mod/semver"
... 时间较长，耐心等待
```

```
➜  kubernetes pwd
/home/ubuntu/go-dev/src/k8s.io/kubernetes
➜  kubernetes tree _output/bin
_output/bin
|-- conversion-gen
|-- deepcopy-gen
|-- defaulter-gen
|-- go2make
|-- go-bindata
|-- kubelet				# 编译文件
|-- openapi-gen
`-- prerelease-lifecycle-gen

0 directories, 8 files
➜  kubernetes
```


