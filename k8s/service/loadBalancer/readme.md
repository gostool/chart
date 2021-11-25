## LoadBalancer
使用云厂商.
[fix bug](https://makeoptim.com/service-mesh/kubernetes-external-ip-pending)
[fix bug](https://makeoptim.com/service-mesh/kubeadm-kubernetes-istio-setup#metallb)

```
(venv) ➜  k8s git:(dev) kubectl apply -f service/loadBalancer/nginx-service.yaml
service/myservice-slb-nginx created
(venv) ➜  k8s git:(dev)
(venv) ➜  k8s git:(dev) kubectl get svc -o wide
NAME                  TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE    SELECTOR
kubernetes            ClusterIP      10.96.0.1       <none>        443/TCP        8d     <none>
myservice-slb-nginx   LoadBalancer   10.106.230.99   <pending>     80:31903/TCP   2m6s   app=nginx
(venv) ➜  k8s git:(dev)
```


