APP = flaskweb
BINARY = app.py
# 禁止使用hub.docker.com 必须使用私有仓库
DOCKER_HUB = registry.cn-beijing.aliyuncs.com
NAMESPACE = hyhbackend
VERSION = 0.4.1
TAG = $(VERSION)
TAG_CMD = $(VE8SION_CMD)
# 必须小写
IMG_NAME = $(APP)
IMG_FULL_NAME = $(DOCKER_HUB)/$(NAMESPACE)/$(IMG_NAME):$(TAG)

all: img

.PHONY : clean fmt build img help autoR test

clean:
	docker images | grep $(IMG_NAME) | sort | awk '{print $3}' | xargs docker rmi

img:
	docker build -t $(IMG_FULL_NAME) . -f Dockerfile
	docker push $(IMG_FULL_NAME)

imgR:
	docker run --rm -it -p 5000:5000 $(IMG_FULL_NAME)

imgRL:
	docker run --rm -it --network=host  $(IMG_FULL_NAME)