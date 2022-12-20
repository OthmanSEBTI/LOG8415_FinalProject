import boto3
import os
from Key_pair import *
from Security_group import *
from Instance import *
from Instance_connect import *

'''
# create a key  
key_name = 'key' 
key_pair(key_name)

# create a security group
securityGroupId = security_group('security_group')

# create needed instances of type t2.micro
instances= ['mysql_standalone','mysql_cluster_master','mysql_cluster_slave1','mysql_cluster_slave2','mysql_cluster_slave3']

for instance in instances :
    create_instance(instance,securityGroupId,key_name)
'''
# start ssh seessions
sessions={}
instances= ['mysql_standalone','mysql_cluster_master','mysql_cluster_slave1','mysql_cluster_slave2','mysql_cluster_slave3']
key_name = 'key' 

for instance in instances :
    instanceId = retrieve_intanceId(instance)
    publicIp = retrieve_publicIp(instanceId)
    sessions[instance] = ssh_to_instance(key_name+'.pem',publicIp)