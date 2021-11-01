## nginx 
* nginx work: 用户
* 13 Permission denied

1.查看当前nginx worker 使用的用户: nobody 非root
```
(venv) root@:~/apps/app# ps -ef | grep nginx
root      1002     1  0  2020 ?        00:00:00 nginx: master process /usr/local/openresty/nginx/sbin/nginx -g daemon on; master_process on;
nobody   22833  1002  0 16:22 ?        00:00:01 nginx: worker process
nobody   22834  1002  0 16:22 ?        00:00:01 nginx: worker process
root     26466 24071  0 16:52 pts/0    00:00:00 grep --color=auto nginx
(venv) root@:~/apps/app#
```

2. 检查nobody 用户是否拥有static 权限. 没有权限则报权限不足
```
(venv) root@:~/apps/app# sudo -u nobody stat  /www/static
  File: '/www/static'
  Size: 4096      	Blocks: 8          IO Block: 4096   directory
Device: fd01h/64769d	Inode: 2359902     Links: 9
Access: (0755/drwxr-xr-x)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2021-10-29 16:50:37.761187062 +0800
Modify: 2021-10-29 16:50:37.809188602 +0800
Change: 2021-10-29 16:50:37.809188602 +0800
 Birth: -
(venv) root@:~/apps/app#
```

如权限不足:
```
(venv) root@:~/apps/budao_qls# sudo -u nobody stat /root/apps
stat: cannot stat '/root/apps': Permission denied
(venv) root@:~/apps/budao_qls#
```


3.出现权限问题，一定要检查当前用户是否可以看见配置的目录.

```
/root/xxx 需要root权限
/home/xxx/www  需要用户xxx的权限
```