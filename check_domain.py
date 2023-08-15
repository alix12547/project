import csv
import datetime
import random
from threading import Thread
from time import sleep
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# ----------------------------------fonction for my project ----------------------------------
# function for check profil
listop=[]
def prf(i):

    options2 = uc.ChromeOptions()
    profile = "profile"+str(i)
    path = 'C:\\Users\\admin4\\AppData\\Roaming\\checkdomain\\' + profile
    isExist = os.path.exists(path)
    options2.add_argument(
        '--no-first-run --no-service-autorun --password-store=basic')
    # check if profil exist open 
    if isExist == 0:
        options2.add_experimental_option("prefs", {
            "profile.name": profile
        })
    options2.add_argument('--user-data-dir='+path)
    # options2.add_argument('--proxy-server='+ proxy + ':92' )
    
    listop.append({"option":options2,"profil":profile,'index':i})
    

    
 
    
def check_domain(drivers,profil):
    # try:
        
        # go to spam
        drivers.get("https://www.brightcloud.com/tools/url-ip-lookup.php")
        drivers.minimize_window()
        drivers.maximize_window()
        print('open '+str(profil))
        sleep(random.randint(6,8)) 
        inex=0
        with open('datasources/domain.txt','r') as csv_file:

                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                        inex+=1
                        domain=row[0]
                    # try:
                        
                        inp=drivers.find_element(By.CSS_SELECTOR, 'input[id="searchBox"]')
                        inp.clear()
                        inp.send_keys(domain)
                        drivers.find_element(By.CSS_SELECTOR, 'body').click()
                        # sleep(6)
                        WebDriverWait(drivers, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[src^='https://www.google.com/recaptcha/api2/anchor']")))
                        WebDriverWait(drivers, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span#recaptcha-anchor"))).click()
                        drivers.switch_to.default_content()
                        WebDriverWait(drivers, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='recaptcha challenge expires in two minutes']")))
                        sleep(4)
                        drivers.switch_to.default_content()
                        # ActionChains(drivers).move_by_offset(120, 545).click().perform()
                        # WebDriverWait(drivers, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[title="Solve the challenge"]'))).click()
    
                        # WebDriverWait(drivers, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#solver-button"))).click()
                        # sleep(5)
                        WebDriverWait(drivers, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="btn btn-base"]'))).click()
                        

                        

                        sleep(3)
                        statu=drivers.find_element(By.CSS_SELECTOR, 'div[id="threatScore"]').text
                        f = open("datasources/resultatdomain.txt", "a")
                        f.write(str(domain)+':'+str(statu)+'\n')
                        f.close() 
                        print(inex)
                        continue
                    # except:
                    #     drivers.get("https://www.brightcloud.com/tools/url-ip-lookup.php")
                    #     drivers.maximize_window()                             
                    #     continue
        
# ---------------------------------inbox---------------------------------




def repo(listop):
    # try:
    with open('datasources/proxy.txt','r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                index=0
                for row in csv_reader:
                        if index==listop['index']-1:
                            listop['option'].add_argument('--proxy-server='+ row[0] + ':92' )
                            # print('proxy donne '+row[0]+' in '+listop['profil']+'\n' )
                            break
                        index+=1
    drivers = uc.Chrome(use_subprocess=True, options = listop['option'],version_main=106)
    profil=listop['profil']
    check_domain(drivers,profil)
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
    sleep(3)