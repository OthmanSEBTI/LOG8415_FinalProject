#install mysql
sudo apt-get update
sudo apt-get install mysql-server -y
sudo mysql

#install sakila
sudo git clone https://github.com/OthmanSEBTI/LOG8415_FinalProject.git
cp ~/LOG8415_FinalProject/sakila-db.tar.gz ~/
tar xvf sakila-db.tar.gz
sudo mysql
SOURCE /home/ubuntu/sakila-db/sakila-schema.sql;
SOURCE /home/ubuntu/sakila-db/sakila-data.sql;
