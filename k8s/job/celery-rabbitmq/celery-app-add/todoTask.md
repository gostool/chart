## todo
* 画架构图.
* 消费任务频率，每10s一个
	* 修改代码
	* 编译新镜像, 重写makefile
	* 更新celery-controller.yaml 镜像.
* 替换rabbit mq 中消息队列的名字为pyTaskQueue
* 使用redis 替换rabbit


## flask celery
* 定时任务
* 异步任务

使用flask + celery 构建一个任务Api
* 异步任务
	* 创建任务，获取任务id
	* 查询任务状态.
* 定时抓取知乎热榜.

## django celery