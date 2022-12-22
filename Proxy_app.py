from Sessions_setup import sessions

instances= ['mysql_cluster_master','mysql_cluster_slave1','mysql_cluster_slave2','mysql_cluster_slave3']
List_of_requests =['CREATE DATABASE test1;','CREATE DATABASE test2;','CREATE DATABASE test3;','CREATE DATABASE test4;']

cmd = " sudo echo '" + str(List_of_requests[3]) + "' >> requests.sql && sudo /opt/mysqlcluster/home/mysqlc/bin/mysql -h 127.0.0.1 -u root < requests.sql"
sessions['mysql_cluster_master'].exec_command('touch requests.sql')

stdin, stdout, stderr = sessions['mysql_cluster_master'].exec_command(cmd )
print('stdout:', stdout.read())
print('stderr:', stderr.read())

sessions['mysql_cluster_master'].exec_command('rm requests.sql')