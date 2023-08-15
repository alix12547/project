import os
import undetected_chromedriver.v2 as uc
import csv
import os.path
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from threading import Thread
def prf(i):
    print("script run  ........")
    # for add in option in ur browser
    options2 = uc.ChromeOptions()
    k=1+i
    profile = "profile"+str(i+2)
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
        listop.append({"option": options2, "from": int(
        parts*i+1), "to": int(parts*k)})
   

def get_latest_image(new_name ):
    while True:
       
       try: 
        pathdon="C:\\Users\\admin4\\Downloads"
        pathdon_count=len([entry for entry in os.listdir(pathdon) if os.path.isfile(os.path.join(pathdon, entry))])-1
        if numberinfolder+1==pathdon_count:
            i=1
            valid_files = [os.path.join(pathdon, filename) for filename in os.listdir(pathdon)]
            valid_files = [f for f in valid_files if '.' in f and \
                f.rsplit('.',1)[-1] in ('jpg','jpeg','png','ai','psd') and os.path.isfile(f)]
            # try:
            if not valid_files:
                raise ValueError("No valid images in %s" % pathdon)
            pathlast= max(valid_files, key=os.path.getmtime)
            split_tup = os.path.splitext(os.path.split(pathlast)[1])
            try:os.rename(pathlast, "image\\"+new_name+split_tup[1])
            except:pass;os.rename(pathlast, "image\\"+new_name+str(i)+split_tup[1])
            i+=1
            break
            
       except:pass
        
       
def task(listop):
    listop['option'].add_experimental_option("prefs", {"download.default_directory":os.getcwd()+'\image',"directory_upgrade": True})

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
                    WebDriverWait(drivers, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div'))).click()
                    name=WebDriverWait(drivers, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div/div[3]/h1'))).text  
                    WebDriverWait(drivers, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div'))).click()
                    WebDriverWait(drivers, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="download-file"]'))).click()
                    WebDriverWait(drivers, 6).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div'))).click()
                    print(name)                                                                 
                    WebDriverWait(drivers, 3).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/div/aside/div[2]/div[1]/div[2]/div/div/div[4]/div'))).click()
                    get_latest_image(name)
                if line_count > listop['to']:
                    drivers.quit()
                    break

                line_count += 1
            # except:pass
            
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
        

        
# print("do you want to hide this operation?")
# hd=input("[N/?]: ")
print('')
print ('########################################################')
print ('####             Download image freepic             ####')
print ('####         Coded by weon Thanks for Abdes         ####')
print ('####                                                ####')
print ('####                 --------------                 ####')
print ('########################################################')
print ('')
hd="n"
numberinfolder=len([entry for entry in os.listdir("C:\\Users\\admin4\\Downloads") if os.path.isfile(os.path.join("C:\\Users\\admin4\\Downloads", entry))])-1
print('numberinfolder '+str(numberinfolder))
data = 'datafreepic.txt'
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
