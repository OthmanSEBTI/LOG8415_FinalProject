from Proxy_sessions_setup import sessions
import random

Client_request = open('/home/ubuntu/request.sql', mode="r", encoding="utf-8")
# Client_request=sessions['mysql_cluster_master'].exec_command('sudo echo /home/ubuntu/request.sql')

request = Client_request.readlines()[0]

instances= ['mysql_cluster_slave1','mysql_cluster_slave2','mysql_cluster_slave3']

random_slave=random.choice(instances)

cmd = " sudo echo '" + str(request) + "' >> requests.sql && sudo /opt/mysqlcluster/home/mysqlc/bin/mysql -h ec2-54-210-201-233.compute-1.amazonaws.com -u myapp2 < requests.sql"


stdin, stdout, stderr = sessions[random_slave].exec_command(cmd )
print('stdout:', stdout.read())
print('stderr:', stderr.read())

sessions[random_slave].exec_command("sudo rm requests.sql" )

