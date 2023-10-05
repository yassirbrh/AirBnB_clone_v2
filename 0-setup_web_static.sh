#!/usr/bin/env bash
# Bash script that sets up the web servers for the deployment of web_static
apt-get update
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
chown -R ubuntu /data/
chgrp -R ubuntu /data/
echo -e "http {
        root /var/www/helloworld;
        index index.html;
        server {
                listen 80;
                add_header X-Served-By $HOSTNAME;
                location \ {
                }
                location /redirect_me {
                	return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
                }
                error_page 404 /404_redirection;
                location = /404_redirection {
                        internal;
                        return 404 \"Ceci n'est pas une page\n\n\";
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
