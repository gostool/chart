[文档](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

#### 金丝雀发布
```yml
即确认其中一个pod没有问题后再进行剩余的更新
1. kubectl set image deployment/nginx-deployment nginx=nginx:1.16.1 --record
2. kubectl rollout pause deployment/nginx-deployment
命令1会更新nginx的版本,命令2会使更新第一个pod的时候就停止后续操作。更新完一个后，验证没有问题了，使用命令3恢复更新
3. kubectl rollout resume deployment/nginx-deployment
```