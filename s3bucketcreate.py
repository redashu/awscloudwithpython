import  boto3 # boto3 for creating resources in aws cloud
import time 
# function for creating bucket on S3 
s3=boto3.client('s3')
# connecting to aws s3 
'''
s3.create_bucket(Bucket="ashutoshhlnbbucket11")
# this will use secret and access key to connect & create 
time.sleep(3)
print("S3 bucket got create you can check in AWS Portal")
'''
## code for printing buckets 
response=s3.list_buckets()

for  i in  response['Buckets']:
    print(f,' {i["name"]}')




