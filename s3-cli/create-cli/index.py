import os

def main():
    with open('cloud_accounts.csv') as accounts_file:
        accounts = [line.strip().split(',') for line in accounts_file]
    #print(df.iloc[1].rdp_name)
    contents = "profile,cloud,state,proxy \n"
    
    f = open( "profiles.csv", "w")
    f.write(contents)
    i = 0
    for account in accounts:
        i = i + 1
        if i == 1:
            continue
        
        cloud = account[1]
        state = account[2]
        proxy = account[6]
        cli_access_key_id = account[3]
        cli_access_key = account[4]
        default_region = account[5]
        profile_name = account[0]
    
        command = "aws configure set aws_access_key_id " + str(cli_access_key_id) + " --profile " + str(profile_name) + " && aws configure set aws_secret_access_key " + str(cli_access_key) + "  --profile " + str(profile_name) + " && aws configure set region " + str(default_region) + " --profile " + str(profile_name) 
    
        print(command)
        os.system(command)
        contents = str(profile_name) + "," + str(cloud) + "," + str(state) + "," + proxy + "\n"
        f.write(contents)
    f.close() 
    os.system("profiles.csv")   

if __name__ == '__main__':
    main()