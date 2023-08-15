import csv
import datetime
import random
from threading import Thread
from time import sleep
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
import os
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import imaplib
import email
from email.header import decode_header

# ----------------------------------fonction for my project ----------------------------------
def script():
    

    # account credentials
    # username ='firstscriptemh@gmail.com'
    # password = 'wxphtlrmcgpvvnew'
    username ='sponsourformal@gmail.com'
    password = 'fxdqjkrcvqcihzwv'
    # username ='jacobmayle24@gmail.com'
    # password = 'lxnxbswrfpzgvbce'
    
    # username ='chaymaejarodi@gmail.com'
    # password = 'ltywhykdsbubwixp'

    # create an IMAP4 class with SSL 
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    # authenticate
    imap.login(username, password)
    # select the mailbox I want to delete in
    # if you want SPAM, use imap.select("SPAM") instead
    imap.select('"[Gmail]/All Mail"')
    # search for specific mails by sender
    # status, messages = imap.search(None, 'FROM "googlealerts-noreply@google.com"')
    # # to get mails by subject
    # status, messages = imap.search(None, 'SUBJECT "Thanks for Subscribing to our Newsletter !"')
    # to get all mails
    status, messages = imap.search(None, "ALL")

    # convert messages to a list of email IDs
    messages = messages[0].split(b' ')
    # while True:
    #  try:
    print(len(messages))
    for mail in messages:
    #  while True:
    #   try:
        _, msg = imap.fetch(mail, "(RFC822)")
        # you can delete the for loop for performance if you have a long list of emails
        # because it is only for printing the SUBJECT of target email to delete
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                subject = decode_header(msg["Subject"])[0][0]
                From = decode_header(msg["From"])[0][0]
                Received=msg['Received-SPF']
                # print(msg["body"])
                if isinstance(subject, bytes):
                    # if it's a bytes type, decode to str
                    subject = subject.decode()
                if isinstance(From, bytes):
                    # if it's a bytes type, decode to str
                    From=From.decode()
                    
                if subject=='Verification !-':
                    # print('Received-SPF:' + Received.split(' ')[0])
                    print('Received-SPF:' + Received.split(' ')[0]+' IP:'+''.join(re.findall( '[0-9]+(?:\.[0-9]+){3}', Received.split('client-ip=')[0] )))
                    # print("Deleting", subject,'From :',From)
                    for i in range(2):
                        imap.store(mail, '+X-GM-LABELS', '\\Trash')
                        imap.select('[Gmail]/Trash')
                        imap.store(mail, '+FLAGS', '\\Deleted') # FLag aLL Trash as Deleted
                        imap.expunge()
                    imap.select('"[Gmail]/All Mail"')
import winshell
winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)



                    # imap.select('"[Gmail]/All Mail"')
                            # newUidList = processEmails(messages)
                # for uid in newUidList:
                #     mail.uid('STORE',uid, '+FLAGS', '(\\Deleted)')
        # SECTION 3: Once all the required emails have been sent to Trash,
        # permanently delete emails marked as deleted from the selected folder
        # print("Emptying Trash and expunge...")
        # imap.select('[Gmail]/Trash')
        # imap.store("1:*", '+FLAGS', '\\Deleted') # FLag aLL Trash as Deleted
        # imap.expunge()

        # imap.select('[Gmail]/Trash')  # select all trash
        # imap.store("1:*", '+FLAGS', '\\Deleted')
    # imap.select('"[Gmail]/All Mail"')
                # print('Received-SPF:' + msg['Received-SPF'].split(' ')[0])
                # print("Deleting", subject,'From :',From)

        # mark the mail as deleted
        # imap.store(mail, "+FLAGS", "\\Deleted")
    #   except:
    #     sleep(1)
    #     print("0 email")
    #     continue
    # m = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    # m.login(username,password)
    # m.select('INBOX')
    # print('start')
    # result, data = m.uid('search', None, "ALL") # search all email and return uids
    # if result == 'OK':
    #     for num in data[0].split():
    #         result, data = m.uid('fetch', num, '(RFC822)')
    #         if result == 'OK':
    #             email_message = email.message_from_bytes(data[0][1])    # raw email text including headers
    #             print('From:' + email_message['From'])
    #             print('Received-SPF:' + email_message['Received-SPF'].split(' ')[0])
    #             m.store(email_message, "+FLAGS", "\\Deleted")
    # m.close()
    # m.logout()
