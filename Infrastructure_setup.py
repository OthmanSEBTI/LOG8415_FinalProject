import boto3
import os
from Key_pair import *
from Security_group import *
from Instance import *
from Instance_connect import *

def Infrastructure_setup():
    # create a key  
    key_name = 'key' 
    key_pair(key_name)

    # create a security group
    securityGroupId = security_group('security_group1')

    # create needed instances of type t2.micro
    instances= ['mysql_standalone','mysql_cluster_master','mysql_cluster_slave1','mysql_cluster_slave2','mysql_cluster_slave3','Proxy']

    for instance in instances :
        create_instance(instance,securityGroupId,key_name)