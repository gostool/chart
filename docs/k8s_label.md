## Label(标签)
[label对象](https://kubernetes.io/zh/docs/concepts/overview/working-with-objects/labels/)

Label以key/val键值对的形式附加到各种对象(Pod, Service, RC, Node)。

### 形式
* 等值
* 不包含
* 集合

```
"app=nginx"
"env!=production"
"name in (redis-master, redis-slave)"
```


