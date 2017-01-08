import boto3

__author__ = 'vikrame'

connection = boto3.client(
    'emr',
    region_name='us-east-1',
    aws_access_key_id='XXXXXXXXXXXXXXXXXXX',
    aws_secret_access_key='XXXXXXXXXXXXXXXXXXX',
)

cluster_id = connection.run_job_flow(
    Name='test_emr_job_with_boto3',
    LogUri='s3://XXXXXXXXXXXXXXXXXXX/',
    ReleaseLabel='emr-5.2.0',
    Instances={
        'InstanceGroups': [
            {
                'Name': "Master nodes",
                'Market': 'ON_DEMAND',
                'InstanceRole': 'MASTER',
                'InstanceType': 'm1.large',
                'InstanceCount': 1,
            },
            {
                'Name': "Slave nodes",
                'Market': 'ON_DEMAND',
                'InstanceRole': 'CORE',
                'InstanceType': 'm1.large',
                'InstanceCount': 2,
            }
        ],
        'Ec2KeyName': 'XXXXXXXXXXXXXXXXXXX',
        'KeepJobFlowAliveWhenNoSteps': True,
        'TerminationProtected': False,
        'Ec2SubnetId': 'subnet-58482875',
    },
    Steps=[],
    VisibleToAllUsers=True,
    JobFlowRole='EMR_EC2_DefaultRole',
    ServiceRole='EMR_DefaultRole',
    Tags=[
        {
            'Key': 'tag_name_1',
            'Value': 'tab_value_1',
        },
        {
            'Key': 'tag_name_2',
            'Value': 'tag_value_2',
        },
    ],
)

print (cluster_id['JobFlowId'])
