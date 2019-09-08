#! /bin/bash
mkdir /run/sshd
/usr/sbin/sshd
redis-server --daemonize yes
python3 /app/server.py
gunicorn -w 4 -t 4 -b [::]:8000 -b 0.0.0.0:8000 app:app
