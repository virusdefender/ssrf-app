FROM python:3.7
RUN apt update && apt install -y redis-server openssh-server curl
RUN pip3 install flask requests furl gunicorn
ADD . /app
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT /app/entrypoint.sh