def extrat_ip(drivers):
    while True:
        
        # try: 
            count=0  
            drivers.get('https://mail.google.com/mail/u/0/#inbox') 
            try:
                try:   ip= drivers.find_element(By.XPATH, "/html/body/div[*]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[5]/div[1]/div/table/tbody/tr[1]/td[6]/div/div/span").text
                except:ip= drivers.find_element(By.XPATH, "/html/body/div[*]/div[3]/div/div[2]/div[*]/div/div/div/div/div[2]/div/div[1]/div/div[*]/div[*]/div[1]/div/table/tbody/tr[1]/td[6]/div").text
                ip=''.join(re.findall( '[0-9]+(?:\.[0-9]+){3}', ip ))
                
                if ip!='':
                    count+=1
                    print(str(count)+' ip inbox')
                    print(ip)
                    # save historique
                    f = open("datasources/ip_inbox.txt", "a")
                    f.write(ip+'\n')
                    f.close()                     
                    # select email                         
                    try:   drivers.find_element(By.XPATH, "/html/body/div[*]/div[3]/div/div[2]/div[*]/div/div/div/div/div[2]/div/div[1]/div/div/div[5]/div[1]/div/table/tbody/tr[1]/td[2]/div").click()
                    except:drivers.find_element(By.XPATH, "/html/body/div[*]/div[3]/div/div[2]/div[*]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[4]/div[1]/div/table/tbody/tr[1]/td[2]/div").click()
                    # delete email
                    try:   drivers.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/div/div/div[2]/div[3]").click()
                    except:drivers.find_element(By.XPATH, "/html/body/div[*]/div[3]/div/div[2]/div[*]/div/div/div/div/div[1]/div[2]/div[*]/div[1]/div/div/div[2]/div[3]/div").click()
                    # go to trush
                    drivers.get("https://mail.google.com/mail/u/0/#trash")
                    # select email                  /html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[4]/div[1]/div/table/tbody/tr[1]/td[2]
                    sleep(0.6)
                    drivers.find_element(By.XPATH, "/html/body/div[*]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[4]/div[1]/div/table/tbody/tr[1]/td[2]").click()
                    # except:drivers.find_element(By.XPATH, "/html/body/div[*]/div[3]/div/div[2]/div[*]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[8]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/div").click()
                    # delete email in trush                
                    drivers.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[2]").click()
            except:pass
            # go to spam
            drivers.get("https://mail.google.com/mail/u/0/#spam")
            sleep(0.6)
            try:
                ips= drivers.find_element(By.XPATH, "/html/body/div[*]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[4]/div[1]/div/table/tbody/tr[1]/td[6]/div").text
                # except:ips= drivers.find_element(By.XPATH, "/html/body/div[*]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[*]/div[1]/div/table/tbody/tr[1]/td[6]/div/div/div/span/span").text
                ips=''.join(re.findall( '[0-9]+(?:\.[0-9]+){3}', ips ))
                if ips!='':
                    # select mail spam
                    try:   drivers.find_element(By.XPATH, "/html/body/div[*]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[4]/div[1]/div/table/tbody/tr[1]/td[2]").click()
                    except:drivers.find_element(By.XPATH, "/html/body/div[*]/div[3]/div/div[2]/div[*]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[8]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/div").click()
                    # delete email forever                 
                    try:   drivers.find_element(By.CSS_SELECTOR, 'div[class="Bn"]').click()
                    except:drivers.find_element(By.XPATH, "/html/body/div[*]/div[3]/div/div[2]/div[*]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div").click()
            except:pass
            # # go to trsh
            # drivers.get("https://mail.google.com/mail/u/0/#trash")
            # sleep(0.6)
            # try:
            #     ips= drivers.find_element(By.XPATH, "/html/body/div[*]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[4]/div[1]/div/table/tbody/tr[1]/td[6]/div").text
            #     # except:ips= drivers.find_element(By.XPATH, "/html/body/div[*]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[*]/div[1]/div/table/tbody/tr[1]/td[6]/div/div/div/span/span").text
            #     ips=''.join(re.findall( '[0-9]+(?:\.[0-9]+){3}', ips ))
            #     if ips!='':
            #         # select mail spam
            #         try:   drivers.find_element(By.XPATH, "/html/body/div[*]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[4]/div[1]/div/table/tbody/tr[1]/td[2]").click()
            #         except:drivers.find_element(By.XPATH, "/html/body/div[*]/div[3]/div/div[2]/div[*]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[8]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/div").click()
            #         # delete email forever                 
            #         try:   drivers.find_element(By.XPATH, "/html/body/div[*]/div[3]/div/div[2]/div[2]/div/div/div/div/div[1]/div[*]/div[2]/div[1]/div/div/div[2]").click()
            #         except:drivers.find_element(By.XPATH, "/html/body/div[*]/div[3]/div/div[2]/div[*]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div").click()
            # except:pass
            continue
            sleep(10)
        # except:continue

