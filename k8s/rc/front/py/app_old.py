#!flask/bin/python
import os
from flask import Flask, jsonify

app = Flask(__name__)

master_host = os.getenv('REDIS_MASTER_SERVICE_HOST', 'localhost')
master_port = os.getenv('REDIS_MASTER_SERVICE_PORT', 6379)
slave_host = os.getenv('REDIS_SLAVE_SERVICE_HOST', 'localhost')
slave_port = os.getenv('REDIS_SLAVE_SERVICE_PORT', 6379)

@app.route('/')
def index():
    data = {
        "master_host": master_host,
        "master_port": master_port,
        "slave_host": slave_host,
        "slave_port": slave_port,
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)