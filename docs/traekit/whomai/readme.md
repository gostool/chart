## traefik whomai 
[源码仓库](https://github.com/gostool/chart/tree/dev/k8s/ingress/traefik)

## whoami 实践过程
* pod/svc
* http: ingressRoute
* https: ingressRoute-tls


```
(venv) ➜  traefik git:(dev) kubectl apply -f whoami.yaml
pod/whoami created
service/whoami created
(venv) ➜  traefik git:(dev) kubectl get all -l "app=whoami"
NAME         READY   STATUS    RESTARTS   AGE
pod/whoami   1/1     Running   0          5s

NAME             TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
service/whoami   ClusterIP   10.107.131.127   <none>        80/TCP    5s
(venv) ➜  traefik git:(dev) kubectl get ingressRoute -o wide
No resources found in default namespace.
(venv) ➜  traefik git:(dev) kubectl apply -f whoami-route.yaml
ingressroute.traefik.containo.us/whoami-route created
(venv) ➜  traefik git:(dev) kubectl apply -f whoami-route-tls.yaml
ingressroute.traefik.containo.us/whoami-route-tls created
(venv) ➜  traefik git:(dev) kubectl get ingressRoute -o wide
NAME               AGE
whoami-route       12s
whoami-route-tls   4s
(venv) ➜  traefik git:(dev)
```

## 测试 http/https
http:
```
(venv) ➜  traefik git:(dev) kubectl get svc -n traefik-ingress
NAME      TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)                                     AGE
traefik   NodePort   10.106.81.178   <none>        9000:30466/TCP,80:30525/TCP,443:30758/TCP   3h38m
(venv) ➜  traefik git:(dev) curl -v http://k8s.pyhuo.top:30525
*   Trying 8.142.109.91:30525...
* TCP_NODELAY set
* Connected to k8s.pyhuo.top (8.142.109.91) port 30525 (#0)
> GET / HTTP/1.1
> Host: k8s.pyhuo.top:30525
> User-Agent: curl/7.68.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Content-Length: 372
< Content-Type: text/plain; charset=utf-8
< Date: Thu, 09 Dec 2021 06:33:19 GMT
<
Hostname: whoami
IP: 127.0.0.1
IP: 10.244.1.119
RemoteAddr: 10.244.1.116:42646
GET / HTTP/1.1
Host: k8s.pyhuo.top:30525
User-Agent: curl/7.68.0
Accept: */*
Accept-Encoding: gzip
X-Forwarded-For: 10.244.0.0
X-Forwarded-Host: k8s.pyhuo.top:30525
X-Forwarded-Port: 30525
X-Forwarded-Proto: http
X-Forwarded-Server: traefik-5bd4d8d6cd-b765z
X-Real-Ip: 10.244.0.0

* Connection #0 to host k8s.pyhuo.top left intact
```

https:
```
(venv) ➜  traefik git:(dev) curl -v https://k8s.pyhuo.top:30758
*   Trying 8.142.109.91:30758...
* TCP_NODELAY set
* Connected to k8s.pyhuo.top (8.142.109.91) port 30758 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: /etc/ssl/certs
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_128_GCM_SHA256
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=k8s.pyhuo.top
*  start date: Dec  9 00:00:00 2021 GMT
*  expire date: Dec  9 23:59:59 2022 GMT
*  subjectAltName: host "k8s.pyhuo.top" matched cert's "k8s.pyhuo.top"
*  issuer: C=US; O=DigiCert Inc; OU=www.digicert.com; CN=Encryption Everywhere DV TLS CA - G1
*  SSL certificate verify ok.
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* Using Stream ID: 1 (easy handle 0x55fe82e3f620)
> GET / HTTP/2
> Host: k8s.pyhuo.top:30758
> user-agent: curl/7.68.0
> accept: */*
>
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* Connection state changed (MAX_CONCURRENT_STREAMS == 250)!
< HTTP/2 200
< content-type: text/plain; charset=utf-8
< date: Thu, 09 Dec 2021 06:33:35 GMT
< content-length: 373
<
Hostname: whoami
IP: 127.0.0.1
IP: 10.244.1.119
RemoteAddr: 10.244.1.116:42646
GET / HTTP/1.1
Host: k8s.pyhuo.top:30758
User-Agent: curl/7.68.0
Accept: */*
Accept-Encoding: gzip
X-Forwarded-For: 10.244.0.0
X-Forwarded-Host: k8s.pyhuo.top:30758
X-Forwarded-Port: 30758
X-Forwarded-Proto: https
X-Forwarded-Server: traefik-5bd4d8d6cd-b765z
X-Real-Ip: 10.244.0.0
* Connection #0 to host k8s.pyhuo.top left intact
(venv) ➜  traefik git:(dev)
```

访问效果:

![](https://oscimg.oschina.net/oscnet/up-53339d6721ab9d2c9c31dfafaed0c608092.png)