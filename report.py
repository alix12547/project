from asyncio.windows_events import NULL
from inspect import trace
from random import randint
from threading import Thread
from time import sleep
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
import os
from linereader import dopen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# ----------------------------------fonction for my project ----------------------------------
# function for check profil
listop=[]
def prf(i):

    options2 = uc.ChromeOptions()
    profile = "profile"+str(i)
    path = 'C:\\Users\\admin4\\AppData\\Roaming\\Google\\' + profile
    isExist = os.path.exists(path)
    options2.add_argument(
        '--no-first-run --no-service-autorun --password-store=basic')
    # check if profil exist open 
    if isExist != 0:
        # options2.add_experimental_option("prefs", {
        #     "profile.name": profile
        # })
        options2.add_argument('--user-data-dir='+path)
        # options2.add_argument('--proxy-server='+ proxy + ':92' )
       
        listop.append({"option":options2,"profil":profile,'index':i})
    

    
 
    
def spam(drivers,profil):
    try:
        # go to spam
        drivers.get("https://mail.google.com/mail/u/0/#spam")
        drivers.refresh()
        sleep(randint(6,8)) 
        try:
            rec=(drivers.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/h1/span').text)
            boit=(drivers.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div').text)
            print(rec+' for profil '+profil)
            if rec=="Confirmez qu'il s'agit bien de vous" or rec=="Verify it’s you":
                print("boit "+boit+" not connected : "+profil)
                sleep(10)
                print(profil+" close ")
                drivers.quit()
        except:pass
        task=0
        # check if proxy down
        try:
            if drivers.find_element(By.CSS_SELECTOR, 'span[jsvalues=".innerHTML:msg"]').text=='This site can’t be reached':
                print('proxy down for '+profil)
                sleep(10)
                print(profil+" close ")
                drivers.quit()
        except:pass
        # check if profil vide
        try:
            
            if drivers.find_element(By.CSS_SELECTOR, 'a[data-action="sign in"]').text=='Login':
                print(profil+' vide  ')
                sleep(10)
                print(profil+" close ")
                drivers.quit()
        except:pass                                

        # try:

        while True:
                try:drivers.find_element(By.CSS_SELECTOR, 'div[role="alertdialog"]>div:nth-child(3)>button:nth-child(2)').click()
                except:pass
                # refrech
                sleep(randint(2,3)) 
                WebDriverWait(drivers, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[act="20"]'))).click()
                check=False
                # try:rec=(drivers.find_element(By.CSS_SELECTOR, "table[role='grid']>tbody>tr:nth-child(1)>td:nth-child(5)>div>div>span").text).rstrip();check=True
                # except:pass
                # open msg spam
                sleep(randint(2,3))      
                drivers.find_element(By.CSS_SELECTOR, "table[role='grid']>tbody>tr:nth-child(1)").click()
                # click first link
                # try:
                #     if check==True:    
                #         sleep(randint(1,3))
                #         ct=drivers.find_element(By.XPATH, "//h2[.='"+rec[4:len(rec)]+"']")
                #         ct.click()
                #         sleep(randint(1,3))
                #         drivers.switch_to.window(drivers.window_handles[1])
                #         drivers.close()
                #         drivers.switch_to.window(drivers.window_handles[0])
                #         print("click in link ('_')")
                # except:pass
                if drivers.current_url!="https://mail.google.com/mail/u/0/#spam":
                    # click not spam
                    sleep(randint(1,3))
                    if randint(1, 10)%2!=0:      
                        drivers.find_element(By.CSS_SELECTOR, 'div[gh="mtb"]>div>div:nth-child(3)>div>div:nth-child(1)').click()
                    else:
                        drivers.find_element(By.CSS_SELECTOR, 'div[data-legacy-message-id]>div:nth-child(2)>div:nth-child(2)>div>div>div>div>button').click()

                    
                    task+=1
                print("task spam donne in"+profil)
        
    except:
        inbox(drivers,profil)
        pass
        
# ---------------------------------inbox---------------------------------


def inbox(drivers,profil) :
    # task inbox
    try:
        drivers.get("https://mail.google.com/mail/u/0/#inbox")
        task=0
        print("0 spam in "+profil)
        # try:       
        sleep(randint(1,3))   
        # check if boit disible
        try:
                rec=(drivers.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/h1/span').text)
                boit=(drivers.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div').text)
                print(rec+' for profil '+profil)
                if rec=="Confirmez qu'il s'agit bien de vous" or rec=="Verify it’s you":
                    print("boit "+boit+" not connected : "+profil)
                    sleep(10)
                    print(profil+" close ")
                    drivers.quit()
        except:
            pass
        # check if proxy down
        try:
            if drivers.find_element(By.CSS_SELECTOR, 'span[jsvalues=".innerHTML:msg"]').text=='This site can’t be reached':
                print('proxy down for '+profil)
                sleep(10)
                print(profil+" close ")
                drivers.quit()
        except:pass
        # check if profil vide
        try:
            
            if drivers.find_element(By.CSS_SELECTOR, 'a[data-action="sign in"]').text=='Login':
                print(profil+' vide  ')
                sleep(10)
                print(profil+" close ")
                drivers.quit()
        except:pass
        try:  
                                
            while True:
                    #chack spam
                        
                                    
                        try:
                            try:

                                if  drivers.find_element(By.CSS_SELECTOR,'div[data-tooltip="Spam"]>div>div>div').text!='':
                                    break
                                    
                            except:
                                drivers.find_element(By.CSS_SELECTOR, 'span[gh="mll"]').click()
                                if drivers.find_element(By.CSS_SELECTOR,'div[data-tooltip="Spam"]>div>div>div').text!='':
                                        break
                                        
                                        
                                            
                            
                        except:
                            pass
                            try:drivers.find_element(By.CSS_SELECTOR, 'div[role="alertdialog"]>div:nth-child(3)>button:nth-child(2)').click()
                            except:pass
                            check=False
                            try:rec=(drivers.find_element(By.CSS_SELECTOR, 'table[role="grid"]>tbody>tr:nth-child(1)>td:nth-child(5)>div>div>span').text).rstrip();check=True
                            except:pass
                            
                        # open mail inbox
                    
                            try:WebDriverWait(drivers, 6).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='tabpanel']>div:nth-child(2)>div>table[role='grid']>tbody>tr:nth-child(1)"))).click()
                            except:WebDriverWait(drivers, 6).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='main']>div:nth-child(5)>div:nth-child(1)>div:nth-child(1)>table[role='grid']>tbody>tr:nth-child(1)"))).click()
                                                                                                               
                            
                            sleep(randint(1,2))
                            if drivers.current_url!="https://mail.google.com/mail/u/0/#inbox":
                                # click first link
                                try:
                                    if check==True:    
                                        sleep(randint(1,3))
                                        ct=drivers.find_element(By.XPATH, "//h2[.='"+rec[4:len(rec)]+"']")
                                        ct.click()
                                        sleep(randint(1,3))
                                        drivers.switch_to.window(drivers.window_handles[1])
                                        drivers.close()
                                        drivers.switch_to.window(drivers.window_handles[0])
                                        print("click in link ('_')")
                                except:pass
                                # etoil 
                                if randint(1, 10)%2!=0:      
                                    WebDriverWait(drivers, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="gK"]>div[role="checkbox"]'))).click()
                                # Archive
                                sleep(randint(1,2))      
                                # document.querySelector('div[class="T-I J-J5-Ji lR T-I-ax7 T-I-Js-IF mA"]')
                                drivers.find_element(By.CSS_SELECTOR, 'div[gh="mtb"]>div>div:nth-child(2)>div:nth-child(1)').click()
                                task+=1
                            if task%5==0 and task!=0:
                                    for i in range(1,randint(1,20)) :
                                        try:drivers.find_element(By.CSS_SELECTOR, "div[role='tabpanel']>div:nth-child(2)>div>table[role='grid']>tbody>tr:nth-child("+str(i)+")>td:nth-child(2)").click()
                                        except:drivers.find_element(By.CSS_SELECTOR, "div[role='main']>div:nth-child(5)>div:nth-child(1)>div:nth-child(1)>table[role='grid']>tbody>tr:nth-child("+str(i)+")>td:nth-child(2)").click()

                                        
                                        task+=1
                                    # Archive
                                    sleep(randint(1,2))      
                                    try:drivers.find_element(By.CSS_SELECTOR, 'div[gh="mtb"]>div>div:nth-child(1)>div:nth-child(2)>div').click()
                                    except:pass
            spam(drivers,profil)
                    # except:pass    
        except:print("0 inbox in "+profil);sleep(randint(2,4));spam(drivers,profil)
    except:pass;print("probleme in "+profil)
        # except:pass;print('0 inbox in '+profil)
    
def repo(listop):
    try:
        lign = dopen('datasources\\profiles.txt').getline(listop['index'])
        proxy = lign.split(",")[0]
        listop['option'].add_argument('--proxy-server='+ proxy + ':92' )
        # print('proxy donne '+proxy+' in '+listop['profil']+'\n' )
        drivers = uc.Chrome(use_subprocess=True, options = listop['option'],version_main=106)
        drivers.minimize_window()
        drivers.maximize_window()
        profil=listop['profil']
        inbox(drivers,profil)
    except:print('faild open '+listop['profil']+' :/')
# ----------------------------------start my project ----------------------------------
print("----------------------------------Enter the required information----------------------------------")
pr_start = int(input("From which profile do you start?: "))
pr_end = int(input("Which profile to finish?: "))
# action_nb = int(input("How many action do you want?: "))
# pr_start=pr_end=action=1
for i in range(pr_start,pr_end+1):
        prf(i)
print(f"open {len(listop)} profil  donne........")
 
# for start script
for l in listop:
    p=Thread(target=repo,args=(l,))
    p.start()
    sleep(3)