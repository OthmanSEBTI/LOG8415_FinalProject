from Proxy_sessions_setup import sessions

# read the requests 
Client_request = open('/home/ubuntu/request.sql', mode="r", encoding="utf-8")
request = Client_request.readlines()[0]

# forward the request to the master
cmd = " sudo echo '" + str(request) + "' >> requests.sql && sudo /opt/mysqlcluster/home/mysqlc/bin/mysql -h 127.0.0.1 -u root < requests.sql"
stdin, stdout, stderr = sessions['mysql_cluster_master'].exec_command(cmd )
print('stdout:', stdout.read())
print('stderr:', stderr.read())
sessions['mysql_cluster_master'].exec_command("sudo rm requests.sql" )

