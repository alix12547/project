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




def create_bucket(bucket_name, profile_name, region, endpoint_url, cloud):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-west-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """
    
    

    # Create bucket
    try:
        
        # Use the following code to connect using Wasabi profile from .aws/credentials file
        
        session = boto3.Session(profile_name=profile_name)
        credentials = session.get_credentials()
        aws_access_key_id = credentials.access_key
        aws_secret_access_key = credentials.secret_key
        s3 = None
        if cloud == "amazon":
            s3 = boto3.client('s3',
                    region_name=region,
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key)
        else: 
            s3 = boto3.client('s3',
                    endpoint_url= endpoint_url,
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key)

        
        s3.create_bucket(Bucket=bucket_name)
        """if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)"""
    except ClientError as e:
        logging.error(e)
        return False
    return True

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
    #print("Random string of length", length, "is:", result_str)


def upload_file(file_name, bucket,content_type,profile, endpoint_url, region, cloud, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    session = boto3.Session(profile_name=profile)
    credentials = session.get_credentials()
    aws_access_key_id = credentials.access_key
    aws_secret_access_key = credentials.secret_key
    s3_client = None
    if cloud == "amazon":
        s3_client = boto3.client('s3',
                region_name=region,
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key)
    else: 

        s3_client = boto3.client('s3',
                endpoint_url= endpoint_url,
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key)


    
    # Upload the file
    #s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name, ExtraArgs={'ContentType': content_type,'ACL': 'public-read'})

    except ClientError as e:
        logging.error(e)
        return False
    return True


def creating_buckets():
    
    # clouds = {
    #     "amazon": "1- amazon (total ok account for now is " + str(len(accountsAmazon)) + ") \n",
    #     "wasabi" : "2- wasabi (total ok account for now is " + str(len(accountsWasabi)) + ") \n",
    # }
    
    #print(clouds.values())
    
    clouds = ["1- amazon  ( working account: " + str(len(accountsAmazon)) + " )", "2- wasabi ( working account: " + str(len(accountsWasabi)) + " )"]
    
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
    
    
    listOfRegion = ["us-west-1", "eu-west-1", "us-east-1", "us-east-2", "eu-west-1", "eu-west-2", "us-central-1", "ca-central-1"]
    if cloud == "amazon":
        regionEntered =  input("please enter the region name (leave empty for default ("+ region +"))  " + str(listOfRegion)  + ": ")
    else:
        regionEntered = "us-west-1"
    
    if len(regionEntered) == 0:
        regionEntered = region
    elif regionEntered not in listOfRegion:
        print("please enter a valid region name")
        return
        
    region = regionEntered

    
    contents = ""
    accountCount = 0
    for i in range(numberOfbuckets):
        bucket_name = get_random_string(30)
        # bucket_name = "rzscgfxoayvmcbjsmllitvbxu"
        print(bucket_name)
        
        
        
        profile_name = accountsList[accountCount]
        


        
        # create_bucket(bucket_name, profile_name, region, endpoint_url, cloud):
        if create_bucket(bucket_name, profile_name, region, endpoint_url, cloud) == False:
            accountsList.pop(accountCount)
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
            upload_file(diroffer + filename , bucket_name,content_type, profile_name,endpoint_url ,region, cloud, newname)
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
    creating_buckets()
    
    
    
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
            
        client = boto3.client('s3',
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
            accountsWasabi.append(df.iloc[i].profile)
        elif df.iloc[i].cloud == "amazon" and df.iloc[i].state == "ok":
            accountsAmazon.append(df.iloc[i].profile)
        
            
        
        
def setConfig():
    global endpointAmazon,maxCreationAmazon,pathAmazon,endpointWasabi,maxCreationWasabi,pathWasabi, regionAmazon, regionWasabi
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
    main()
    """ accounts = ["chevalierperot@outlook.de-wasabi2", "saWs2ss9ss9g@yahoo.com-wasabi", "mo.movahed2244@gmail.com"]
    profile_id = int(input("please enter profile index " + str(accounts) + ": "))
    
    
    profile_name = accounts[profile_id - 1]
    
    
    #getQuotaMax()
    creating_buckets()
    # deleteBuckets()
    #deleteBucketsOlderThan(profile_name,5)
    printBuckets() """
    
    