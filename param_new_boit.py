from inspect import trace
from random import randint
import select
from threading import Thread
from time import sleep
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
import os
from linereader import dopen
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
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
    

    
 
    
def task(drivers,profil):
    # try:
    while True:

     try:
        drivers.minimize_window()
        drivers.maximize_window()
        try:
            rec=(WebDriverWait(drivers, 6).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/h1/span'))).text)
            boit=(drivers.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div').text)
            print(rec+' for profil '+profil)
            if rec=="Confirmez qu'il s'agit bien de vous" or rec=="Verify it’s you":
                print("boit "+boit+" not connected : "+profil)
                sleep(10)
                print(profil+" close ")
                drivers.quit()
        except:pass
        drivers.get("https://mail.google.com/mail/u/0/#settings/general")
        WebDriverWait(drivers, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="bx_tnunoo"][value="0"]'))).click()
        # 100 in boit inbox
        Select(drivers.find_element(By.CSS_SELECTOR,'table > tbody > tr:nth-child(4) > td:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(1) >select')).select_by_index(5)
        # Language:	Gmail display language:
        Select(drivers.find_element(By.CSS_SELECTOR,'table > tbody > tr:nth-child(2) > td:nth-child(2)> * > select')).select_by_index(11)
        # conversation
        drivers.find_element(By.CSS_SELECTOR,'input[name="bx_vmb"][value="1"]').click()
        drivers.get("https://mail.google.com/mail/u/0/#settings/inbox")
        # Inbox type: defullt 
        Select(drivers.find_element(By.CSS_SELECTOR,'select[name="inbox-type"]')).select_by_index(0)
        drivers.get("https://mail.google.com/mail/u/0/#settings/fwdandpop")
        # Disable IMAP
        drivers.find_element(By.CSS_SELECTOR,'input[name="bx_ie"][value="0"]').click()
        # chat
        drivers.get("https://mail.google.com/mail/u/0/#settings/chat")
        # Chat:Off 
        drivers.find_element(By.CSS_SELECTOR,'input[name="ix_ct"][value="3"]').click()
        # Meet:Hide the Meet section in the main menu
        drivers.find_element(By.CSS_SELECTOR,'input[name="bx_mlnepd"][value="1"]').click()
        # theme
        drivers.get("https://mail.google.com/mail/u/0/#settings/oldthemes")
        drivers.find_element(By.CSS_SELECTOR,'a[href="https://mail.google.com/mail/?tm=1#settings/themes"]').click()
        # select theme
        WebDriverWait(drivers, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, f'div[role="alertdialog"] > div:nth-child(2) > div:nth-child(2) > div:nth-child({str(randint(1,53))})'))).click()
        # Save & close
        drivers.find_element(By.CSS_SELECTOR,'span[data-tooltip]').click()
        drivers.get("https://mail.google.com/mail/u/0/#settings/general")
        # Save
        drivers.find_element(By.CSS_SELECTOR,'button[guidedhelpid="save_changes_button"]').click()
        drivers.quit()
        print(profil+' finish')
        break
     except:pass    
# ---------------------------------inbox---------------------------------




def repo(listop):
    # try:
    lign = dopen('datasources\\profiles.txt').getline(listop['index'])
    proxy = lign.split(",")[0]
    listop['option'].add_argument('--proxy-server='+ proxy + ':92' )
    profil=listop['profil']
    try:
        drivers = uc.Chrome(use_subprocess=True, options = listop['option'],version_main=106)
        task(drivers,profil)
    except:
        print("faild to open "+profil)
    
    
    
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