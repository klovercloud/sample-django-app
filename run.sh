#!/bin/bash
echo '[INFO] Starting Nginx'
nginx -g 'daemon on;'
echo '[INFO] Starting Application Server'
python3 manage.py runserver 0.0.0.0:8000