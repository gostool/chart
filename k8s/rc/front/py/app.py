#!flask/bin/python
import os
from flask import Flask, jsonify

app = Flask(__name__)

# helm install redis bitnami/redis -n db
# 使用helm安装bitnami/redis. 一个主节点多个副本节点.
# redis-master.db.svc.cluster.local for read/write operations (port 6379)
# redis-replicas.db.svc.cluster.local for read-only operations (port 6379)
# 需要登陆密码
master_host = os.getenv('REDIS_MASTER_SERVICE_HOST', 'localhost')
master_port = os.getenv('REDIS_MASTER_SERVICE_PORT', 6379)
slave_host = os.getenv('REDIS_REPLICAS_SERVICE_HOST', 'localhost')
slave_port = os.getenv('REDIS_REPLICAS_SERVICE_HOST', 6379)

@app.route('/')
def index():
    data = {
        "master_host": master_host,
        "master_port": master_port,
        "slave_host": slave_host,
        "slave_port": slave_port,
        "app": "app",
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)