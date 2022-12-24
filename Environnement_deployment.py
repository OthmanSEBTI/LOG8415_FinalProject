import boto3
import os
import time
from Sessions_setup import sessions
from Sessions_setup import Master_second_session

instances= ['mysql_standalone','mysql_cluster_master','mysql_cluster_slave1','mysql_cluster_slave2','mysql_cluster_slave3']


# setup mysql standalone instance
sessions['mysql_standalone'].exec_command("sudo apt-get update")
stdin, stdout, stderr =sessions['mysql_standalone'].exec_command("sudo git clone https://github.com/OthmanSEBTI/LOG8415_FinalProject.git && sudo bash /home/ubuntu/LOG8415_FinalProject/Standalone_setup/Install_mysql_sakila.sh && sudo mysql < /home/ubuntu/LOG8415_FinalProject/Standalone_setup/Sakila_setup.sql")
print('stdout:', stdout.read())
print('stderr:', stderr.read())


# setup mysql master node
sessions['mysql_cluster_master'].exec_command("sudo apt-get update")
stdin, stdout, stderr =sessions['mysql_cluster_master'].exec_command("sudo git clone https://github.com/OthmanSEBTI/LOG8415_FinalProject.git && sudo bash /home/ubuntu/LOG8415_FinalProject/Cluster_setup/Common_steps.sh && sudo bash /home/ubuntu/LOG8415_FinalProject/Cluster_setup/Master_setup.sh")
print('stdout:', stdout.read())
print('stderr:', stderr.read())

# setup slaves node
for instance in instances[2:]:
    sessions[instance].exec_command("sudo apt-get update")
    stdin, stdout, stderr =sessions[instance].exec_command("sudo git clone https://github.com/OthmanSEBTI/LOG8415_FinalProject.git && sudo bash /home/ubuntu/LOG8415_FinalProject/Cluster_setup/Common_steps.sh && sudo bash /home/ubuntu/LOG8415_FinalProject/Cluster_setup/Slave_setup.sh")
    print('stdout:', stdout.read())
    print('stderr:', stderr.read())



# back to mysql master node
stdin, stdout, stderr =sessions['mysql_cluster_master'].exec_command("cd /opt/mysqlcluster/home/mysqlc && sudo scripts/mysql_install_db --no-defaults --datadir=/opt/mysqlcluster/deploy/mysqld_data")
print('stdout:', stdout.read())
print('stderr:', stderr.read())

Master_second_session.exec_command("sudo /opt/mysqlcluster/home/mysqlc/bin/mysqld --defaults-file=/opt/mysqlcluster/deploy/conf/my.cnf --user=root &")

time.sleep(30)

stdin, stdout, stderr =sessions['mysql_cluster_master'].exec_command("/opt/mysqlcluster/home/mysqlc/bin/mysql -h 127.0.0.1 -u root < /home/ubuntu/LOG8415_FinalProject/Cluster_setup/mysql_user.sql")
print('stdout:', stdout.read())
print('stderr:', stderr.read())

#install sysbench in the cluster instances
for instance in instances[1:]:
    stdin, stdout, stderr =sessions[instance].exec_command("sudo apt-get install sysbench -y")
    print('stdout:', stdout.read())
    print('stderr:', stderr.read())

#install sakila db in the master
stdin, stdout, stderr =sessions['mysql_cluster_master'].exec_command("cp /home/ubuntu/LOG8415_FinalProject/sakila-db.tar.gz /home/ubuntu/ & sudo tar xvf /home/ubuntu/sakila-db.tar.gz")
print('stdout:', stdout.read())
print('stderr:', stderr.read())

stdin, stdout, stderr =sessions['mysql_cluster_master'].exec_command("/opt/mysqlcluster/home/mysqlc/bin/mysql -h 127.0.0.1 -u root < /home/ubuntu/LOG8415_FinalProject/Cluster_setup/Install_sakila.sql")
print('stdout:', stdout.read())
print('stderr:', stderr.read())

# Proxy setup and launch
sessions['Proxy'].exec_command("sudo apt-get update")
stdin, stdout, stderr =sessions['Proxy'].exec_command("sudo git clone https://github.com/OthmanSEBTI/LOG8415_FinalProject.git && sudo bash /home/ubuntu/LOG8415_FinalProject/Proxy_setup.sh ")
print('stdout:', stdout.read())
print('stderr:', stderr.read())
stdin, stdout, stderr =sessions['Proxy'].exec_command("python3 /home/ubuntu/LOG8415_FinalProject/Proxy_sessions_setup.py ")
print('stdout:', stdout.read())
print('stderr:', stderr.read())





 




