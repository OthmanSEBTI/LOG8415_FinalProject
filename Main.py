import boto3
import os
from Key_pair import *
from Security_group import *
from Instance import *
from Instance_connect import *

"""
# create a key  
key_name = 'key' 
key_pair(key_name)

# create a security group
securityGroupId = security_group('securityGroup')

# create needed instances of type t2.micro
instances= ['mysql_standalone','mysql_cluster_master','mysql_cluster_slave1','mysql_cluster_slave2','mysql_cluster_slave3']

for instance in instances :
    create_instance(instance,securityGroupId,key_name)

"""

key_name = 'key' 

instances= ['mysql_standalone','mysql_cluster_master','mysql_cluster_slave1','mysql_cluster_slave2','mysql_cluster_slave3']

sessions={}

for instance in instances :
    instanceId = retrieve_intanceId(instance)
    publicIp = retrieve_publicIp(instanceId)
    sessions[instance] = ssh_to_instance(key_name+'.pem',publicIp)

#sessions['mysql_standalone'].exec_command("sudo apt-get update")
#sessions['mysql_standalone'].exec_command("sudo git clone https://github.com/OthmanSEBTI/LOG8415_FinalProject.git")

#stdin, stdout, stderr = sessions['mysql_standalone'].exec_command("cd /home/ubuntu/LOG8415_FinalProject/Standalone_setup; sudo bash ./test.sh ")
stdin, stdout, stderr = sessions['mysql_standalone'].exec_command("sudo bash /home/ubuntu/LOG8415_FinalProject/Standalone_setup/test.sh ")

print('stdout:', stdout.read())
print('stderr:', stderr.read())
