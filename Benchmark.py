import boto3
import os
import time

from Sessions_setup import sessions
from Sessions_setup import Master_second_session

#Launch Sysbench Benchmark on Standalone Server
stdin, stdout, stderr =sessions['mysql_standalone'].exec_command("sudo sysbench oltp_read_write --table-size=1000000 --mysql-db=sakila --mysql-user=root prepare ")
print('stdout:', stdout.read())
print('stderr:', stderr.read())

time.sleep(30)

start = time.time()

stdin, stdout, stderr =sessions['mysql_standalone'].exec_command("time sudo sysbench oltp_read_write --table-size=1000000 --threads=16 --max-requests=0 --mysql-db=sakila --mysql-user=root run")
print('stdout:', stdout.read())
print('stderr:', stderr.read())

end = time.time()

Standalone_exec_time = end - start 

#Launch Sysbench Benchmark on Cluster
stdin, stdout, stderr =sessions['mysql_cluster_slave1'].exec_command("sudo sysbench  oltp_read_write --num-threads=16 --max-requests=10000 --db-driver=mysql --mysql-host=ec2-54-210-201-233.compute-1.amazonaws.com --mysql-user=myapp2 --mysql-db=sakila --table-size=1000000 --max-requests=1000000  prepare")
print('stdout:', stdout.read())
print('stderr:', stderr.read())

time.sleep(30)

start = time.time()

stdin, stdout, stderr = sessions['mysql_cluster_slave1'].exec_command("time sudo sysbench  oltp_read_write --num-threads=16 --max-requests=10000 --db-driver=mysql --mysql-host=ec2-54-210-201-233.compute-1.amazonaws.com --mysql-user=myapp2 --mysql-db=sakila --table-size=1000000 --max-requests=1000000  run")
print('stdout:', stdout.read())
print('stderr:', stderr.read())

end = time.time()

Cluster_exec_time = end - start

print ('Mysql standalone execution time :', Standalone_exec_time)
print ('Mysql cluster execution time :', Cluster_exec_time)
