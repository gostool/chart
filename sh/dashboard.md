## 参考ansible 部署仓库

```
(venv) ➜  sh systemctl status dashboard
● dashboard.service - Dashboard
     Loaded: loaded (/etc/systemd/system/dashboard.service; disabled; vendor preset: enabled)
     Active: active (running) since Wed 2021-11-24 11:25:58 CST; 2min 20s ago
   Main PID: 3935207 (dashboard.sh)
      Tasks: 8 (limit: 4654)
     Memory: 10.9M
     CGroup: /system.slice/dashboard.service
             ├─3935207 /bin/zsh /root/apps/install/sh/dashboard.sh
             └─3935233 kubectl -n kubernetes-dashboard port-forward --address 0.0.0.0 kubernetes-dashboard-7c5bb7b588-k9ggq 8443:8443

Nov 24 11:25:58 master-node dashboard.sh[3935208]: current-context: kubernetes-admin@kubernetes
Nov 24 11:25:58 master-node dashboard.sh[3935208]: kind: Config
Nov 24 11:25:58 master-node dashboard.sh[3935208]: preferences: {}
Nov 24 11:25:58 master-node dashboard.sh[3935208]: users:
Nov 24 11:25:58 master-node dashboard.sh[3935208]: - name: kubernetes-admin
Nov 24 11:25:58 master-node dashboard.sh[3935208]:   user:
Nov 24 11:25:58 master-node dashboard.sh[3935208]:     client-certificate-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURJVENDQWdtZ0F3SUJBZ0lJU2hVQUN6V2pOU3d3RFFZSktvWklodmNOQVFFTEJRQXdGVEVUTUJFR0ExVUUKQXhNS2EzVmlaWEp1WlhSbGN6QWVGdzB5>
Nov 24 11:25:58 master-node dashboard.sh[3935208]:     client-key-data: LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFcEFJQkFBS0NBUUVBMktrUUk0c2JIanV3cXRPQWpUYTVGNy9pMVpwQWJtT3hKZWV0aGVSZnhleFpDTXRtCnl1VmZNSWo3VWxGL1pjRk9HT040ZHkxcXRr>
Nov 24 11:25:58 master-node dashboard.sh[3935207]: will start dashboard
Nov 24 11:25:59 master-node dashboard.sh[3935233]: Forwarding from 0.0.0.0:8443 -> 8443
(venv) ➜  sh
```


## 部署和访问 Kubernetes 仪表板（Dashboard）

[doc](https://kubernetes.io/zh-cn/docs/tasks/access-application-cluster/web-ui-dashboard/)

