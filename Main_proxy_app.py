import boto3
import os
import time
from Sessions_setup import sessions
from Sessions_setup import Master_second_session

# input the proxy mode
Proxy_mode = str(input("Please enter the proxy mode : "))

# proxy mode direct hit
if Proxy_mode == "direct hit" :
    while(True):
        # read the client request
        var = str(input("Please enter request : "))
        # send request to the proxy
        stdin, stdout, stderr =sessions['Proxy'].exec_command('sudo echo ' + "'" + str(var) + "'" + ' >> /home/ubuntu/request.sql')
        print('stdout:', stdout.read())
        print('stderr:', stderr.read())
        # execute the proxy selected mode
        stdin, stdout, stderr =sessions['Proxy'].exec_command("python3 /home/ubuntu/LOG8415_FinalProject/Proxy_app_direct_hit.py")
        print('stdout:', stdout.read())
        print('stderr:', stderr.read())

        sessions['Proxy'].exec_command("sudo rm request.sql")

# proxy mode random
elif Proxy_mode=="random" :
    while(True):
        var = str(input("Please enter request : "))

        stdin, stdout, stderr =sessions['Proxy'].exec_command('sudo echo ' + "'" + str(var) + "'" + ' >> /home/ubuntu/request.sql')
        print('stdout:', stdout.read())
        print('stderr:', stderr.read())
        
        stdin, stdout, stderr =sessions['Proxy'].exec_command("python3 /home/ubuntu/LOG8415_FinalProject/Proxy_app_random.py")
        print('stdout:', stdout.read())
        print('stderr:', stderr.read())

        sessions['Proxy'].exec_command("sudo rm request.sql")

# proxy mode customize
elif Proxy_mode=="customize" :
    while(True):
        var = str(input("Please enter request : "))

        stdin, stdout, stderr =sessions['Proxy'].exec_command('sudo echo ' + "'" + str(var) + "'" + ' >> /home/ubuntu/request.sql')
        print('stdout:', stdout.read())
        print('stderr:', stderr.read())
        
        stdin, stdout, stderr =sessions['Proxy'].exec_command("sudo python3 /home/ubuntu/LOG8415_FinalProject/Proxy_app_customize.py")
        print('stdout:', stdout.read())
        print('stderr:', stderr.read())

        sessions['Proxy'].exec_command("sudo rm request.sql")