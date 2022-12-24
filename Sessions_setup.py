from Instance_connect import *

key_name = 'key'

sessions={}
instances= ['mysql_standalone','mysql_cluster_master','mysql_cluster_slave1','mysql_cluster_slave2','mysql_cluster_slave3', 'Proxy']

# start ssh seessions for the environment deployment of cluster standalone and proxy
for instance in instances :
    instanceId = retrieve_intanceId(instance)
    publicIp = retrieve_publicIp(instanceId)
    sessions[instance] = ssh_to_instance(key_name+'.pem',publicIp)

instanceId = retrieve_intanceId('mysql_cluster_master')
publicIp = retrieve_publicIp(instanceId)
Master_second_session=ssh_to_instance(key_name+'.pem',publicIp)