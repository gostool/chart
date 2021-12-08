# ingress 技术选型
* nginx-ingress: nginx 出品 

## nginx-ingress
[文档](https://docs.nginx.com/nginx-ingress-controller/installation/installation-with-manifests/)

## helm bitnami Nginx Ingress Controller 

[文档](https://artifacthub.io/packages/helm/bitnami/nginx-ingress-controller)
```
$ helm repo add bitnami https://charts.bitnami.com/bitnami
$ helm install my-release bitnami/nginx-ingress-controller
```

chart:下载
```
helm pull bitnami/nginx-ingress-controller --untar
```


```
(venv) ➜  k8s git:(dev) ✗ helm install my-nginx-ingress-controller bitnami/nginx-ingress-controller
NAME: my-nginx-ingress-controller
LAST DEPLOYED: Wed Dec  8 16:38:02 2021
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
CHART NAME: nginx-ingress-controller
CHART VERSION: 9.0.8
APP VERSION: 1.1.0

** Please be patient while the chart is being deployed **

The nginx-ingress controller has been installed.

Get the application URL by running these commands:

 NOTE: It may take a few minutes for the LoadBalancer IP to be available.
        You can watch its status by running 'kubectl get --namespace default svc -w my-nginx-ingress-controller'

    export SERVICE_IP=$(kubectl get svc --namespace default my-nginx-ingress-controller -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
    echo "Visit http://${SERVICE_IP} to access your application via HTTP."
    echo "Visit https://${SERVICE_IP} to access your application via HTTPS."

An example Ingress that makes use of the controller:

  apiVersion: networking.k8s.io/v1
  kind: Ingress
  metadata:
    name: example
    namespace: default
  spec:
    ingressClassName: nginx
    rules:
      - host: www.example.com
        http:
          paths:
            - backend:
                service:
                  name: example-service
                  port:
                    number: 80
              path: /
              pathType: Prefix
    # This section is only required if TLS is to be enabled for the Ingress
    tls:
        - hosts:
            - www.example.com
          secretName: example-tls

If TLS is enabled for the Ingress, a Secret containing the certificate and key must also be provided:

  apiVersion: v1
  kind: Secret
  metadata:
    name: example-tls
    namespace: default
  data:
    tls.crt: <base64 encoded cert>
    tls.key: <base64 encoded key>
  type: kubernetes.io/tls
(venv) ➜  k8s git:(dev) ✗
```