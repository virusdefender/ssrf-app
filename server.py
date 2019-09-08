#!/usr/bin/env python3
import logging
import socket

import requests
from flask import Flask, request
import furl

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)


@app.route("/api/internal/secret")
def internal_secret_api():
    if request.remote_addr != "127.0.0.1":
        return "your ip " + request.remote_addr + " is not allowed"
    else:
        return "secret{4l0DyXxz8WBRQfIwZEQ}"


@app.route("/")
def index():
    url = request.args.get('url')
    if not url:
        return "url parameter is required"
    try:
        hostname = furl.furl(url).host
        if not hostname:
            raise ValueError("empty hostname")
        ip = socket.gethostbyname(hostname)
        logging.info("resolve %s ip is %s", hostname, ip)
    except Exception as e:
        return str(e)
    if ip == "127.0.0.1":
        return "127.0.0.1 is forbidden"
    try:
        resp = requests.get(url, timeout=2)
        return resp.text
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
