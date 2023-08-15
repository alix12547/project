import logging
import numbers
from pprint import pprint
import boto3
from botocore.exceptions import ClientError
import os
import random
import string
from os import walk
import tempfile
import datetime
import csv
import time
import pytz
import pandas as pd
import botocore
from pathlib import Path
import json
from botocore.config import Config

def delete_bucket_completely(bucket_name,profile_name, region, endpoint_url, cloud, profile_proxy):

    try:           
        # Use the following code to connect using Wasabi profile from .aws/credentials file
        
        session = boto3.Session(profile_name=profile_name)
        credentials = session.get_credentials()
        aws_access_key_id = credentials.access_key
        aws_secret_access_key = credentials.secret_key
        s3 = None
        if cloud == "amazon":
            s3 = boto3.client('s3',
                    config=Config(proxies={'https': profile_proxy}),
                    region_name=region,
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key)
        else: 
            s3 = boto3.client('s3',
                    config=Config(proxies={'https': profile_proxy}),
                    endpoint_url= endpoint_url,
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key)

        
        
    except ClientError as e:
        logging.error(e)
        return False

    #client = boto3.client('s3')
    try: 
        response = s3.list_objects_v2(
            Bucket=bucket_name,
        )
    except ClientError as e:
        logging.error(e)
        return False

    while response['KeyCount'] > 0:
        print('Deleting %d objects from bucket %s' % (len(response['Contents']),bucket_name))
        response = s3.delete_objects(
            Bucket=bucket_name,
            Delete={
                'Objects':[{'Key':obj['Key']} for obj in response['Contents']]
            }
        )
        response = s3.list_objects_v2(
            Bucket=bucket_name,
        )

    print('Now deleting bucket %s' % bucket_name)
    response = s3.delete_bucket(
        Bucket=bucket_name
    )
    
    
def deleteBuckets(profile_name, region, endpoint_url, cloud, profile_proxy):
    with open('buckets.txt', 'r') as csvfile:
        data = list(csv.reader(csvfile))
    
    for row in data:
        
        #print(row[0])  
        
        try:
            
            # Use the following code to connect using Wasabi profile from .aws/credentials file
            
            session = boto3.Session(profile_name=profile_name)
            credentials = session.get_credentials()
            aws_access_key_id = credentials.access_key
            aws_secret_access_key = credentials.secret_key
            s3 = None
            if cloud == "amazon":
                s3 = boto3.resource('s3',
                        config=Config(proxies={'https': profile_proxy}),
                        region_name=region,
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key)
            else: 
                s3 = boto3.resource('s3',
                        config=Config(proxies={'https': profile_proxy}),
                        endpoint_url= endpoint_url,
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key)

            
            # Print out bucket names
            for bucket in s3.buckets.all():
                bucket_name = row[0]
                #print(bucket_name)
                #print(bucket.name)
                if bucket_name.strip() == bucket.name.strip():
                    
                    print(bucket.name)
                    delete_bucket_completely(bucket_name,profile_name, region, endpoint_url, cloud, profile_proxy)
                    #print(bucket.name)
                
            
        except ClientError as e:
            logging.error(e)
            return False
        
    
def deleteBucketsOlderThan(profile_name, region, endpoint_url, cloud, profile_proxy, day):
    
    try:
        day = day + 1
        tod = datetime.datetime.now()
        d = datetime.timedelta(days = day)
        old_date = tod - d
        session = boto3.Session(profile_name=profile_name)
        credentials = session.get_credentials()
        aws_access_key_id = credentials.access_key
        aws_secret_access_key = credentials.secret_key

        client = None
        if cloud == "amazon":
            client = boto3.client('s3',
                    config=Config(proxies={'https': profile_proxy}),
                    region_name=region,
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key)
        else: 
            client = boto3.client('s3',
                    config=Config(proxies={'https': profile_proxy}),
                    endpoint_url= endpoint_url,
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key)
        
        response = client.list_buckets()
        utc=pytz.UTC
        count = 0
        # Print out bucket names
        for bucket in response['Buckets']:
            bucket_name = bucket["Name"]
            creation_date = bucket["CreationDate"]
            #print(type(creation_date))
            if utc.localize(old_date) > creation_date:
                print(str(creation_date) + " " + bucket_name)
                delete_bucket_completely(bucket_name,profile_name, region, endpoint_url, cloud, profile_proxy)
                count += 1
                
        print("the buckets older than " + str(old_date) + " was deleted, number of buckets deleted is " + str(count))   
        
    except ClientError as e:
        logging.error(e)
        return False
    return True



