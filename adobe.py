import datetime
from multiprocessing.connection import wait
import os
import webbrowser
import undetected_chromedriver.v2 as uc
from time import sleep
import csv
import os.path
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from threading import Thread
import urllib
import glob
def prf(i):
    print("script run  ........")
    # for add in option in ur browser
    options2 = uc.ChromeOptions()
    # for hide ur browser
    if hd!='N' and hd!="n":
        options2.headless=True
        options2.add_argument('--headless')
    k = i+1
    #  path for ur br
    profile = "profile"+str(i+2)
    path = 'C:\\Users\\admin4\\\AppData\\Roaming\\Google\\adobe\\' + profile
    # condition for creat ur br if not found
    isExist = os.path.exists(path)
    options2.add_argument(
        '--no-first-run --no-service-autorun --password-store=basic')
    if isExist == 0:
        options2.add_experimental_option("prefs", {
            "profile.name": profile
        })
    # for renomu ur br
        options2.add_argument('--user-data-dir='+path)
    
    options2.add_experimental_option("prefs", {"download.default_directory":os.getcwd()+'\image',"directory_upgrade": True})
    listop.append({"option": options2, "from": int(
        parts*i+1), "to": int(parts*k)})
   

def get_latest_image(new_name ):
    pathdon="C:/Users/admin4/Downloads"
    valid_files = [os.path.join(pathdon, filename) for filename in os.listdir(pathdon)]
    valid_files = [f for f in valid_files if '.' in f and \
        f.rsplit('.',1)[-1] in ('jpg','jpeg','png') and os.path.isfile(f)]
    # try:
    if not valid_files:
        raise ValueError("No valid images in %s" % pathdon)
    pathlast= max(valid_files, key=os.path.getmtime)
    split_tup = os.path.splitext(os.path.split(pathlast)[1])
    os.rename(pathlast, "image\\"+new_name+split_tup[1])
    # except:pass
def task(listop):

    drivers = uc.Chrome(use_subprocess=True, options=listop['option'])
    print("script run  ........")
    with open(data) as csv_file:
        line_count = 1
        csv_reader = csv.reader(csv_file, delimiter=';')
        print('you have '+str(langefile))
        for row in csv_reader:
           

            # try:
                url = row[0]
                if line_count >= listop['from']:
                    drivers.get(url)
                    sleep(3)
                    try:WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#details > div > div > div.row-flex-detailspanel > div:nth-child(2) > div > div > div > div > div.margin-bottom-medium > h2 > a'))).click()
                    except:pass
                    try:name=WebDriverWait(drivers, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#details > div > div > div.row-flex-detailspanel > div:nth-child(2) > div > div > div > div > div.margin-bottom-medium > h2 > span'))).text
                    except:
                        name=WebDriverWait(drivers, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#details > div > div > div.row-flex-detailspanel > div:nth-child(2) > div > div > div > div > div.margin-bottom-medium > h2'))).text
                        name=name[:len(name)-9]
                    print(name)
                    WebDriverWait(drivers, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#details > div > div > div.row-flex-detailspanel > div:nth-child(2) > div > div > div > div > div.container-block.padding-top-medium.row > div > div.detail-button-group > button > span')))
                    get_latest_image(name)
                if line_count > listop['to']:
                    drivers.quit()
                    break

                line_count += 1
            # except:
            #     pass
            #     print("errer"+str(line_count))

def supline(ficher, to):
    with open(ficher, 'r') as fr:
        # reading line by line
        lines = fr.readlines()

        # pointer for position
        ptr = 1

        # opening in writing mode

        with open(ficher, 'w') as fw:
            for line in lines:

                # we want to remove 5th line
                if line.strip('\n') != to:
                    fw.write(line)
                ptr += 1

# ---------------------------------------------


path_don=os.getcwd()+'\image'

print(path_don)
while True :
    try:
        pr = int(input("how to want pr creat?: "))
        if pr==0 :
           continue 
    except ValueError:   
        
        print("Please enter a number")
        continue
        
    else:break
        

        
print("do you want to hide this operation?")
hd=input("[N/?]: ")

data = 'data.txt'
langefile = len(open(data, 'r').readlines())
parts = langefile/pr

listop = []


for i in range(pr):
    prf(i)

for l in listop:
    p = Thread(target=task, args=(l,))
    p.start()
quit()

# print("sleep")
# sleep(500000)
