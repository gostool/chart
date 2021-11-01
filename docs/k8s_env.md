## ENV

每个pod在创建时，都可以获取到当前命名空间下的当前环境变量。
新增service后，需要重新创建的pod才能看到.

```
root@frontend-wqxwc:/app# env
KUBERNETES_SERVICE_PORT_HTTPS=443
DEIS_WORKFLOW_SERVICE_HOST=10.99.59.176
KUBERNETES_SERVICE_PORT=443
NGINX_SERVICE_PORT_80_TCP_ADDR=10.104.125.47
REDIS_MASTER_SERVICE_HOST=10.106.70.90
HOSTNAME=frontend-wqxwc
PYTHON_VERSION=3.9.7
DEIS_WORKFLOW_SERVICE_PORT=80
NGINX_SERVICE_PORT_80_TCP=tcp://10.104.125.47:80
NGINX_SERVICE_SERVICE_HOST=10.104.125.47
REDIS_SLAVE_PORT_6379_TCP_PROTO=tcp
REDIS_MASTER_PORT_6379_TCP_PROTO=tcp
DEIS_WORKFLOW_PORT_80_TCP_ADDR=10.99.59.176
PWD=/app
MYSVCNODE_PORT_80_TCP_PROTO=tcp
DEIS_WORKFLOW_PORT_80_TCP_PORT=80
PYTHON_SETUPTOOLS_VERSION=57.5.0
NGINX_SERVICE_PORT_80_TCP_PROTO=tcp
HOME=/root
NGINX_SERVICE_PORT_80_TCP_PORT=80
LANG=C.UTF-8
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
DEIS_WORKFLOW_PORT=tcp://10.99.59.176:80
GPG_KEY=E3FF2839C048B25C084DEBE9B26995E310250568
NGINX_SERVICE_SERVICE_PORT=80
MYSVCNODE_SERVICE_PORT=80
DEIS_WORKFLOW_SERVICE_PORT_HTTP=80
NGINX_SERVICE_PORT=tcp://10.104.125.47:80
MYSVCNODE_PORT_80_TCP=tcp://10.109.242.208:80
REDIS_MASTER_PORT_6379_TCP_PORT=6379
MYSVCNODE_PORT_80_TCP_ADDR=10.109.242.208
MYSVCNODE_PORT=tcp://10.109.242.208:80
REDIS_MASTER_SERVICE_PORT=6379
TERM=xterm
REDIS_MASTER_PORT=tcp://10.106.70.90:6379
REDIS_SLAVE_SERVICE_PORT=6379
REDIS_MASTER_PORT_6379_TCP=tcp://10.106.70.90:6379
DEIS_WORKFLOW_PORT_80_TCP=tcp://10.99.59.176:80
MYSVCNODE_PORT_80_TCP_PORT=80
SHLVL=1
KUBERNETES_PORT_443_TCP_PROTO=tcp
PYTHON_PIP_VERSION=21.2.4
REDIS_MASTER_PORT_6379_TCP_ADDR=10.106.70.90
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
REDIS_SLAVE_PORT_6379_TCP=tcp://10.107.140.134:6379
DEIS_WORKFLOW_PORT_80_TCP_PROTO=tcp
PYTHON_GET_PIP_SHA256=01249aa3e58ffb3e1686b7141b4e9aac4d398ef4ac3012ed9dff8dd9f685ffe0
REDIS_SLAVE_SERVICE_HOST=10.107.140.134
REDIS_SLAVE_PORT_6379_TCP_ADDR=10.107.140.134
KUBERNETES_SERVICE_HOST=10.96.0.1
KUBERNETES_PORT=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP_PORT=443
PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/d781367b97acf0ece7e9e304bf281e99b618bf10/public/get-pip.py
PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
MYSVCNODE_SERVICE_HOST=10.109.242.208
REDIS_SLAVE_PORT=tcp://10.107.140.134:6379
REDIS_SLAVE_PORT_6379_TCP_PORT=6379
_=/usr/bin/env
root@frontend-wqxwc:/app#
```


## debug

我们在python的容器里调