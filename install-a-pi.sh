#!/bin/bash

apt-get update
apt-get upgrade
apt-get dist-upgrade

apt-get install git
cd /usr/src/

git clone https://github.com/afloresescarcega/UTR5.git # perhaps ignore this file

adduser r5 --home /home/r5 -q --disabled-password --gecos GECOS

#su r5
#cd ~

sudo apt-get install python python-pip python-dev python3 python-pip3 python3-dev
pip install wiringpi
pip install wiringpi2
