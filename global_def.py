from myimport import *

#os.getcwd() 


# clear cmd

clear = lambda: os.system('cls')


killtheard = []
joinlist=[]
optiontheard_gmail=[]

def show_tab(drivers):
    # drivers.switch_to().Window ( drivers.CurrentWindowHandle )
    #  try:drivers.minimize_window()
    #  except:pass
    #  drivers.maximize_window()
    #  sleep(1)
    try:
        sleep(2)
        drivers.set_window_position(2000, 0)
        if randint(1, 10)%2!=0:
            drivers.minimize_window()
        drivers.maximize_window()
        
    except:
        pass
        try:
            drivers.maximize_window()
        except:pass
        # try:
        #     WebDriverWait(drivers,7).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'body'))).click()
        # except:
        #     pass




def ask_fileName(question):
   
    file_found=False

    
    while(file_found!=True):
        fileName=input("\n "+question+" :  ")
        
        path=os.getcwd()+"\\project\\datasources\\"+fileName
        if(exists(path)):
            return path
        erreurfile=True
        print("this file ",fileName,"not found  \n")




  
def recheckfill(drivers,element,key,by,req):
            input=""
            print("\n reckeck",element)
            
            while(str(input)==""):
                drivers.refresh()
                sleep(0.3)
                WebDriverWait(drivers,10).until(EC.visibility_of_element_located((by,req))).send_keys(key)
                sleep(0.1)
                input=WebDriverWait(drivers,10).until(EC.visibility_of_element_located((by,req))).get_attribute('value')
                
                 
                    
                    
                    
                 
def scrollTo(drivers):
    drivers.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(0.1)
    drivers.execute_script("window.scrollTo(0,0)")
    sleep(0.1)
                  
    
   
 
 
def GetMoroccoTime():
    import pytz
    #pip install pytz
    return datetime.datetime.now(pytz.timezone('Africa/Casablanca'))


def arealyconnected(drivers,profile):
    try:
        drivers.get("https://mail.google.com/mail")
        sleep(1)
        print("check profile "+profile)
        if(str.__contains__(drivers.current_url, 'mail.google.com/mail/u/0/')):   
            return True    

        return False  
    except:
        pass
        print("proxy down for "+profile)
        killtheard.append(drivers)
        drivers.quit() 
 
    
import time
from selenium.webdriver.remote.webelement import WebElement
def slow_type(element: WebElement, text: str, delay: float = 0.1):
    element.clear()

    for character in text:
        element.send_keys(character)
        time.sleep(delay)    