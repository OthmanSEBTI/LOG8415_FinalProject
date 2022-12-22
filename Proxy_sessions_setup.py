from Instance_connect import *
key_name = '/home/ubuntu/LOG8415_FinalProject/key'

# start ssh seessions
sessions={}
instances= ['mysql_standalone','mysql_cluster_master','mysql_cluster_slave1','mysql_cluster_slave2','mysql_cluster_slave3', 'Proxy']



for instance in instances :
    instanceId = retrieve_intanceId(instance)
    publicIp = retrieve_publicIp(instanceId)
    sessions[instance] = ssh_to_instance(key_name+'.pem',publicIp)