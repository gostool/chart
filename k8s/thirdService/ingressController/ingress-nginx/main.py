#!/bin/python
import os

img_registry = "registry.cn-beijing.aliyuncs.com/hyhbackend"
image_map = {
	"k8s.gcr.io/ingress-nginx/controller:v1.1.0": "ingress-nginx-controller:v1.1.0",
	"k8s.gcr.io/ingress-nginx/kube-webhook-certgen:v1.1.1": "ingress-nginx-kube-webhook-certgen:v1.1.1",
}

def cmd_exec(*cmd_args, debug=True):
	for cmd in cmd_args:
		if debug:
			print(f"{cmd}")
			continue
		os.system(cmd)
	return

def make_img_cmd(src_img:str, new_name:str, debug:bool):
	"""
	组合命令
	"""
	cmd_pull = f"docker pull {src_img}"
	new_img = f"{img_registry}/{new_name}"
	cmd_tag = f"docker tag {src_img} {new_img}"
	cmd_push = f"docker push {new_img}"
	cmd_exec(cmd_pull, cmd_tag, cmd_push, debug=debug)
	return

def main():
	for k,v in image_map.items():	
		make_img_cmd(k, v, True)

if __name__ == '__main__':
	main()
	