#!/usr/bin/env bash
# Script that sets up web-servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/{releases/test,shared}
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i '/listen 80 default_server/a \\tlocation /hbnb_static {alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo service nginx restart
