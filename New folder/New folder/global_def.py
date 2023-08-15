from myimport import *

#os.getcwd() 


# clear cmd

clear = lambda: os.system('cls')



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


   
 
    
import time
from selenium.webdriver.remote.webelement import WebElement
def slow_type(element: WebElement, text: str, delay: float = 0.1):
    element.clear()

    for character in text:
        element.send_keys(character)
        time.sleep(delay)    