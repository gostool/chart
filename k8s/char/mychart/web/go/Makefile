APP = main
BINARY = main
# 禁止使用hub.docker.com 必须使用私有仓库
DOCKER_HUB = registry.cn-beijing.aliyuncs.com
NAMESPACE = hyhbackend
VERSION = 0.1.0
TAG = $(VERSION)
# 必须小写
IMG_NAME = web
IMG_FULL_NAME = $(DOCKER_HUB)/$(NAMESPACE)/$(IMG_NAME):$(TAG)

all: build

.PHONY : clean fmt build img help autoR test

clean:
	rm -f ./$(BINARY)
	docker images | grep $(IMG_NAME) | sort | awk '{print $3}' | xargs docker rmi

img:
	docker build -t $(IMG_FULL_NAME) . -f Dockerfile
	docker push $(IMG_FULL_NAME)

help:
	@echo "make docker - 编译镜像!"
	@echo "make autoR - tx环境,自动部署!"


