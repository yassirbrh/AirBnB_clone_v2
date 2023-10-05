#!/usr/bin/env bash
# Bash script that sets up the web servers for the deployment of web_static
apt-get update -y
apt-get install -y nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
echo "http {
        root /var/www/helloworld;
        index index.html;
        server {
                listen 80;
                location \ {
                }
                location /hbnb_static {
                	alias /data/web_static/current;
                	index index.html;
                }
        }
}
events {
}" > /etc/nginx/nginx.conf
service nginx restart
