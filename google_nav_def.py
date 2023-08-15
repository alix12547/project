from tkinter import E
from global_def import *
from myimport import *

optiontheard = []
killtheard = []
#lenfile=len(open('google_searsh.txt', 'r').readlines())
data = 'datasources\\data.txt'


def load_profiles(pr_start,pr_end, file, path):
    try:

        for i in range(pr_start,pr_end+1):
            lign = dopen(file).getline(i)
            proxy = lign.split(",")[0]
            profileName = lign.split(",")[1]
            email=lign.split(",")[2]
            profiles(proxy, profileName, path+profileName,email)
    except Exception as e:
        print('Exception:  ' + str(e))


def profiles(proxy, profileName, path,email):
    print("profile ", profileName, " ........")
    options = uc.ChromeOptions()

    isExist = os.path.exists(path + profileName)
    options.add_argument(
        '--no-first-run --no-service-autorun --password-store=basic')
    if isExist == 0:
        options.add_experimental_option("prefs", {
            "profile.name": profileName
        })
    options.add_argument('--user-data-dir='+path)
    # options.headless=True
    # options.add_argument('--headless')
    options.add_argument('--proxy-server='+ proxy + ':92' )
    optiontheard.append({


        "profileName": profileName,
        "option": options,
        'email':email,


    })


