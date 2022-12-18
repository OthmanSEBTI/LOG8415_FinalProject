#! /usr/bin/bash

# install mysql
sudo apt-get install mysql-server -y
sudo apt-get install sysbench -y

# install sakila
cp /home/ubuntu/LOG8415_FinalProject/sakila-db.tar.gz /home/ubuntu/
sudo tar xvf /home/ubuntu/sakila-db.tar.gz
