import boto3
import os

def key_pair(keyName): 
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    key_pair = ec2_client.create_key_pair(KeyName=keyName)

    private_key = key_pair["KeyMaterial"]
    
    # write private key to file with 400 permissions
    with os.fdopen(os.open(keyName+".pem", os.O_WRONLY | os.O_CREAT, 0o400), "w+") as handle:
        handle.write(private_key)