import boto3,time
myos=boto3.client('ec2')
# listing all the features and options under myos variable 
#print(dir(myos))
for  i  in dir(myos):
    if 'instance' in i:
        print(i)
## OR
#[i for i in dir(myos) if 'instance' in i]
print("creating Instance...")
time.sleep(3)
output=myos.run_instances(
    ImageId='ami-047a51fa27710816e',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='macdocker'
)
print(output)



