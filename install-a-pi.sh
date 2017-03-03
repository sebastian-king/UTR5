#!/bin/bash

echo "THE PI WILL REBOOT ONCE THIS SCRIPT HAS FINISHED RUNNING!";
read -r -p "Press X to exit the script now if you do not want to reboot " response;
if [[ "$response" =~ ^([xX])+$ ]]; then
    exit;
fi

raspi-config --expand-rootfs

sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade

sudo apt-get -y install git

cd ~
git clone https://github.com/afloresescarcega/UTR5.git # perhaps ignore this file

#adduser r5 --home /home/r5 -q --disabled-password --gecos GECOS

#su r5
#cd ~

sudo sudo apt-get -y install python python-pip python-dev python3 python-pip3 python3-dev
sudo pip install wiringpi
sudo pip install wiringpi2

sudo reboot
