#!/usr/bin/env bash
# bash script to set up the servers for the deployment of web_static
sudo apt-get update

#check if nginx is installed
command -v nginx
check1=$?
if [ "$check1" -eq 1 ]; then
    sudo apt-get -y install nginx
fi

#set a path to install the web_static pages
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/shared
varpath='/data/web_static/releases/test/'
sudo mkdir -p "$varpath"
if [ ! -e "${varpath}"/index.html ]; then
    echo "<html><h1>Test</h1>file index</html>" | sudo tee "${varpath}/index.html"
fi

#create a symbolic link
sudo ln -sf "$varpath" /data/web_static/current

# adduser ubuntu for docker
#update ownership of /data
sudo chown -R ubuntu:ubuntu /data/

#update the nginx config file
new_string="\n    #set the location of the static site\n    location /hbnb_static {\n        alias /data/web_static/current/;\n   }"
grep -q /etc/nginx/sites-enabled/default -e "hbnb_static"
check2=$?
if [ "$check2" -eq 1 ] ; then
    sudo sed -i "51 i\ $new_string" /etc/nginx/sites-available/default
fi
sudo service nginx restart
