#!flask/bin/python
import os
from flask import Flask, jsonify
import redis

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


@app.route('/set/<key>/<value>')
def setData(key, value):
    r = redis.StrictRedis(host=master_host, port=master_port)
    r.set(key, value)
    data = {
        key: value,
        "result": "success"
    }
    return jsonify(data)


@app.route('/get/<key>')
def getData(key):
    r = redis.StrictRedis(host=master_host, port=master_port)
    data = r.get(key)
    data = data.decode('utf8')
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
