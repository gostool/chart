## helm debug mychart


```
(venv) ➜  char git:(dev) helm install mycahrt mychart --dry-run --debug
install.go:178: [debug] Original chart version: ""
install.go:199: [debug] CHART PATH: /root/apps/chart/k8s/char/mychart
```

```yaml
NAME: mycahrt
LAST DEPLOYED: Mon Nov 29 14:51:32 2021
NAMESPACE: default
STATUS: pending-install
REVISION: 1
USER-SUPPLIED VALUES:
{}

COMPUTED VALUES:
affinity: {}
autoscaling:
  enabled: false
  maxReplicas: 100
  minReplicas: 1
  targetCPUUtilizationPercentage: 80
fullnameOverride: ""
image:
  containerPort: 8000
  pullPolicy: IfNotPresent
  repository: registry.cn-beijing.aliyuncs.com/hyhbackend/web
  tag: 0.1.0
imagePullSecrets:
- name: regcred
ingress:
  annotations: {}
  className: ""
  enabled: false
  hosts:
  - host: chart-example.local
    paths:
    - path: /
      pathType: ImplementationSpecific
  tls: []
nameOverride: ""
nodeSelector: {}
podAnnotations: {}
podSecurityContext: {}
replicaCount: 1
resources: {}
securityContext: {}
service:
  port: 80
  targetPort: 8000
  type: ClusterIP
serviceAccount:
  annotations: {}
  create: true
  name: mychart-web
tolerations: []

HOOKS:
---
# Source: mychart-web/templates/tests/test-connection.yaml
apiVersion: v1
kind: Pod
metadata:
  name: "mycahrt-mychart-web-test-connection"
  labels:
    helm.sh/chart: mychart-web-0.1.0
    app.kubernetes.io/name: mychart-web
    app.kubernetes.io/instance: mycahrt
    app.kubernetes.io/version: "1.0.0"
    app.kubernetes.io/managed-by: Helm
  annotations:
    "helm.sh/hook": test
spec:
  containers:
    - name: wget
      image: busybox
      command: ['wget']
      args: ['mycahrt-mychart-web:80']
  restartPolicy: Never
MANIFEST:
---
# Source: mychart-web/templates/serviceaccount.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: mychart-web
  labels:
    helm.sh/chart: mychart-web-0.1.0
    app.kubernetes.io/name: mychart-web
    app.kubernetes.io/instance: mycahrt
    app.kubernetes.io/version: "1.0.0"
    app.kubernetes.io/managed-by: Helm
---
# Source: mychart-web/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: mycahrt-mychart-web
  labels:
    helm.sh/chart: mychart-web-0.1.0
    app.kubernetes.io/name: mychart-web
    app.kubernetes.io/instance: mycahrt
    app.kubernetes.io/version: "1.0.0"
    app.kubernetes.io/managed-by: Helm
spec:
  type: ClusterIP
  ports:
    - port: 80
      targetPort:  8000
      protocol: TCP
      name: http
  selector:
    app.kubernetes.io/name: mychart-web
    app.kubernetes.io/instance: mycahrt
---
# Source: mychart-web/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mycahrt-mychart-web
  labels:
    helm.sh/chart: mychart-web-0.1.0
    app.kubernetes.io/name: mychart-web
    app.kubernetes.io/instance: mycahrt
    app.kubernetes.io/version: "1.0.0"
    app.kubernetes.io/managed-by: Helm
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/name: mychart-web
      app.kubernetes.io/instance: mycahrt
  template:
    metadata:
      labels:
        app.kubernetes.io/name: mychart-web
        app.kubernetes.io/instance: mycahrt
    spec:
      imagePullSecrets:
        - name: regcred
      serviceAccountName: mychart-web
      securityContext:
        {}
      containers:
        - name: mychart-web
          securityContext:
            {}
          image: "registry.cn-beijing.aliyuncs.com/hyhbackend/web:0.1.0"
          imagePullPolicy: IfNotPresent
          ports:
            - name: http
              containerPort: 8000
              protocol: TCP
          livenessProbe:
            httpGet:
              path: /
              port: http
          readinessProbe:
            httpGet:
              path: /
              port: http
          resources:
            {}

```

NOTES:
```sh
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=mychart-web,app.kubernetes.io/instance=mycahrt" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8000 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8000:$CONTAINER_PORT
  echo "Visit http://ip:8000 to use your application"
  kubectl --namespace default port-forward --address 0.0.0.0 $POD_NAME 8000:$CONTAINER_PORT
(venv) ➜  char git:(dev)
```