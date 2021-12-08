#!/bin/python
import os

image_list = [
	"k8s.gcr.io/ingress-nginx/controller:v1.1.0",
	"k8s.gcr.io/ingress-nginx/kube-webhook-certgen:v1.1.1",
]

def cmd_exec(*cmd_args):
	for cmd in cmd_args:
		print(f"cmd:{cmd}")
		os.system(cmd)
	return

def make_img_cmd(src_img:str):
	"""
	组合命令
	"""
	cmd_pull = f"docker pull {src_img}"
	new_img = str(src_img).replace("k8s.gcr.io", "registry.cn-beijing.aliyuncs.com/hyhbackend")
	cmd_tag = f"docker tag {src_img} {new_img}"
	cmd_push = f"docker push {new_img}"
	print(cmd_pull)
	print(cmd_tag)
	print(cmd_push)
	cmd_exec(cmd_pull, cmd_tag, cmd_pull)
	return

def main():
	for img in image_list:	
		pull_img(img)

if __name__ == '__main__':
	main()
	