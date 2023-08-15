import datetime
from random import *
from threading import Thread
from time import sleep
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
import os
from linereader import dopen
from selenium.webdriver.remote.webelement import WebElement

# ----------------------------------fonction for my project ----------------------------------
# function for check profil
listop=[]

def profiles(i):
    try:
            lign = dopen(file).getline(i)
            proxy = lign.split(",")[0]
            profileName = lign.split(",")[1]
            email=lign.split(",")[2]
            password=lign.split(",")[3]
            path="C:\\Users\\admin4\\AppData\\Roaming\\Google\\"+profileName
            options = uc.ChromeOptions()
            isExist = os.path.exists(path)
            options.add_argument(
                '--no-first-run --no-service-autorun --password-store=basic')
            if isExist == 0:
                options.add_experimental_option("prefs", {
                    "profile.name": profileName
                })
            # options.headless=True
            # options.add_argument('--headless')
            options.add_argument('--user-data-dir='+path)
            # options.headless=True
            # options.add_argument('--headless')
            options.add_argument('--proxy-server='+ proxy + ':92' )
            listop.append({
                "password":password,
                "profileName": profileName,
                "option": options,
                'email':email,


            })
    except Exception as e:
        print('Exception:  ' + str(e))
def max_min(drivers):
    drivers.minimize_window()
    drivers.maximize_window()
    sleep(randint(2, 6))
def slow_type(element: WebElement, text: str):
    for character in text:
        element.send_keys(character)
        sleep(0.005)    
def disble(listop):
 drivers = uc.Chrome(use_subprocess=True, options=listop['option'],version_main=106)
 email=listop['email']
 max_min(drivers)
 sleep(randint(10,32)) 
 while True:               
    try:
                try:
                    validi=" Validez votre identité"
                    if validi== drivers.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/h1').text :
                        print(email+" valid phone "+listop['profileName'])
                        break
                    else:pass
                except:pass
    #     rec=(drivers.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/h1/span').text)
    #     if rec=="Confirmez qu'il s'agit bien de vous":
    #         try: 
                drivers.get("https://mail.google.com/mail/u/0/#inbox")
                max_min(drivers) 

                # suivant
                try:  
                    if drivers.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/button').text=='Adresse e-mail oubliée ?':
                                        drivers.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
                                        max_min(drivers)                                    
                except:pass
                try:drivers.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/button').click()
                except:drivers.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
                # add pass
                max_min(drivers)               
                pasw=drivers.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
                max_min(drivers)
                slow_type(pasw,listop['password'])  
                max_min(drivers)
                drivers.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
                # Commencer l'appel
                max_min(drivers)
                drivers.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
                try:
                    max_min(drivers)
                    deja=drivers.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div[2]/div/div[1]/div/form/span/section/div/div/div[1]').text
                    if deja!="Vous avez déjà soumis une demande à l'équipe Comptes Google.":
                     # suivant
                        max_min(drivers)
                        drivers.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/button').click()
                        # add message
                        max_min(drivers)
                        addmessage=drivers.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div/div[1]/div[2]/textarea')
                        message=dopen("datasources\\messages.txt").getline(randint(1,  int(len(open("datasources\\messages.txt", 'r').readlines()))        ))
                        slow_type(addmessage,message)
                        # suivant
                        # max_min(drivers)
                        # drivers.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/button').click()        
                        max_min(drivers)
                        boitadd=dopen("datasources\\boit.txt").getline(randint(1,int(len(open("datasources\\boit.txt", 'r').readlines()))))  
                        # add boit
                        addboit=drivers.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div[1]/div/div[1]/input')
                        slow_type(addboit,boitadd)
                        # fine
                        # drivers.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/button').click()         
                        f = open("datasources/historique_disbl.txt", "a")
                        f.write(f"this email : {email} recouvry : {boitadd} at time : {datetime.datetime.now()}\n")
                        f.close() 
                        print(f"this email : {email} recouvry : {boitadd}")   
                        sleep(randint(3,5))
                        drivers.quit()
                        break
                        
                    else:
                        print("deja reported "+email) 
                        drivers.quit()
                        break 
                except:
                    print("deja reported "+email) 
                    drivers.quit()
                    break      
    #         except:
    #             pass
    #             print("error in "+listop["profileName"])
            
    except Exception as e:
        # print('Exception:  ' + str(e))
        print("probleme in : "+listop['profileName'])
        sleep(randint(10,32))
        continue
        # sleep(100)
        # print(listop['profileName']+" close ")
        # drivers.quit()
 sleep(6000)




print("----------------------------------Enter the required information----------------------------------")
pr_start = int(input("From which profile do you start?: "))
pr_end = int(input("Which profile to finish?: "))
file="datasources\\profiles.txt"
for i in range(pr_start,pr_end+1):
        profiles(i)
print(f"open {len(listop)} profil  donne........")
 
# for start script
for l in listop:
    p=Thread(target=disble,args=(l,))
    p.start()
    sleep(1)