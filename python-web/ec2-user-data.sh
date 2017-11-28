#!/bin/bash
yum update -y
yum install -y python36 python36-pip python36-setuptools
easy_install-3.6 pip
/usr/local/bin/pip3 install flask
mkdir /website
cd /website
curl https://s3.amazonaws.com/gd2017-team-assets-us-east-1/modules/dude_wheres_my_website/player-assets/unicorn_rentals_website_1_0.zip -o /website/unicorn_rentals.zip
unzip /website/unicorn_rentals.zip
chmod +700 unicornrentalswebserver.py
./unicornrentalswebserver.py
