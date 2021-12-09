## kube-state-metrics


[教程](http://www.mydlq.club/article/113/)


```
kubectl apply -f kube-state-metrics-rbac.yaml
kubectl apply -f kube-state-metrics-deploy.yaml -n kube-system
```

查看指标:
```

curl -kL  $(kubectl get service -n kube-system | grep kube-state-metrics |awk '{ print $3 }'):8080/metrics
```


```
export IP=`kubectl get service -n kube-system -l "app.kubernetes.io/name=kube-state-metrics" -o jsonpath="{.items[0].spec.clusterIP}" | xargs echo`
echo $IP
curl -kL $IP:8080/metrics
```