def deletemail(drivers):
                    
     while True:
        
        # try: 
        
            drivers.get('https://mail.google.com/mail/u/0/#inbox') 
            sleep(0.5)
            try:
                    # refresh
                    WebDriverWait(drivers,2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[gh="mtb"]>div>div>div:nth-child(5)>div>div'))).click()
                    # select email                         
                    WebDriverWait(drivers,1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'table[role="grid"] > tbody > tr > td:nth-child(2)'))).click()
                    # delete email
                    WebDriverWait(drivers,1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[act="10"]'))).click()
                    print("inbox")
                    # go to trush
                    try:
                        drivers.get("https://mail.google.com/mail/u/0/#trash")
                        # select email                  /html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[4]/div[1]/div/table/tbody/tr[1]/td[2]
                    
                        WebDriverWait(drivers,2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[gh="mtb"] >div>div >div >div>div >span'))).click()
                        # delete email in trush                
                        WebDriverWait(drivers,2).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div[gh="mtb"]>div>div>div:nth-child(2)>div>div[class="Bn"]'))).click()                   
                    except:
                        pass
            except:
                pass
                # go to spam
                drivers.get("https://mail.google.com/mail/u/0/#spam")
                try:
                    # refresh
                    WebDriverWait(drivers,2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[gh="mtb"]>div>div>div:nth-child(6)>div>div'))).click()
                    # select mail spam
                    WebDriverWait(drivers,2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'table[role="grid"] > tbody > tr > td:nth-child(2)'))).click()
                    # delete email forever 
                    WebDriverWait(drivers,2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[gh="mtb"]>div>div>div:nth-child(2)>div>div[class="Bn"]'))).click()
                    print("spam")
                    continue
                except:pass
            continue
   
def main(pr_start):
    if pr_start==1 or pr_start==2:
        options2 = uc.ChromeOptions()
        profile = "profile"+str(pr_start)
        # +str(i)
        path = 'C:/Users/'+os.getlogin()+'/AppData/Roaming/Google/tools_gmail' + profile
        isExist = os.path.exists(path)
        options2.add_argument(
            '--no-first-run --no-service-autorun --password-store=basic')
        # check if profil exist open 
        if isExist == 0:
            options2.add_experimental_option("prefs", {
                "profile.name": profile
            })
        options2.add_argument('--user-data-dir='+path)
        drivers = uc.Chrome(use_subprocess=True, options = options2,version_main=106)
        drivers.maximize_window()
        if pr_start==1: deletemail(drivers)
        else: extrat_ip(drivers)
    elif pr_start==3:
        script()

while True:
    try:
        os.system("cls")
        print("choice 1 or 2 :\n1-send\n2-test ip\n3-script")
        pr_start = int(input("what do you need?: "))
        if pr_start>3 or pr_start<1:continue
        else:
            
            break
            
    except:
        os.system("cls")
        print('donne incorect')
        sleep(0.5)
        continue
# prf(pr_start)
main(pr_start)