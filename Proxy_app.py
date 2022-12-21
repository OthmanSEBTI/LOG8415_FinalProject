from Infrastructure_setup import sessions

instances= ['mysql_cluster_master','mysql_cluster_slave1','mysql_cluster_slave2','mysql_cluster_slave3']
List_of_requests =['CREATE DATABASE test1;','CREATE DATABASE test2;','create databse test3;','create databse test4;']

cmd = " sudo echo '" + str(List_of_requests[1]) + "' >> requests.sql"
sessions['mysql_cluster_master'].exec_command('touch requests')

stdin, stdout, stderr = sessions['mysql_cluster_master'].exec_command(cmd )
print('stdout:', stdout.read())
print('stderr:', stderr.read())

sessions['mysql_cluster_master'].exec_command('sudo /opt/mysqlcluster/home/mysqlc/bin/mysql -h 127.0.0.1 -u root -p < requests.sql')