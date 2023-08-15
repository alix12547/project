import datetime
import random
from threading import Thread
from time import sleep
import csv
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.remote.webelement import WebElement


# ----------------------------------fonction for my project ----------------------------------
# function for check profil
listop=[]
def prf(i):

    options2 = uc.ChromeOptions()
    profile = "profile"+str(i)
    path = 'C:\\Users\\admin4\\\AppData\\Roaming\\Google\\' + profile
    isExist = os.path.exists(path)
    # options2.headless=True
    # options2.add_argument('--headless')
    options2.add_argument(
        '--no-first-run --no-service-autorun --password-store=basic')
    # check if profil exist open 
    if isExist != 0:
        # options2.add_experimental_option("prefs", {
        #     "profile.name": profile
        # })
        options2.add_argument('--user-data-dir='+path)
        listop.append({"option":options2,"profil":profile,'index':i})
    

    
# function for slow tiping 
def slow_type(element: WebElement, text: str):
    for character in text:
        element.send_keys(character)
        sleep(0.005)    
    

def sendemail(listop):
    boit=[]
    subject=[]
    messages=[]
    with open('datasources/profiles.txt','r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                index=0
                for row in csv_reader:
                        profil=row[2]
                        if index==listop['index']-1:
                            listop['option'].add_argument('--proxy-server='+ row[0] + ':92' )
                            print('proxy donne '+row[0]+' in '+listop['profil']+'\n' )
                            break
                        index+=1
    drivers = uc.Chrome(use_subprocess=True, options = listop['option'],version_main=106)
    drivers.minimize_window()
    drivers.maximize_window()
    drivers.get("https://mail.google.com/mail/u/0/#inbox")
   
    # stock donne in array
    with open(data, encoding="utf8") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=';')
                for row in csv_reader:
                    try:
                        boit.append(row[0])
                        subject.append(row[1])
                        messages.append(row[2])
                    finally:
                        boit=list(filter(None,boit))
                        subject=list(filter(None,subject))
                        messages=list(filter(None,messages))
    

    # strat taske 
    try:    
                sleep(3)
                boits=(drivers.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div').text)
                print("boit "+boits+" not connected : "+listop['profil'])
                sleep(10)
                print(listop['profil']+" close ")
                drivers.quit()
    except:
        pass    
        for i in range(1,nb_message+1):
            while True:
                bt=boit[random.randint(0,len(boit)-1)]
                if bt==profil:continue
                else:break
            sub=subject[random.randint(0,len(subject)-1)]
            msg=messages[random.randint(0,len(messages)-1)]
            try:
                
                
                if i <= nb_message:
                        # ------------------------send email-----------------------
                        print(f'Message {str(i)} for : '+str(listop['profil']))
                        #click in compose
                        sleep(random.randint(2,3))   
                        drivers.find_element(By.XPATH, "//div[@class='T-I T-I-KE L3']").click()
                        if(str.__contains__(drivers.current_url, 'compose=new')):
                                sleep(random.randint(2,3))
                                # add TO                        
                                slow_type(drivers.find_elements(By.XPATH, '//input[@type="text"]')[3],bt.lower())
                                sleep(random.randint(2,3))
                                # add subject
                                slow_type(drivers.find_elements(By.TAG_NAME, 'input')[11], sub)
                                sleep(random.randint(2,3))
                                # add messages
                                slow_type(drivers.find_element(By.XPATH, '//div[contains(@class, "Am Al editable LW-avf tS-tW")]'), msg)
                                sleep(random.randint(2,3))
                                # click send
                                drivers.find_element(By.XPATH, '/html/body/div[*]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]').click()
                                sleep(random.randint(2,3))
                                # save historique
                                f = open("datasources/historique.txt", "a")
                                f.write(profil+' send email from : '+str(bt)+' at time : '+str(datetime.datetime.now())+'\n')
                                f.close() 
                                # send  Message
                                print(f"send    {str(i)} for : "+str(listop['profil']))   
                                sleep(random.randint(3,5)) 
                                i += 1        
                if i == nb_message:
                    print(str(listop['profil'])+" finish ........")
                    drivers.quit()
                    break
                try:
                    limite="Vous avez atteint la limite d'envoi d'e-mails. Votre message n'a pas été envoyé."
                    limite2="You have reached a limit for sending mail. Your message was not sent."
                    txt=drivers.find_element(By.CSS_SELECTOR, 'table[role="grid"]>tbody>tr:nth-child(1)>td:nth-child(5)>div>div>span').text
                    if(str.__contains__(txt, limite) or str.__contains__(txt, limite2)):
                        print(listop['profil']+" limite de send a "+str(i))
                        drivers.quit()
                        break
                except:pass
            except:
                pass
                sleep(3)
                drivers.get("https://mail.google.com/mail/u/0/#inbox")
                print("errer"+str(i)+'in :'+str(listop['profil']))

    
    
                       
                       
                






                      

# ----------------------------------start my project ----------------------------------
print("----------------------------------Enter the required information----------------------------------")
pr_start = int(input("From which profile do you start?: "))
pr_end = int(input("Which profile to finish?: "))
nb_message = int(input("How many messages do you want to send?: "))
data='datasources\\data.txt'
f=len(open(data, 'r', encoding="mbcs").readlines())
for i in range(pr_start,pr_end+1):
        prf(i)
print(f"creat {len(listop)} profil  donee........")
 
# for start script
for l in listop:
    p=Thread(target=sendemail,args=(l,))
    p.start()
    sleep(1)