### dashboard token认证
[]()
```sh
如果没有kubernetes-dashboard这个ns，请先创建
(venv) ➜  ~ kubectl get ns
NAME                   STATUS   AGE
default                Active   2d17h
kube-node-lease        Active   2d17h
kube-public            Active   2d17h
kube-system            Active   2d17h
kubernetes-dashboard   Active   17m
(venv) ➜  ~ cd apps/chart/k8s 
(venv) ➜  k8s git:(dev) kubectl apply -f configuration/ServiceAccount/admin-user.yaml
serviceaccount/admin-user created
(venv) ➜  k8s git:(dev) kubectl apply -f rbac/cluster-admin.yaml                     
clusterrolebinding.rbac.authorization.k8s.io/admin-user unchanged
(venv) ➜  k8s git:(dev) 
(venv) ➜  k8s git:(dev) 
(venv) ➜  k8s git:(dev) 
(venv) ➜  k8s git:(dev) kubectl -n kubernetes-dashboard get secret $(kubectl -n kubernetes-dashboard get sa/admin-user -o jsonpath="{.secrets[0].name}") -o go-template="{{.data.token | base64decode}}"

eyJhbGciOiJSUzI1NiIsImtpZCI6InJEMVpudnpaQVh4WlVrbV9odUVjLXlaNHhfUmRnbm9laGxkOTdMTWV5ZlUifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXRva2VuLWpsc2s3Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiI3NzQ2YjcyOC1kZGFkLTQ2OGYtODZhYS0yMzgxODgyNjYyYzgiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZXJuZXRlcy1kYXNoYm9hcmQ6YWRtaW4tdXNlciJ9.tNH-N-oZ589uPhby7gex-n0hD3t9ajAy0isY2e78fLeP6ADAcYbn3yJwgcIJxueUqlefWJQLYNSh0pcwac_acwbDgEDkBglwUc9n-LQSP1kRD7JB34sVwCUK8OAk39TROLEw--GE6T28MGK6fHkMHGh3tspsxmgk_N4BG0__9vbvRXM6UzJE563p16tgHDStb8KUFQH7zaaWOcT7kHpIKm7ERjleIkeNF7-cVm0t0u3Ib2yd59AAGxaVzo_liNcHbxF2psu7Mw3OnxVbRLklDR36FctY2L10aCFEwucVVH7zdpPGJ9kmOJw8R2RKPtccSrzvKh_ronz3kUwFaXl2LA# 
```