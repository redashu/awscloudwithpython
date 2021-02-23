import boto3,time
from botocore.exceptions import ClientError
s3_client = boto3.client('s3')
'''
#s3_client.create_bucket(Bucket="ashutoshhbkt007")
#time.sleep(4)
s3_client.delete_object(Bucket='mybucketname', Key='obc1')
time.sleep(2)
'''
s3_client.delete_bucket(Bucket='ashutoshhbkt007')
