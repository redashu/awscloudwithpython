import boto3
client = boto3.client('ec2')

response=client.run_instances(
    ImageId='ami-047a51fa27710816e',
    InstanceType='t2.micro',
    KeyName='macdocker',
    MinCount=1,
    MaxCount=1
)
print(response[0].id)

'''
# stopping instances 
st=client.stop_instances(InstanceIds=['i-0d1f0cd55d49ccf93','i-090bb6eb11a934ee3'])
print(st)
'''