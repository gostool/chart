#!/bin/bash
nohup kubectl proxy --port=8888 --address=0.0.0.0 --accept-hosts='^.*' &
