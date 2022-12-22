import boto3
import paramiko

def retrieve_intanceId(instanceName):
    ec2_resource = boto3.resource('ec2', region_name="us-east-1")

    instances= ec2_resource.instances.all()

    # For each insteance with a tag
    for instance in instances:
        for tag in instance.tags:
            if tag['Key'] == 'Name' and tag['Value'] == instanceName:
                instanceId=instance.id
    return(instanceId)

def retrieve_publicIp(instanceId):
    ec2_client = boto3.client('ec2', region_name="us-east-1")
    reservations = ec2_client.describe_instances(InstanceIds=[
            instanceId,
        ])
    publicIpAddress = reservations['Reservations'][0]['Instances'][0]['PublicIpAddress']
    return (publicIpAddress)

def ssh_to_instance(key,publicIpAddress):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    privkey = paramiko.RSAKey.from_private_key_file(
            key)
    ssh.connect(hostname=publicIpAddress,
                        username='ubuntu', pkey=privkey)
    return ssh

# ssh.exec_command("mkdir test1")






