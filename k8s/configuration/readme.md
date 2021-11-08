## configmap
* pod-with-configmap.yaml

pod 中的环境变量使用 configMap的值

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
```