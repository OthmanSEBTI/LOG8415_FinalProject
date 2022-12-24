import boto3

#create instance of type t2.micro and ubuntu 22.04 image
def create_instance(instanceName,secGroupId,keyName):
    ec2_resource = boto3.resource('ec2', region_name="us-east-1")
    ec2_resource.create_instances(
        MinCount = 1,
        MaxCount = 1,
        ImageId="ami-0574da719dca65348",
        InstanceType='t2.micro',
        KeyName=keyName,
        SecurityGroupIds = [secGroupId],
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': instanceName
                    },
                ]
            },
        ]
    )




