## 


## linux 容器


lower: 镜像层
workdir/upper: 容器rw层
mergedir: 统一视图


```
(venv) ➜  ~ docker run -d --name busybox busybox top
d7972b05a3f8465349ca6d7867dc1466a7f534749e82df5da07a547a2bbf4d27
(venv) ➜  ~
```

docker inspect busybox

```
(venv) ➜  ~ docker inspect buxyboxy
[
    {
        "Id": "d7972b05a3f8465349ca6d7867dc1466a7f534749e82df5da07a547a2bbf4d27",
        "Created": "2021-11-29T08:13:44.808680585Z",
        "Path": "top",
        "Args": [],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 2714214,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2021-11-29T08:13:45.178682987Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:7138284460ffa3bb6ee087344f5b051468b3f8697e2d1427bac1a20c8d168b14",
        "ResolvConfPath": "/var/lib/docker/containers/d7972b05a3f8465349ca6d7867dc1466a7f534749e82df5da07a547a2bbf4d27/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/d7972b05a3f8465349ca6d7867dc1466a7f534749e82df5da07a547a2bbf4d27/hostname",
        "HostsPath": "/var/lib/docker/containers/d7972b05a3f8465349ca6d7867dc1466a7f534749e82df5da07a547a2bbf4d27/hosts",
        "LogPath": "/var/lib/docker/containers/d7972b05a3f8465349ca6d7867dc1466a7f534749e82df5da07a547a2bbf4d27/d7972b05a3f8465349ca6d7867dc1466a7f534749e82df5da07a547a2bbf4d27-json.log",
        "Name": "/buxyboxy",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "docker-default",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "host",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": false,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/8911acbb2fc9f22562688183a8751fc8a1ae03fa48e4707d56bb59908a1f8886-init/diff:/var/lib/docker/overlay2/695de00d545eba641980a9a6b5f09adb7e6b6085b86ab4f8b2b5d4dade026047/diff",
                "MergedDir": "/var/lib/docker/overlay2/8911acbb2fc9f22562688183a8751fc8a1ae03fa48e4707d56bb59908a1f8886/merged",
                "UpperDir": "/var/lib/docker/overlay2/8911acbb2fc9f22562688183a8751fc8a1ae03fa48e4707d56bb59908a1f8886/diff",
                "WorkDir": "/var/lib/docker/overlay2/8911acbb2fc9f22562688183a8751fc8a1ae03fa48e4707d56bb59908a1f8886/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "d7972b05a3f8",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "top"
            ],
            "Image": "busybox",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
        },
		...
    }
]
(venv) ➜  ~
```