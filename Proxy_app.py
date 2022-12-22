from Proxy_sessions_setup import sessions

Client_request= open('/home/ubuntu/LOG8415_FinalProject/Client_request', "r", encoding='utf-8')
Client_request= open('/home/ubuntu/LOG8415_FinalProject/Client_request', "w", encoding='utf-8')

request =Client_request.readlines()[0].strip('\n')

instances= ['mysql_cluster_master','mysql_cluster_slave1','mysql_cluster_slave2','mysql_cluster_slave3']

cmd = " sudo echo '" + str(request) + "' >> requests.sql && sudo /opt/mysqlcluster/home/mysqlc/bin/mysql -h 127.0.0.1 -u root < requests.sql"
sessions['mysql_cluster_master'].exec_command('touch requests.sql')

stdin, stdout, stderr = sessions['mysql_cluster_master'].exec_command(cmd )
print('stdout:', stdout.read())
print('stderr:', stderr.read())

sessions['mysql_cluster_master'].exec_command('rm requests.sql')