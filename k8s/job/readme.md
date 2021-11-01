## job
* [k8s job](https://kubernetes.io/zh/docs/concepts/workloads/controllers/job/)


* Job 会创建一个或者多个 Pods，并将继续重试 Pods 的执行，直到指定数量的 Pods 成功终止
* 随着 Pods 成功结束，Job 跟踪记录成功完成的 Pods 个数。 当数量达到指定的成功个数阈值时，任务（即 Job）结束
* 删除 Job 的操作会清除所创建的全部 Pods。
* 挂起 Job 的操作会删除 Job 的所有活跃 Pod，直到 Job 被再次恢复执行


## 要点
* 
* 自动清理完成的Job
* Job 模式


## demo


eg1: 它负责计算 π 到小数点后 2000 位，并将结果打印出来。 此计算大约需要 10 秒钟完成。

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: pi
spec:
  template:
    spec:
      containers:
      - name: pi
        image: perl
        command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
      restartPolicy: Never
  backoffLimit: 4
```


## Job 的并行执行
* spec.completions
* spec.parallelism

适合以 Job 形式来运行的任务主要有三种
* 非并行 Job
	* 通常只启动一个 Pod，除非该 Pod 失败
	* 当 Pod 成功终止时，立即视 Job 为完成状态
* 具有确定完成计数的并行Job
	* .spec.completions 字段设置为非 0 的正数值
	* Job 用来代表整个任务，当成功的 Pod 个数达到 .spec.completions 时，Job 被视为完成
	* 当使用 .spec.completionMode="Indexed" 时，每个Pod都会获得一个不同的索引值，介于 0 和 .spec.completions-1 之间
* 带工作队列的并行Job:
	* 不设置spec.completions，默认值为 .spec.parallelism
	* 多个Pod之间必须相互协调，或者借助外部服务确定每个 Pod 要处理哪个工作条目. 例如，任一 Pod 都可以从工作队列中取走最多 N 个工作条目
	* 每个 Pod 都可以独立确定是否其它 Pod 都已完成，进而确定 Job 是否完成
	* 当 Job 中 任何 Pod 成功终止，不再创建新 Pod
	* 一旦至少 1 个 Pod 成功完成，并且所有 Pod 都已终止，即可宣告 Job 成功完成
	* 一旦任何 Pod 成功退出，任何其它 Pod 都不应再对此任务执行任何操作或生成任何输出。 所有 Pod 都应启动退出过程


对于 非并行 的 Job，你可以不设置 spec.completions 和 spec.parallelism。 这两个属性都不设置时，均取默认值 1



### 并行job
* 同时有2个任务执行.

```
➜  k8s git:(dev) ✗ kubectl apply -f job/paral-job.yaml
job.batch/paral-myjob created
➜  k8s git:(dev) ✗ kubectl get job
NAME          COMPLETIONS   DURATION   AGE
paral-myjob   0/8           4s         4s
➜  k8s git:(dev) ✗
➜  k8s git:(dev) ✗ kubectl get pod
NAME                        READY   STATUS      RESTARTS   AGE
paral-myjob-2ckql           0/1     Completed   0          100s
paral-myjob-5rgtm           0/1     Completed   0          62s
paral-myjob-7f465           0/1     Completed   0          97s
paral-myjob-8wf4v           0/1     Completed   0          2m14s
paral-myjob-g4blw           0/1     Completed   0          65s
paral-myjob-gbrx5           1/1     Running     0          29s
paral-myjob-nx9w9           1/1     Running     0          27s
paral-myjob-vnvhm           0/1     Completed   0          2m14s
➜  k8s git:(dev) ✗
```