def task(op, keywordfile, nb_message):
    
    drivers = uc.Chrome(use_subprocess=True, options=op['option'],version_main=106)
    drivers.minimize_window()
    drivers.maximize_window()
    sleep(randint(3, 4))
    #checkconnected =  arealyconnected(drivers)
    # if (checkconnected!=True):
    r = 0
    drivers.get("https://google.com")
    while (r < 3):
        if not (str.__contains__(drivers.current_url, 'google.com')):
            drivers.get("https://google.com")

        sleep(randint(1, 2))

        question = dopen(keywordfile).getline(
            randint(1, int(len(open(keywordfile, 'r').readlines()))))
        el = WebDriverWait(drivers, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='q']")))
        #text = "how many cups in a pint"
        text = question
        slow_type(el, text)
        if (str(WebDriverWait(drivers, 7).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='q']"))).get_attribute('value')) == ""):
            recheckfill(drivers, str(text), text,
                        By.XPATH, "//input[@name='q']")

        try:
            drivers.find_element(
                By.XPATH, "//div[@class='o3j99 LLD4me yr19Zb LS8OJ']").click()

        except:
            pass

        try:
            drivers.find_element(
                By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").click()

        except:
            pass

        sleep(randint(1, 2))

        # drivers.find_element(By.XPATH,'//*[@id="rso"]//h3').click()
        try:
            drivers.find_element(
                By.CSS_SELECTOR, "#rso >* > div > div > div.Z26q7c.UK95Uc.jGGQ5e > div > a > h3").click()

        except:
            print("  ", str(op['profileName']), " erreur 1 ")

            try:
                # drivers.find_element(By.CSS_SELECTOR,"#rso > div:nth-child(2) > div > div > div.Z26q7c.UK95Uc.jGGQ5e > div > a > h3").click()
                sleep(0.5)
                drivers.find_element(
                    By.XPATH, '//*[@id="rso"]/div[2]/div[2]/div/div/div/div[1]/div/a').click()

            except:
                print("  ", str(op['profileName']), " erreur 2 ")

                try:
                    # drivers.find_element(By.CSS_SELECTOR,"#rso > div:nth-child(2) > div > div > div.Z26q7c.UK95Uc.jGGQ5e > div > a > h3").click()
                    sleep(0.5)
                    drivers.find_element(
                        By.XPATH, '//*[@class="LC20lb MBeuO DKV0Md"]/div[2]/div/div/div/div/div[1]/div/div[1]/div/a/h3').click()

                except:
                    print("  ", str(op['profileName']), " erreur 3 ")
                pass

                pass

            pass

        sleep(2)

        total_height = int(drivers.execute_script(
            "return document.body.scrollHeight"))

        for i in range(1, int(total_height/randint(2, 6)), 20):
            drivers.execute_script("window.scrollTo(0, {});".format(i))

        sleep(randint(10, 15))

        drivers.back()

        sleep(randint(5, 10))

        # drivers.execute_script("window.open('https://www.google.com')")
        r += 1
        drivers.execute_script("window.scrollTo(0,0)")

    print("profile : ", str(op['profileName']), " terminate")

    sendemail(drivers, op, nb_message)
    # drivers.close()
    # killtheard.append(op)


joinlist = []


def google_theard(keywordfile, nb_message):

    for op in optiontheard:
        p = threading.Thread(target=task, args=(op, keywordfile, nb_message))
        joinlist.append(p)


def start_wait_theard(wait_profiles):

    threadparts = wait_profiles  # 3

    i = 1

    for l in joinlist:

        if i <= threadparts:

            
            l.start()
            sleep(0.5)
        if i == threadparts:
            print("open thread  .....")

            tnext = False
            while (tnext != True):
                sleep(15)
                # print(threadparts, len(killtheard), str(tnext))

                if (len(killtheard) == threadparts):
                    tnext = True

            print("thread finish .....")
            i = 0
            killtheard.clear()

        i += 1
# stock donne in array
def donnemail():
    boit = [];subject = [];messages = []
    with open(data, encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
               if row[0]!='': boit.append(row[0])
               if row[1]!='':subject.append(row[1])
               if row[2]!='':messages.append(row[2])
    return (boit,subject,messages)
boit,subject,messages=donnemail()


def sendemail(drivers, op, nb_message):
    
    drivers.get("https://mail.google.com/mail/u/0/#inbox")
    try:
            boit=(drivers.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div').text)
            print("boit "+boit+"not connected : "+op['profileName'])
            sleep(10)
            print(op['profileName']+" close ")
            drivers.quit()
    except:pass
    # strat taske
    for i in range(1, nb_message+1):
        while True:
            bt=boit[randint(0,len(boit)-1)]
            if bt==op['email']:continue
            else:break
        # bt =dopen(data).getline(randint(1, int(len(open(data, 'r').readlines().readrows().split(";")[0])))).split(";")[0]
        try:
            if i <= nb_message:
                # ------------------------send email-----------------------
                print(f'Message {str(i)} for : '+str(op['profileName']))
                #click in compose
                sleep(randint(4, 6))
                drivers.find_element(
                    By.XPATH, "//div[@class='T-I T-I-KE L3']").click()
                if (str.__contains__(drivers.current_url, 'compose=new')):
                    sleep(randint(4, 6))
                    # add TO
                    slow_type(drivers.find_elements(
                        By.XPATH, '//input[@type="text"]')[3], bt.lower())
                    sleep(randint(3, 5))
                    # add subject
                    slow_type(drivers.find_elements(By.TAG_NAME, 'input')[
                              11], subject[randint(0, len(subject)-1)])
                    sleep(randint(3, 5))
                    # add messages
                    slow_type(drivers.find_element(
                        By.XPATH, '//div[contains(@class, "Am Al editable LW-avf tS-tW")]'), messages[randint(0, len(messages)-1)])
                    sleep(randint(3, 5))
                    # click send
                    drivers.find_element(
                        By.XPATH, '/html/body/div[*]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]').click()
                    sleep(randint(3, 5))
                    # save historique
                    f = open("datasources\\historique.txt", "a")
                    f.write(op['email']+' send email from :'+str(bt) +
                            ' at time : '+str(GetMoroccoTime())+'\n')
                    f.close()
                    # send  Message
                    print(f"send    {str(i)} for : "+str(op['profileName']))
                    sleep(randint(3, 5))
            if i == nb_message:
                print(op['email']+" finish ........")
                drivers.quit()
                killtheard.append(op)
                break
            i += 1
        except:
            pass
            print("errer"+str(i)+' in :'+str(op['profileName']))
