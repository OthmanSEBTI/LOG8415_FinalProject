#! /usr/bin/bash

# install mysql
sudo apt-get update
sudo apt-get install mysql-server -y
# sudo mysql

# install sakila
sudo git clone https://github.com/OthmanSEBTI/LOG8415_FinalProject.git
cp ~/LOG8415_FinalProject/sakila-db.tar.gz ~/
tar xvf sakila-db.tar.gz
sudo mysql
SOURCE /home/ubuntu/sakila-db/sakila-schema.sql;
SOURCE /home/ubuntu/sakila-db/sakila-data.sql;
exit

# USE sakila; SHOW FULL TABLES; for testing the database sakila

# install sysbench
sudo apt-get install sysbench -y

sudo sysbench oltp_read_write --table-size=1000000 --mysql-db=sakila --mysql-user=root prepare
sudo sysbench oltp_read_write --table-size=1000000 --threads=6 --time=60 --max-requests=0 --mysql-db=sakila --mysql-user=root run