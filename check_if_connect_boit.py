from threading import Thread
from time import sleep
import undetected_chromedriver.v2 as uc
import os


# ----------------------------------fonction for my project ----------------------------------
# function for check profil
listop=[]
def prf(i):
    options2 = uc.ChromeOptions()
    profile = "profile"+str(i)
    path = 'C:\\Users\\admin4\\\AppData\\Roaming\\Google\\' + profile
    isExist = os.path.exists(path)
    options2.add_argument(
        '--no-first-run --no-service-autorun --password-store=basic')
    options2.headless=True
    options2.add_argument('--headless')
    if isExist != 0:
        options2.add_argument('--user-data-dir='+path)
        listop.append({"option":options2,"profil":profile,'index':i})






def checkprofil(listop):
    drivers = uc.Chrome(use_subprocess=True, options = listop['option'],version_main=106)
    drivers.get("https://mail.google.com/mail/u/0/#spam")
    if drivers.current_url!="https://mail.google.com/mail/u/0/#spam":
        print(listop["profil"]+" not connected")
    drivers.quit()

print("----------------------------------Enter the required information----------------------------------")
pr_start = int(input("From which profile do you start?: "))
pr_end = int(input("Which profile to finish?: "))

for i in range(pr_start,pr_end+1):
        prf(i)
print(f"open {len(listop)} profil")
 
# for start script
for l in listop:
    p=Thread(target=checkprofil,args=(l,))
    p.start()
    sleep(1)