def create_bucket(bucket_name, profile_name, region, endpoint_url, cloud, profile_proxy):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-west-1).

    :param bucket_name: Bucket to create
    :param profile_name: Profile name associated with the IAM user
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :param endpoint_url: Endpoint URL for non-AWS S3-compatible service
    :param cloud: Cloud provider ('amazon' or 'other')
    :param profile_proxy: Proxy configuration for the profile
    :return: True if bucket created, else False
    """
    try:
        session = boto3.Session(profile_name=profile_name)
        s3 = None
        if cloud == "amazon":
            s3 = session.client('s3', region_name=region)
        else:
            s3 = session.client('s3', endpoint_url=endpoint_url)

        s3.create_bucket(Bucket=bucket_name)

        # Set the bucket policy to allow public read access
        bucket_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": "s3:GetObject",
                    "Principal": "*",
                    "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*REGION*"
                }
            ]
        }

        bucket_policy_str = json.dumps(bucket_policy)
        s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy_str)

    except ClientError as e:
        error_message = str(e)
        if "Missing required field Principal" not in error_message and "Policy has invalid resource" not in error_message:
            raise
        else:
            logging.info("Ignoring error: %s", error_message)
            print("Ignoring error: %s", error_message)

    return True



def upload_file(file_name, bucket, content_type, profile, endpoint_url, region, cloud, profile_proxy, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified, file_name is used
    :return: True if file was uploaded, else False
    """
    if object_name is None:
        object_name = os.path.basename(file_name)

    session = boto3.Session(profile_name=profile)
    credentials = session.get_credentials()
    aws_access_key_id = credentials.access_key
    aws_secret_access_key = credentials.secret_key
    s3_client = None
    if cloud == "amazon":
        s3_client = boto3.client(
            's3',
            config=Config(proxies={'https': profile_proxy}),
            region_name=region,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )
    else:
        s3_client = boto3.client(
            's3',
            config=Config(proxies={'https': profile_proxy}),
            endpoint_url=endpoint_url,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )

    try:
        response = s3_client.upload_file(
            file_name,
            bucket,
            object_name,
            ExtraArgs={'ContentType': content_type}
        )

        # Set the uploaded object's ACL to public-read
        if response and 'ResponseMetadata' in response:
            object_url = f"https://{bucket}.s3.amazonaws.com/{object_name}"
            s3_client.put_object_acl(
                Bucket=bucket,
                Key=object_name,
                ACL='public-read'
            )
            print(f"File uploaded successfully and is publicly accessible at: {object_url}")
            return True

    except ClientError as e:
        logging.error(e)
        print(f"Error details: {e}")
        return False


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
    #print("Random string of length", length, "is:", result_str)

