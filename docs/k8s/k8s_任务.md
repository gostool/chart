# 任务

## job

[job](https://kubernetes.io/zh/docs/concepts/workloads/controllers/job/)

## CronJob
[cronjob](https://kubernetes.io/zh/docs/concepts/workloads/controllers/cron-jobs/)


```
apiVersion: batch/v1
kind: CronJob
metadata:
  name: hello
spec:
  schedule: "*/1 * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: hello
            image: busybox
            imagePullPolicy: IfNotPresent
            command:
            - /bin/sh
            - -c
            - date; echo Hello from the Kubernetes cluster
          restartPolicy: OnFailure

```
