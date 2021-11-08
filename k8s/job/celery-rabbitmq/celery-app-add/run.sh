#!/bin/bash
# Run the celery worker
/usr/local/bin/celery -A celery_conf worker -f /data/celery.log &

# Start firing periodic tasks automatically
python /data/rn_tasks.py