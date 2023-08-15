import csv
import datetime
import random
from threading import Thread
from time import sleep
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
import os

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
    # try:
        
        drivers.get("https://www.youtube.com/watch?v=k2o-PZb2IQQ&list=PLayxbg1BHkA4k771z1CdtNiI3CvERd4fw&index=3")
        print('open '+str(profil))
        while True:
            print('')
        count=0
        # go to spam
        # drivers.get("https://mail.google.com/mail/u/0/#spam")
        # drivers.minimize_window()
        # drivers.maximize_window()
        # print('open '+str(profil))
        # sleep(random.randint(6,8)) 
        # while count<200:
        #     # 1<=int(drivers.find_element(By.XPATH, "/html/body/div[*]/div[3]/div/div[2]/div[*]/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/span/div[1]/span/span[2]").text):
        #     try:
        #         check=False
        #         try:
        #             rec=(drivers.find_element(By.XPATH, '/html/body/div[*]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[4]/div[1]/div/table/tbody/tr[1]/td[5]/div/div/span').text).rstrip()
        #             check=True
        #         except:pass
        #         # open msg spam
        #         sleep(random.randint(4,6))      
        #         drivers.find_element(By.XPATH, "/html/body/div[*]/div[3]/div/div[2]/div[*]/div/div/div/div/div[2]/div/div[1]/div/div[*]/div[4]/div[1]/div/table/tbody/tr[1]").click()
        #         # click first link
        #         if check==True:
        #             try:
        #                     sleep(random.randint(4,6))
        #                     ct=drivers.find_element(By.XPATH, "//h2[.='"+rec[4:len(rec)]+"']")
        #                     ct.click()
        #                     sleep(random.randint(4,6))
        #                     drivers.switch_to.window(drivers.window_handles[1])
        #                     drivers.close()
        #                     drivers.switch_to.window(drivers.window_handles[0])
        #                     print("click in link ('_')")
        #                     check=False
        #             except:pass
        #         if drivers.current_url!="https://mail.google.com/mail/u/0/#spam":
        #             # click not spam
        #             sleep(random.randint(4,6))      
        #             drivers.find_element(By.XPATH, "/html/body/div[*]/div[3]/div/div[2]/div[*]/div/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div/div").click()
        #         count+=1
        #     except:
        #         drivers.get("https://mail.google.com/mail/u/0/#spam")
        #         drivers.maximize_window()                             
        #         try:drivers.find_element(By.XPATH, "/html/body/div[*]/div[3]/div/div[2]/div[*]/div/div/div/div/div[1]/div[*]/div[2]/div[1]/div/div/div[6]/div").click()
        #         except:pass
        #         continue
        
# ---------------------------------inbox---------------------------------




def repo(listop):
    # try:
    with open('datasources/profiles2.txt','r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                index=0
                for row in csv_reader:
                        email=row[2]
                        if index==listop['index']-1:
                            listop['option'].add_argument('--proxy-server='+ row[0] + ':92' )
                            # print('proxy donne '+row[0]+' in '+listop['profil']+'\n' )
                            break
                        index+=1
    f = open("datasources/last_time_report_not_spam.txt", "a")
    f.write('last time at'+str(datetime.datetime.now())+' this boit report not spam '+str(email)+'\n')
    f.close() 
    try:
        drivers = uc.Chrome(use_subprocess=True, options = listop['option'],version_main=108)
        profil=listop['profil']
        print('start task for '+profil)
        spam(drivers,profil)
    except:

        pass
    # except:print('faild open '+listop['profil']+' :/')
# ----------------------------------start my project ----------------------------------
print("----------------------------------Enter the required information----------------------------------")
pr_start = int(input("From which profile do you start?: "))
pr_end = int(input("Which profile to finish?: "))
for i in range(pr_start,pr_end+1):
        prf(i)
print(f"open {len(listop)} profil  donne........")
 
# for start script
for l in listop:
    p=Thread(target=repo,args=(l,))
    p.start()
    sleep(10)