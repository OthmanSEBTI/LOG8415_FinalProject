#! /usr/bin/bash

sudo apt-get update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.9 -y

sudo apt install python3-pip -y
sudo pip install boto3
sudo pip install paramiko

sudo git clone https://github.com/OthmanSEBTI/LOG8415_FinalProject.git

# set credantials
sudo mkdir  /home/ubuntu/.aws

echo | cat /home/ubuntu/LOG8415_FinalProject/credentials | sudo tee -a credentials
echo | cat /home/ubuntu/LOG8415_FinalProject/config | sudo tee -a config

python3 ./LOG8415_FinalProject/Sessions_setup.py


