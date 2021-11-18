### helm install k8s dashboard
[参考](https://artifacthub.io/packages/helm/k8s-dashboard/kubernetes-dashboard)

```sh
(venv) ➜  ~ helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
"kubernetes-dashboard" has been added to your repositories
(venv) ➜  ~ helm install my-release kubernetes-dashboard/kubernetes-dashboard         
NAME: my-release
LAST DEPLOYED: Thu Nov 18 22:46:13 2021
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
*********************************************************************************
*** PLEASE BE PATIENT: kubernetes-dashboard may take a few minutes to install ***
*********************************************************************************

Get the Kubernetes Dashboard URL by running:
  export POD_NAME=$(kubectl get pods -n default -l "app.kubernetes.io/name=kubernetes-dashboard,app.kubernetes.io/instance=my-release" -o jsonpath="{.items[0].metadata.name}")
  echo https://127.0.0.1:8443/
  kubectl -n default port-forward $POD_NAME 8443:8443
(venv) ➜  ~ export POD_NAME=$(kubectl get pods -n default -l "app.kubernetes.io/name=kubernetes-dashboard,app.kubernetes.io/instance=my-release" -o jsonpath="{.items[0].metadata.name}")
(venv) ➜  ~ echo https://127.0.0.1:8443/
https://127.0.0.1:8443/
(venv) ➜  ~ kubectl -n default port-forward
(venv) ➜  ~ kubectl -n default port-forward $POD_NAME 8443:8443
Forwarding from 127.0.0.1:8443 -> 8443
Forwarding from [::1]:8443 -> 8443
Handling connection for 8443
Handling connection for 8443
^C#                                                                                                                                                                                                                                                                                                                                                 (venv) ➜  ~ kubectl -n default port-forward --address 0.0.0.0 $POD_NAME 8443:8443
Forwarding from 0.0.0.0:8443 -> 8443
Handling connection for 8443
Handling connection for 8443
Handling connection for 8443
Handling connection for 8443
Handling connection for 8443
^C#                                                                                                                                                                                                                                                                                                                                                 (venv) ➜  ~ 

```