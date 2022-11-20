sudo service mysqld stop
sudo apt remove mysql-server mysql mysql-devel
sudo mkdir -p /opt/mysqlcluster/home
cd /opt/mysqlcluster/home
sudo wget http://dev.mysql.com/get/Downloads/MySQL-Cluster-7.2/mysql-cluster-gpl-7.2.1-linux2.6-x86_64.tar.gz
sudo tar xvf mysql-cluster-gpl-7.2.1-linux2.6-x86_64.tar.gz
sudo ln -s mysql-cluster-gpl-7.2.1-linux2.6-x86_64 mysqlc
sudo echo ‘export MYSQLC_HOME=/opt/mysqlcluster/home/mysqlc’ >> /etc/profile.d/mysqlc.sh
sudo echo ‘export PATH=$MYSQLC_HOME/bin:$PATH’ >> /etc/profile.d/mysqlc.sh
sudo source /etc/profile.d/mysqlc.sh