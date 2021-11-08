

## configmap
* 环境变量
* 文件
* 被挂载的 ConfigMap 内容会被自动更新
* 不可变更的 ConfigMap


注意要点:
* ETCD对configMap限制了写如大小1MB
* pod 引入的configMap必须是同一个nameSpace. (cm metadata定义了命名空间)
* 先创建configMap, 在创建pod


### pod 使用ConfigMap
* pod-with-configmap.yaml


ConfigMap 挂载为文件 

```
/config # env
MONGO_SERVICE_HOST=10.99.12.52
KUBERNETES_PORT=tcp://10.96.0.1:443
KUBERNETES_SERVICE_PORT=443
UI_PROPERTIES_FILE_NAME=user-interface.properties
HOSTNAME=configmap-demo-pod
PLAYER_INITIAL_LIVES=3
...
PWD=/config
/config # 
/config # pwd
/config
/config # ls -l
total 0
lrwxrwxrwx    1 root     root            22 Nov  8 07:54 game.properties -> ..data/game.properties
lrwxrwxrwx    1 root     root            32 Nov  8 07:54 user-interface.properties -> ..data/user-interface.properties
/config # ls -l ..data/
total 8
-rw-r--r--    1 root     root            55 Nov  8 07:54 game.properties
-rw-r--r--    1 root     root            57 Nov  8 07:54 user-interface.properties
/config # 
/config # 
/config # cat game.properties 
enemy.types=aliens,monsters
player.maximum-lives=5    
/config # cat user-interface.properties 
color.good=purple
color.bad=yellow
allow.textmode=true  
/config # 
```