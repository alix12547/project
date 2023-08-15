import random
import string
from google_nav_def import *
from connectage_def import *

path_creation ="C:\\Users\\admin4\\\AppData\\Roaming\\Google\\"

    
def call_connectage():
    path_creation ="C:\\Users\\admin4\\\AppData\\Roaming\\Google\\all\\"
    profiles_file="datasources\\conect.txt"
    e=False
    while(e!=True):
        try:
            pr_start = int(input("From which profile do you start?: "))
            pr_end = int(input("Which profile to finish?: "))
            print(f"creat {pr_end-pr_start+1} profiles")
            wait_profiles= input(">> profiles wait number : ")
            if wait_profiles=='':wait_profiles=(pr_end-pr_start)+1
            else :int(wait_profiles)
            e=True
        except:
            print("input erreur !") 
            sleep(0.5) 
            clear()
            e=False
            
            
    
    load_profiles_c(pr_start,pr_end,profiles_file,path_creation)
    
    google_theard_c()
    
    start_wait_theard_c(wait_profiles)
def call_google():
    profiles_file="datasources\\profiles.txt"
    # f=len(open(profiles_file, 'r').readlines())
    keyword_file="datasources\\keyword_searsh.txt"
    e=False
    while(e!=True):
        try:
            pr_start = int(input("From which profile do you start?: "))
            pr_end = int(input("Which profile to finish?: "))
            print('open '+str((pr_end-pr_start)+1)+' profil')
            # if pr_end>f:pr_end=f
            wait_profiles= input(">> profiles wait number : ")
            if wait_profiles=='':wait_profiles=(pr_end-pr_start)+1
            else :int(wait_profiles)
            nb_message = int(input(">> How many messages do you want to send?: "))
            e=True
        except:
            print("input erreur !") 
            sleep(0.5) 
            clear()
            e=False
            
            
    
    load_profiles(pr_start,pr_end,profiles_file,path_creation)
    
    google_theard(keyword_file,nb_message)
    
    start_wait_theard(wait_profiles)
    
    
    print('sleep')
    sleep(60)
    
    #started_index= int(input("profile index started : "))
    
    
    
    
# _subjects= dopen(path_subjects).getline(randint(1,len(open(path_subjects, 'r'))).replace('[random]',''+ ''.join(random.choice(string.ascii_letters) for i in range(10))))

################______main_______################
# call_connectage()
# call_google()
 
e=False
while(e!=True):
    try:
        print("#########################################\n")
        print("press (1) if you want to use warmup  \n")
        print("press (2) if you want to use connectage  \n")
        print("#########################################\n")
        choix=int(input("your choice ?:  "))
        e=True
        if(choix not in [1,2]):
            print("choice invalid !") 
            sleep(0.5) 
            clear()
            e=False
    except:
            print("choice invalid !") 
            sleep(0.5) 
            clear()
            e=False


if (choix==1):
    call_google()
elif (choix==2):
    call_connectage()





#################################################




 

 




    
  