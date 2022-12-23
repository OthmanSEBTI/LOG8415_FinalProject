from Proxy_sessions_setup import sessions
import random
from ping3 import ping
import time

instances= ['mysql_cluster_master','mysql_cluster_slave1','mysql_cluster_slave2','mysql_cluster_slave3']
ip_adresses = {'mysql_cluster_master':'ec2-54-210-201-233.compute-1.amazonaws.com', 
'mysql_cluster_slave1':'ec2-44-206-228-96.compute-1.amazonaws.com', 
'mysql_cluster_slave2':'ec2-54-173-199-68.compute-1.amazonaws.com',
'mysql_cluster_slave3':'ec2-3-86-253-19.compute-1.amazonaws.com'}

ping_time={}

for instance in instances:
    start=time.time()
    ping(ip_adresses[instance])
    end=time.time()
    ping_time[instance]=end-start

temp = min(ping_time.values())
res = [key for key in ping_time if ping_time[key] == temp]

instance = res[0]



Client_request = open('/home/ubuntu/request.sql', mode="r", encoding="utf-8")
# Client_request=sessions['mysql_cluster_master'].exec_command('sudo echo /home/ubuntu/request.sql')

request = Client_request.readlines()[0]


cmd = " sudo echo '" + str(request) + "' >> requests.sql && sudo /opt/mysqlcluster/home/mysqlc/bin/mysql -h ec2-35-174-156-89.compute-1.amazonaws.com -u myapp2 < requests.sql"


stdin, stdout, stderr = sessions[instance].exec_command(cmd )
print('stdout:', stdout.read())
print('stderr:', stderr.read())

sessions[instance].exec_command("sudo rm requests.sql" )

