#!flask/bin/python
import os
from flask import Flask

app = Flask(__name__)

master_host = os.getenv('REDIS_MASTER_SERVICE_HOST', 'localhost')
slave_host = os.getenv('REDIS_MASTER_SERVICE_HOST', 'localhost')
port = os.getenv('REDIS_MASTER_SERVICE_PORT', 6379)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)