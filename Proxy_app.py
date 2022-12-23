from Proxy_sessions_setup import sessions

Client_request=sessions['mysql_cluster_master'].exec_command('sudo cat /home/ubuntu/request.sql')

request =Client_request

instances= ['mysql_cluster_master','mysql_cluster_slave1','mysql_cluster_slave2','mysql_cluster_slave3']

cmd = " sudo echo '" + str(request) + "' >> requests.sql && sudo /opt/mysqlcluster/home/mysqlc/bin/mysql -h 127.0.0.1 -u root < requests.sql"


stdin, stdout, stderr = sessions['mysql_cluster_master'].exec_command(cmd )
print('stdout:', stdout.read())
print('stderr:', stderr.read())

