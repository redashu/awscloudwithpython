# LNB by Techienest 

## getting started 

<img src="start.png">

## CLOUd model

<img src="cl.png">

## vendors of cloud 

<img src="vendor.png">

## Cloud model of services 

<img src="services.png">

## CLoud request methods 

<img src="clreq.png">


## Connecting remote OS 

<img src="rdpssh.png">

## COnfigure aws cli on Windows / linux / Mac 

```
root@3b141354c513:/# aws  configure 
AWS Access Key ID [****************B76P]: AKIAQ4OUTXWCQPAUMD6U                    
AWS Secret Access Key [****************NDyP]: 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
Default region name [us-east-1]: 
Default output format [None]: 

```

## check it by connecting s3 

```
root@3b141354c513:/# 
root@3b141354c513:/# aws  s3  ls
2019-06-02 17:33:43 elasticbeanstalk-ap-south-1-061112302981
2019-07-05 02:54:13 elasticbeanstalk-us-east-1-061112302981
2020-01-10 12:54:00 elasticbeanstalk-us-east-2-061112302981
2019-11-02 11:30:24 elasticbeanstalk-us-west-2-061112302981

```

## PYthon to create S3 Bucket 

<img src="s3.png">

## creating bucket 

```
import  boto3 # boto3 for creating resources in aws cloud
import time 
# function for creating bucket on S3 
s3=boto3.client('s3')
# connecting to aws s3 
s3.create_bucket(Bucket="ashutoshhlnbbucket11")
# this will use secret and access key to connect & create 
time.sleep(3)
print("S3 bucket got create you can check in AWS Portal")


```

