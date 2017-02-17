#!/bin/bash

apt-get update
apt-get upgrade
apt-get dist-upgrade

apt-get install git
cd /usr/src/

git clone https://github.com/afloresescarcega/UTR5.git

adduser r5 --home /home/r5 -q --disabled-password --gecos GECOS

su r5
cd ~
