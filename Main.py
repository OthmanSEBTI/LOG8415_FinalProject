import boto3
import os
from Key_pair import *
from Security_group import *
from Instance import *
from Instance_connect import *
from Infrastructure_setup import sessions

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

