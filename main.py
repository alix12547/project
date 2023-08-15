import random
import string
from google_nav_def import *
from connectage_def import *



    
def call_connectage():
    profiles_file="datasources\\boith.txt"
    path_creation ="C:\\Users\\admin4\\\AppData\\Roaming\\Google\\boith\\"
    e=False
    while(e!=True):
        try:
            pr_start = int(input("From which profile do you start?: "))
            pr_end = int(input("Which profile to finish?: "))
            print('open '+str((pr_end-pr_start)+1)+' profil')
            wait_profiles=   input(">> profiles wait number : ") 
           
            if(wait_profiles==""):
                wait_profiles = int((pr_end-pr_start)+1)
            else:
                wait_profiles =int(wait_profiles)
            
            
            e=True
        except:
            print("input erreur !") 
            sleep(0.5) 
            clear()
            e=False
            
            
    
    load_profiles_c(pr_start,pr_end,profiles_file,path_creation)
    
    google_theard_c()
    start_wait_theard_c(wait_profiles)
    out=input("press eny key to quit script  .....")
    
     
    
def call_google():
    profiles_file="datasources\\profiles.txt"
    path_creation ="C:\\Users\\admin4\\\AppData\\Roaming\\Google\\"
    # f=len(open(profiles_file, 'r').readlines())
    keyword_file="datasources\\keyword_searsh.txt"
    e=False
    while(e!=True):
        try:
            pr_start = int(input("From which profile do you start?: "))
            pr_end = int(input("Which profile to finish?: "))
            print('open '+str((pr_end-pr_start)+1)+' profil')
           
            wait_profiles=   input(">> profiles wait number : ") 
            if(wait_profiles==""):
                wait_profiles = int((pr_end-pr_start)+1)
            else:
                wait_profiles =int(wait_profiles)
                
                
                    
            navigate_count = int  (input(">> How many time do you want to profile navigated in google ?: "))
            nb_message = int  (input(">> How many messages do you want to send?: "))
           
          
            
            
            
           
            e=True
        except:
        
            print("input erreur !") 
            sleep(0.5) 
            clear()
            e=False
            
            
    
    load_profiles(pr_start,pr_end,profiles_file,path_creation)
    
    google_theard(keyword_file,nb_message,navigate_count)
    
    start_wait_theard(wait_profiles)
    
    
    
     
    
 
################______main_______################
 





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
    clear()
    call_google()
elif (choix==2):
    clear()
    call_connectage()
 
 
    





#################################################




 

 




    
  