def deleteBucketsOlderThan(profile_name, region, endpoint_url, cloud, profile_proxy, day):
    
    day = day + 1
    tod = datetime.datetime.now()
    d = datetime.timedelta(days = day)
    old_date = tod - d
    session = boto3.Session(profile_name=profile_name)
    credentials = session.get_credentials()
    aws_access_key_id = credentials.access_key
    aws_secret_access_key = credentials.secret_key

    client = None
    if cloud == "amazon":
        client = boto3.client('s3',
                config=Config(proxies={'https': profile_proxy}),
                region_name=region,
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key)
    else: 
        client = boto3.client('s3',
                config=Config(proxies={'https': profile_proxy}),
                endpoint_url= endpoint_url,
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key)
    
    response = client.list_buckets()
    utc=pytz.UTC
    count = 0
    # Print out bucket names
    for bucket in response['Buckets']:
        bucket_name = bucket["Name"]
        creation_date = bucket["CreationDate"]
        #print(type(creation_date))
        if utc.localize(old_date) > creation_date:
            print(str(creation_date) + " " + bucket_name)
            delete_bucket_completely(bucket_name,profile_name, region, endpoint_url, cloud, profile_proxy)
            count += 1
            
    print("the buckets older than " + str(old_date) + " was deleted, number of buckets deleted is " + str(count))

def deleteBucketsInFile():
    clouds = ["1- amazon  ( working account: " + str(len(accountsAmazon)) + " )", "2- wasabi ( working account: " + str(len(accountsWasabi)) + " )"
              ,  "3- backblaze ( working account: " + str(len(accountsBackblaze)) + " )"]
    try:
        profile_id = int(input("please enter cloud index " + str(clouds) + ": "))
    except ValueError as e:
        logging.error(e)
        return
    
    if profile_id > len(clouds):
        logging.error("please enter a valid number")
        return
    cloud = ""
    if profile_id == 1:
        cloud = "amazon"
    elif profile_id == 2:
        cloud = "wasabi"
    elif profile_id == 3:
        cloud = "backblaze"
    
    
    region = ""
    accountsList = []
    endpoint_url = ""
    if cloud == "amazon":
        maxBuckets = maxCreationAmazon
        path = pathAmazon
        region = regionAmazon
        accountsList = accountsAmazon
        endpoint_url = endpointAmazon
    elif cloud == "wasabi":
        maxBuckets = maxCreationWasabi
        path = pathWasabi
        region = regionWasabi
        accountsList = accountsWasabi
        endpoint_url = endpointWasabi
    elif cloud == "backblaze":
        maxBuckets = maxCreationBackblaze
        path = pathBackblaze
        region = regionBackblaze
        accountsList = accountsBackblaze
        endpoint_url = endpointBackblaze
    
    #print(accountsList)
    #profile_id = int(input("please enter profile index " + str(accountsList) + ": "))

    
    # profile_name = accountsList[profile_id][0]
    # profile_proxy = accountsList[profile_id][1]
    #print(profile_name)
    
    for i in range(len(accountsList)):
        print(i)
        profile_name = accountsList[i][0]
        profile_proxy = accountsList[i][1]
        deleteBuckets(profile_name, region, endpoint_url, cloud, profile_proxy)
        
def deletingByDay():
    clouds = ["1- amazon  ( working account: " + str(len(accountsAmazon)) + " )", "2- wasabi ( working account: " + str(len(accountsWasabi)) + " )"
              ,  "3- backblaze ( working account: " + str(len(accountsBackblaze)) + " )"]
    try:
        profile_id = int(input("please enter cloud index " + str(clouds) + ": "))
    except ValueError as e:
        logging.error(e)
        return
    
    try:
        days = int(input("please enter how old the buckets you want to delete (min: 2): "))
    except ValueError as e:
        logging.error(e)
        return
    if (days < 2):
        print("you can not delete buckets please select older day: ")
        return
    
    if profile_id > len(clouds):
        logging.error("please enter a valid number")
        return
    cloud = ""
    if profile_id == 1:
        cloud = "amazon"
    elif profile_id == 2:
        cloud = "wasabi"
    elif profile_id == 3:
        cloud = "backblaze"
    
    
    region = ""
    accountsList = []
    endpoint_url = ""
    if cloud == "amazon":
        maxBuckets = maxCreationAmazon
        path = pathAmazon
        region = regionAmazon
        accountsList = accountsAmazon
        endpoint_url = endpointAmazon
    elif cloud == "wasabi":
        maxBuckets = maxCreationWasabi
        path = pathWasabi
        region = regionWasabi
        accountsList = accountsWasabi
        endpoint_url = endpointWasabi
    elif cloud == "backblaze":
        maxBuckets = maxCreationBackblaze
        path = pathBackblaze
        region = regionBackblaze
        accountsList = accountsBackblaze
        endpoint_url = endpointBackblaze 
    for i in range(len(accountsList)):
        print(i)
        profile_name = accountsList[i][0]
        profile_proxy = accountsList[i][1]
        deleteBucketsOlderThan(profile_name, region, endpoint_url, cloud, profile_proxy, days)
    


