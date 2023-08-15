from global_def import *
from connectage import *
from selenium.webdriver.common.alert import Alert



def load_profiles_c(pr_start,pr_end, file, path):
    try:

        for i in range(pr_start,pr_end+1):
            lign = dopen(file).getline(i)
            proxy = lign.split(",")[0]
            profileName = lign.split(",")[1]
            email = lign.split(",")[2]
            password= lign.split(",")[3]
            recovery= lign.split(",")[4]
            profiles_c(proxy, profileName, path+profileName,email,password,recovery)
    except Exception as e:
        print('Exception:  ' + str(e))

def profiles_c(proxy, profileName, path,email,password,recovery):
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
    options.add_argument("--start-minimize")
    options.add_argument('--proxy-server='+ proxy + ':92' )
    optiontheard_gmail.append({
        "path":path,
        "option": options,
        "profileName": profileName,
        "proxy": proxy,
        "email": email,
        'password':password,
        "recovery":recovery


    })


def google_theard_c():

    for op in optiontheard_gmail:
        p = threading.Thread(target=task2, args=(op,))
        joinlist.append(p)

def start_wait_theard_c(wait_profiles):

    threadparts = wait_profiles  # 3

    i = 1

    for l in joinlist:

        if i <= threadparts:

            
            l.start()
            sleep(15)

        if i == threadparts:
            print("open thread  .....")

            tnext = False
            while (tnext != True):
                sleep(15)
                # print(threadparts, len(killtheard), str(tnext))
                # print('len list kill :',len(killtheard))
                if (len(killtheard) == threadparts):
                    tnext = True

            print("thread finish .....")
            i = 0
            killtheard.clear()

        i += 1

def task2(op):
    
        drivers = uc.Chrome(use_subprocess=True, options=op['option'],version_main=106)
        # drivers.maximize_window()
        checkconnected =  arealyconnected(drivers,op['profileName'])
                                                                                
    
    # try:    
        if (checkconnected==False):
            try:
                drivers.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en")
                # try:drivers.minimize_window()
                # except:pass
                # drivers.maximize_window()
                print("profile ", op["profileName"], " ........")   
                addemails(drivers,op["profileName"],op["proxy"],op["email"],op["password"],op["recovery"])
                print( op["profileName"]+" connected succsucfuly")
            except:
                print(f'this {op["profileName"]} faild open')
                try:
                    drivers.quit()
                    killtheard.append(drivers)
                except:pass
        else:
            print( op["profileName"]+" arealy connected  ")
            addemails(drivers,op["profileName"],op["proxy"],op["email"],op["password"],op["recovery"])
            killtheard.append(op)
    # except:
    #     print("proxy down for " +op["profileName"]+" proxy : "+ op["proxy"])
    #     killtheard.append(op)













def open(op):
    print('wait 30 s')
    sleep(30)
    options = uc.ChromeOptions()
    isExist = os.path.exists(op["path"])
    options.add_argument(
        '--no-first-run --no-service-autorun --password-store=basic')
    # check if profil exist open 
    if isExist != 0:
        print(op["path"])
        options.add_argument('--user-data-dir='+op["path"])
        # options2.add_argument('--proxy-server='+ proxy + ':92' )
        
    

        options.add_argument('--proxy-server='+ op["proxy"] + ':92' )
   
    drivers = uc.Chrome(use_subprocess=True, options=options,version_main=106)
 
    






def gmail_theard():
    for op in optiontheard_gmail:
        p = threading.Thread(target=task2, args=(op))
        joinlist.append(p)









        




