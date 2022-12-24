from Proxy_sessions_setup import sessions
import random

# read the requests 
Client_request = open('/home/ubuntu/request.sql', mode="r", encoding="utf-8")

# select a random slave instance
request = Client_request.readlines()[0]
instances= ['mysql_cluster_slave1','mysql_cluster_slave2','mysql_cluster_slave3']

random_slave=random.choice(instances)

# forward the request to the selected slave
cmd = " sudo echo '" + str(request) + "' >> requests.sql && sudo /opt/mysqlcluster/home/mysqlc/bin/mysql -h ec2-54-210-201-233.compute-1.amazonaws.com -u myapp2 < requests.sql"
stdin, stdout, stderr = sessions[random_slave].exec_command(cmd )
print('stdout:', stdout.read())
print('stderr:', stderr.read())
sessions[random_slave].exec_command("sudo rm requests.sql" )