def creating_buckets():
    
    # clouds = {
    #     "amazon": "1- amazon (total ok account for now is " + str(len(accountsAmazon)) + ") \n",
    #     "wasabi" : "2- wasabi (total ok account for now is " + str(len(accountsWasabi)) + ") \n",
    # }
    
    #print(clouds.values())
    
    clouds = ["1- amazon  ( working account: " + str(len(accountsAmazon)) + " )", "2- wasabi ( working account: " + str(len(accountsWasabi)) + " )"
              ,  "3- backblaze ( working account: " + str(len(accountsBackblaze)) + " )"]
    
    try:
        profile_id = int(input("please enter cloud index " + str(clouds) + ": "))
    except ValueError as e:
        logging.error(e)
        return
    
    if profile_id > len(clouds):
        logging.error("please enter a valid number")
        return
    cloud = ""
    if profile_id == 1:
        cloud = "amazon"
    elif profile_id == 2:
        cloud = "wasabi"
    elif profile_id == 3:
        cloud = "backblaze"
    
    
    
    
    maxBuckets = 0
    path = ""
    region = ""
    accountsList = []
    endpoint_url = ""
    if cloud == "amazon":
        maxBuckets = maxCreationAmazon
        path = pathAmazon
        region = regionAmazon
        accountsList = accountsAmazon
        endpoint_url = endpointAmazon
    elif cloud == "wasabi":
        maxBuckets = maxCreationWasabi
        path = pathWasabi
        region = regionWasabi
        accountsList = accountsWasabi
        endpoint_url = endpointWasabi
    elif cloud == "backblaze":
        maxBuckets = maxCreationBackblaze
        path = pathBackblaze
        region = regionBackblaze
        accountsList = accountsBackblaze
        endpoint_url = endpointBackblaze
        
  
    numberOfbuckets = int(input("Number of buckets(max: "+ str(maxBuckets) +"): "))

    if numberOfbuckets > maxBuckets :
        print("max buckets is : " + str(maxBuckets) )
        return
    
    if numberOfbuckets > 100 :
        print("max buckets is 100 if you change settings")
        return
    
    
    

    
    offer = input("offer folder: ")
    
    
    if checkDir(path + offer) == False:
        return
    
    
    listOfRegion = ["us-west-1", "eu-west-1", "us-east-1", "us-east-2", "eu-west-1", "eu-west-2", "us-central-1", "ca-central-1", "us-west-002"]
    if cloud == "amazon":
        regionEntered =  input("please enter the region name (leave empty for default ("+ region +"))  " + str(listOfRegion)  + ": ")
    elif cloud == "wasabi":
        regionEntered = "us-west-1"
    elif cloud == "backblaze":
        regionEntered = "us-west-002"
    
    if len(regionEntered) == 0:
        regionEntered = region
    elif regionEntered not in listOfRegion:
        print("please enter a valid region name")
        return
        
    region = regionEntered

    
    contents = ""
    accountCount = 0
    if len(accountsList) < 1:
        print("no accounts found")
        return
    for i in range(numberOfbuckets):
        bucket_name = get_random_string(30)
        # bucket_name = "rzscgfxoayvmcbjsmllitvbxu"
        print(bucket_name)
        
        #print(accountsList)
        
        profile_name = accountsList[accountCount][0]
        profile_proxy = accountsList[accountCount][1]
        


        
        # create_bucket(bucket_name, profile_name, region, endpoint_url, cloud):
        if create_bucket(bucket_name, profile_name, region, endpoint_url, cloud, profile_proxy) == False:
            #print("account list count before:" + str(len(accountsList)))
            accountsList.pop(accountCount)
            accountCount += 1
            if accountCount >= len(accountsList):
                accountCount = 0
            continue
            
        
        
        accountCount += 1
        if accountCount >= len(accountsList):
            accountCount = 0
        offerPath = path + offer
        filenames = next(walk(offerPath), (None, None, []))[2]  # [] if no file
        utc_datetime = datetime.datetime.utcnow()
        #print(filenames)
        for filename in filenames:
            
            #print(filename)
            # this will return a tuple of root and extension
            split_tup = os.path.splitext(filename)

            
            # extract the file name and extension
            file_name = split_tup[0]
            file_extension = split_tup[1]
            
            
            #print("File Name: ", file_name)
            #print("File Extension: ", file_extension)
            

            file_name = file_name.replace("_", "")

                
            newname = bucket_name + file_name + file_extension

            diroffer = offerPath + '\\'
            content_type = "image/png"
            if file_extension == ".html":
                content_type = "text/html"
            #upload_file(file_name, bucket,content_type,profile, endpoint_url, region, cloud, object_name=None):
            upload_file(diroffer + filename , bucket_name,content_type, profile_name,endpoint_url ,region, cloud, profile_proxy, newname)
            utc_datetime = datetime.datetime.utcnow()
            
        
        contents += "You Created Bucket " + str(bucket_name) + " with "  + str(len(filenames)) + " files in profile " + profile_name +", in this offer " + str(offer) + " " + str(utc_datetime) +  " \n"
        #print(contents)
    mailerId = input("your id: ")
    f = open( "extraction\\" + mailerId + ".txt", "a")
    f.write(contents)
    f.close()

    os.system('start notepad++.exe extraction\\' + mailerId + ".txt")        
                





