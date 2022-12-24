import boto3

# creating security groups with necessary rules
def security_group(securityGroupName):
        
        ec2_client = boto3.client('ec2', region_name="us-east-1")

        response = ec2_client.describe_vpcs()
        vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')

        response = ec2_client.create_security_group(GroupName=securityGroupName,
                                                Description='DESCRIPTION',
                                                VpcId=vpc_id)

        security_group_id = response['GroupId']

        data = ec2_client.authorize_security_group_ingress(
                GroupId=security_group_id,
                IpPermissions=[
                {'IpProtocol': 'tcp',
                'FromPort': 1186,
                'ToPort': 30000,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                'FromPort': 30000,
                'ToPort': 65535,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                'FromPort': 0,
                'ToPort': 1186,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                'FromPort': 22,
                'ToPort': 22,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
                ])

        data = ec2_client.authorize_security_group_egress(
                GroupId=security_group_id,
                IpPermissions=[
                {'IpProtocol': 'tcp',
                'FromPort': 1186,
                'ToPort': 30000,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                'FromPort': 30000,
                'ToPort': 65535,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                'FromPort': 0,
                'ToPort': 1186,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                ])

        return(security_group_id)

