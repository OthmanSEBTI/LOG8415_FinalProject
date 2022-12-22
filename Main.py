import boto3
import os

from Sessions_setup import sessions

instances= ['mysql_standalone','mysql_cluster_master','mysql_cluster_slave1','mysql_cluster_slave2','mysql_cluster_slave3']

'''
# setup mysql standalone instance
sessions['mysql_standalone'].exec_command("sudo apt-get update")
stdin, stdout, stderr =sessions['mysql_standalone'].exec_command("sudo git clone https://github.com/OthmanSEBTI/LOG8415_FinalProject.git && sudo bash /home/ubuntu/LOG8415_FinalProject/Standalone_setup/Install_mysql_sakila.sh && sudo mysql < /home/ubuntu/LOG8415_FinalProject/Standalone_setup/Sakila_setup.sql")
print('stdout:', stdout.read())
print('stderr:', stderr.read())
# launch sysbench on mysql standalone instance and measure execution time
stdin, stdout, stderr =sessions['mysql_standalone'].exec_command("sudo sysbench oltp_read_write --table-size=1000000 --mysql-db=sakila --mysql-user=root prepare && time sudo sysbench oltp_read_write --table-size=1000000 --threads=6 --time=60 --max-requests=0 --mysql-db=sakila --mysql-user=root run")
print('stdout:', stdout.read())
print('stderr:', stderr.read())

# sessions['mysql_standalone1'].exec_command("sudo mysql < /home/ubuntu/LOG8415_FinalProject/Standalone_setup/Sakila_setup.sql")
# stdin, stdout, stderr =sessions['mysql_standalone1'].exec_command("sudo sysbench oltp_read_write --table-size=1000000 --mysql-db=sakila --mysql-user=root prepare && sudo sysbench oltp_read_write --table-size=1000000 --threads=6 --time=60 --max-requests=0 --mysql-db=sakila --mysql-user=root run")

'''
'''
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
stdin, stdout, stderr =sessions['mysql_cluster_master'].exec_command("cd /opt/mysqlcluster/home/mysqlc && sudo scripts/mysql_install_db --no-defaults --datadir=/opt/mysqlcluster/deploy/mysqld_data && sudo /opt/mysqlcluster/home/mysqlc/bin/mysqld --defaults-file=/opt/mysqlcluster/deploy/conf/my.cnf --user=root &")
print('stdout:', stdout.read())
print('stderr:', stderr.read())


stdin, stdout, stderr =sessions['mysql_cluster_master'].exec_command("/opt/mysqlcluster/home/mysqlc/bin/mysql -h 127.0.0.1 -u root < /home/ubuntu/LOG8415_FinalProject/Cluster_setup/mysql_user.sql")
print('stdout:', stdout.read())
print('stderr:', stderr.read())


#install sysbench in the cluster instances
for instance in instances[2:]:
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


#Launch Benchmark
stdin, stdout, stderr =sessions['mysql_cluster_slave1'].exec_command("sudo sysbench  oltp_read_write --num-threads=16 --max-requests=10000 --db-driver=mysql --mysql-host=ec2-18-234-103-147.compute-1.amazonaws.com --mysql-user=myapp2 --mysql-db=sakila --table-size=1000000 --max-requests=1000000  prepare & time sudo sysbench  oltp_read_write --num-threads=16 --max-requests=10000 --db-driver=mysql --mysql-host=ec2-18-234-103-147.compute-1.amazonaws.com --mysql-user=myapp2 --mysql-db=sakila --table-size=1000000 --max-requests=1000000  run")
print('stdout:', stdout.read())
print('stderr:', stderr.read())

'''

# Proxy setup and launch
sessions['Proxy'].exec_command("sudo apt-get update")
stdin, stdout, stderr =sessions['Proxy'].exec_command("sudo git clone https://github.com/OthmanSEBTI/LOG8415_FinalProject.git && sudo bash /home/ubuntu/LOG8415_FinalProject/Proxy_setup.sh ")
print('stdout:', stdout.read())
print('stderr:', stderr.read())
stdin, stdout, stderr =sessions['Proxy'].exec_command("python3 /home/ubuntu/LOG8415_FinalProject/Proxy_sessions_setup.py & python3 /home/ubuntu/LOG8415_FinalProject/Proxy_app.py")
print('stdout:', stdout.read())
print('stderr:', stderr.read())