def main():
    
    setConfig()
    checkProfiles()
    
    try:
        action = int(input("1- create buckets \n 2- delete buckets by name \n 3- delete by date \n"))
    except ValueError as e:
        logging.error(e)
        return
    
    if action > 3:
        logging.error("please enter a valid number")
        return
    cloud = ""
    if action == 1:
        creating_buckets()
    elif action == 2:
        deleteBucketsInFile()
    elif action == 3:
        deletingByDay()
    #creating_buckets()
    #deleteBucketsInFile()
    #deletingByDay()
    
    
    
def checkProfiles():
    
    
    global accountsAmazon, accountsWasabi
    # read profile data from csv file
    df = pd.read_csv('datasources\\profiles.csv')
    for i in range(len(df)):
        try:
            session = boto3.Session(profile_name=df.iloc[i].profile)
        except botocore.exceptions.ProfileNotFound as e:
            df.loc[i, "state"] = "profile_not_found"
            df.to_csv("datasources\\profiles.csv", index=False)
            #logging.error(e)
            continue
            
        
        
        session = boto3.Session(profile_name=df.iloc[i].profile)
        credentials = session.get_credentials()
        aws_access_key_id = credentials.access_key
        aws_secret_access_key = credentials.secret_key
        endpoint = ""
        if df.iloc[i].cloud == "wasabi":
            endpoint = "https://s3.wasabisys.com"
        elif df.iloc[i].cloud == "amazon": 
            endpoint = "https://s3.amazonaws.com"
        elif df.iloc[i].cloud == "backblaze": 
            endpoint = "https://s3.us-west-002.backblazeb2.com"
            
        client = boto3.client('s3',
                    config=Config(proxies={'https': df.iloc[i].proxy}),
                    endpoint_url=endpoint,
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key) 
        

        try:
            response = client.list_buckets()
            if response:
                df.loc[i, "state"] = "ok"
                df.to_csv("datasources\\profiles.csv", index=False)
        except botocore.exceptions.ClientError as e:
            df.loc[i, "state"] = "not_ok"
            df.to_csv("datasources\\profiles.csv", index=False)
            #logging.error(e)
            continue
            
    df = pd.read_csv('datasources\\profiles.csv')
    
    for i in range(len(df)):
        if df.iloc[i].cloud == "wasabi" and df.iloc[i].state == "ok":
            accountsWasabi.append([df.iloc[i].profile, df.iloc[i].proxy])
        elif df.iloc[i].cloud == "amazon" and df.iloc[i].state == "ok":
            accountsAmazon.append([df.iloc[i].profile, df.iloc[i].proxy])
        elif df.iloc[i].cloud == "backblaze" and df.iloc[i].state == "ok":
            accountsBackblaze.append([df.iloc[i].profile, df.iloc[i].proxy])
        
            
        
        
