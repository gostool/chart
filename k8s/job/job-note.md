### Job执行完成后不会自动删除
```
执行后保留它有一定好处:如用于查找执行日志,或者在出现问题时了解pod所处的状态。
但坏处在于，如果执行次数越多，并且不删除，则这种垃圾式的残留job也会越多,人工删除略显麻烦。
```

### Job自动删除的方法
```
只要修改yaml文件，加上spec.ttlSecondsAfterFinished属性，该属性用于确定在所有任务执行完成后，需要等待多少秒才可删除Job.
这个功能默认是关闭的，需要手动开启，修改的组件包括apiserver,controller和scheduler。
直接修改/etc/Kubernetes/manifests下面对应的3个同名的.yaml静态文件,加入- --feature-gates=TTLAfterFinished=true命令,然后令对应的pod重新运行即可。
例如：修改kube-scheduler.yaml的spec部分如下：对于kube-apiserver.yaml和kube-controller-manager.yaml,
也在spec部分加入- --feature-gates=TTLAfterFinished=true即可。
spec:
  containers:
  - command:
    - kube-scheduler
    - --leader-elect=true
    - --feature-gates=TTLAfterFinished=true
```

### Job中restartPolicy字段只能是OnFailure和Never中的一个
```
因为不同于需要持续提供服务的pod，job中的pod在正常完成任务后，需要及时退出。
所以pod模板中restartPolicy字段的值可以是Always,OnFailure和Never.但在Job中，该字段只能是OnFailure和Never中的一个。
```