## img
make img

```
(venv) ➜  py git:(dev) ✗ make img
make build
make[1]: Nothing to be done for `build'.
docker build -t registry.cn-beijing.aliyuncs.com/hyhbackend/flaskweb:0.1 . -f Dockerfile
[+] Building 0.1s (11/11) FINISHED                                 
 => [internal] load build definition from Dockerfile          0.0s
 => => transferring dockerfile: 37B                           0.0s
 => [internal] load .dockerignore                             0.0s
 => => transferring context: 34B                              0.0s
 => [internal] load metadata for docker.io/library/python:3.  0.0s
 => [1/6] FROM docker.io/library/python:3.9                   0.0s
 => [internal] load build context                             0.0s
 => => transferring context: 299B                             0.0s
 => CACHED [2/6] WORKDIR /app                                 0.0s
 => CACHED [3/6] COPY requirements.txt ./                     0.0s
 => CACHED [4/6] COPY pip.conf /etc/pip.conf                  0.0s
 => CACHED [5/6] RUN pip install --no-cache-dir -r requireme  0.0s
 => CACHED [6/6] COPY . .                                     0.0s
 => exporting to image                                        0.0s
 => => exporting layers                                       0.0s
 => => writing image sha256:7609bbed65bff66c20ef0f5e6f6db76f  0.0s
 => => naming to registry.cn-beijing.aliyuncs.com/hyhbackend  0.0s
docker push registry.cn-beijing.aliyuncs.com/hyhbackend/flaskweb:0.1
The push refers to repository [registry.cn-beijing.aliyuncs.com/hyhbackend/flaskweb]
e260ff0eb196: Layer already exists 
62c6093436d5: Layer already exists 
67a13b60e91c: Layer already exists 
bbce76b2d720: Layer already exists 
c3176dc9be97: Layer already exists 
0462ba7ebae3: Layer already exists 
ec43cabdaa8e: Layer already exists 
4907938bbac8: Layer already exists 
c1792902851c: Layer already exists 
c272c95c3fb0: Layer already exists 
3054497613e6: Layer already exists 
d35dc7f4c79e: Layer already exists 
dabfe5b2ea81: Layer already exists 
5e6a409f30b6: Layer already exists 
0.1: digest: sha256:39e2553fa3895609a6eb497603c503e73c9caec016270b3bce3bc96409655934 size: 3259
(venv) ➜  py git:(dev) ✗ 
```

## run
访问: localhost:8080

```
(venv) ➜  py git:(dev) make imgR
docker run --rm -it -p 8080:8888 registry.cn-beijing.aliyuncs.com/hyhbackend/flaskweb:0.1
[2021-10-13 06:41:56 +0000] [1] [INFO] Starting gunicorn 20.1.0
[2021-10-13 06:41:56 +0000] [1] [INFO] Listening at: http://0.0.0.0:8888 (1)
[2021-10-13 06:41:56 +0000] [1] [INFO] Using worker: sync
[2021-10-13 06:41:56 +0000] [6] [INFO] Booting worker with pid: 6
[2021-10-13 06:41:56 +0000] [7] [INFO] Booting worker with pid: 7
[2021-10-13 06:41:56 +0000] [8] [INFO] Booting worker with pid: 8
[2021-10-13 06:41:56 +0000] [9] [INFO] Booting worker with pid: 9
[2021-10-13 06:41:56 +0000] [10] [INFO] Booting worker with pid: 10
[2021-10-13 06:41:58 +0000] [1] [INFO] Handling signal: winch
[2021-10-13 06:41:58 +0000] [1] [INFO] Handling signal: winch
[2021-10-13 06:41:58 +0000] [1] [INFO] Handling signal: winch
[2021-10-13 06:41:59 +0000] [1] [INFO] Handling signal: winch
[2021-10-13 06:41:59 +0000] [1] [INFO] Handling signal: winch
```