def setConfig():
    global endpointAmazon,maxCreationAmazon,pathAmazon,endpointWasabi,maxCreationWasabi,pathWasabi, regionAmazon, regionWasabi
    global endpointBackblaze,maxCreationBackblaze,pathBackblaze,regionBackblaze
    my_file = Path("myconfig.json")
    if my_file.is_file() == False:
        return
    
    # Opening JSON file
    f = open('myconfig.json')
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    for row in data['settings']:
        
        try:
            if row["cloud"] == "amazon":

                endpointAmazon = row["endpoint"]
                maxCreationAmazon = row["maxcreation"]
                pathAmazon = row["path"]
                regionAmazon = row["regionDefault"]
                # Closing file
            elif row["cloud"] == "wasabi":
                endpointWasabi = row["endpoint"]
                maxCreationWasabi = row["maxcreation"]
                pathWasabi = row["path"]
                regionWasabi = row["regionDefault"]
            elif row["cloud"] == "backblaze":
                endpointBackblaze = row["endpoint"]
                maxCreationBackblaze = row["maxcreation"]
                pathBackblaze = row["path"]
                regionBackblaze = row["regionDefault"]
                # Closing file
        except KeyError as e:
            #logging.error(e)
            pass
            
        
    # Closing file
    f.close()    
    


    
        

        
        
            
        
def checkDir(dir):

    filenames = next(walk(dir), (None, None, []))[2]  # [] if no file
    if len(filenames) <= 0:
        print("Folder "+ dir +" Not Found Or It's Empty")
        return False
    else:
        return True
    

if __name__ == '__main__':
    
    maxCreationWasabi = None
    maxCreationAmazon = None
    endpointWasabi = "https://s3.wasabisys.com"
    endpointAmazon = "https://s3.amazonaws.com"
    pathAmazon = "C:\\Users\\admin\\Documents\\s3-cli\\offers"
    pathWasabi = "C:\\Users\\admin\\Documents\\s3-cli\\offers"
    regionWasabi = "us-west-1"
    regionAmazon = "us-east-1"
    accountsAmazon = []
    accountsWasabi = []
    maxCreationBackblaze = None
    endpointBackblaze = "https://s3.us-west-002.backblazeb2.com"
    pathBackblaze = "C:\\Users\\admin\\Documents\\s3-cli\\offers"
    regionBackblaze = "us-west-002"
    accountsBackblaze = []
    main()
    #print(accountsWasabi[0][1])
    """ accounts = ["chevalierperot@outlook.de-wasabi2", "saWs2ss9ss9g@yahoo.com-wasabi", "mo.movahed2244@gmail.com"]
    profile_id = int(input("please enter profile index " + str(accounts) + ": "))
    
    
    profile_name = accounts[profile_id - 1]
    
    
    #getQuotaMax()
    creating_buckets()
    #deleteBuckets()
    #deleteBucketsOlderThan(profile_name,5)
    printBuckets() """
    
    