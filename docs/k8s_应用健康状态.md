## 应用健康状态
[阿里文档](https://edu.aliyun.com/lesson_1651_17061?spm=5176.10731542.0.0.4e477abd9yQ9wi#_17061)

* Readness: 就绪探针
* Liveness: 存活探针



## 使用方式
探测方式
* httpGet: 	通过发送http get请求, 返回200-399
* Exec:		通过执行命令来检查服务是否正常，命令返回值为0表示容器健康
* tcpSocket 通过容器的IP和Port执行TCP检查. 能建立连接，则正常


探测结果：
* Success 通过检查
* Failure 未通过
* Unkonw  未能执行检查，不采取任何动作


重启策略:
* Always 总是重启
* OnFailure 失败才重启
* Never  永不重启
