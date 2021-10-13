APP = flaskweb
BINARY = app.py
# 禁止使用hub.docker.com 必须使用私有仓库
DOCKER_HUB = registry.cn-beijing.aliyuncs.com
NAMESPACE = hyhbackend
VERSION = 0.1
TAG = $(VERSION)
TAG_CMD = $(VE8SION_CMD)
# 必须小写
IMG_NAME = $(APP)
IMG_FULL_NAME = $(DOCKER_HUB)/$(NAMESPACE)/$(IMG_NAME):$(TAG)

all: build

.PHONY : clean fmt build img help autoR test

clean:
	docker images | grep $(IMG_NAME) | sort | awk '{print $3}' | xargs docker rmi

img:
	make build
	docker build -t $(IMG_FULL_NAME) . -f Dockerfile
	docker push $(IMG_FULL_NAME)

imgR:
	docker run --rm -it -p 8080:8888 $(IMG_FULL_NAME)