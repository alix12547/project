from myimport import *







  
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
                  
    
      

def addemail(drivers,profile,email,proxy): 
   
        try:
            print("\nckeck email")
            WebDriverWait(drivers,10).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='identifierId']"))).send_keys(email)
            sleep(0.1)
            scrollTo(drivers)
            if(str(WebDriverWait(drivers,7).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='identifierId']"))).get_attribute('value'))==""):
                 
                recheckfill(drivers,str(email),email,By.XPATH,"//input[@id='identifierId']")
        
        except:
            print("<error!> proxy ",proxy," for",profile," is not working")
            adderreurlog(str("proxy is not working"),profile,email,proxy)
            pass
            
        
        #button next
        try:
            sleep(randint(1,2)) 
            WebDriverWait(drivers,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='identifierNext']/div/button/span"))).click()
        except:
            pass
            
            
        
        #extract erreur text
        try:   
          erreur_notfound=WebDriverWait(drivers,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[2]/div[2]/div'))).text
          adderreurlog(str("Email is not found"),profile,email,proxy)
          print("<error!> ","Email is not found")
        except:
            
            
            pass
        
   
        
   
         
def addepassword(drivers,profile,password,email,proxy): 
    
    print("check password")
    try:
    
        WebDriverWait(drivers,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='password']/div[1]/div/div[1]/input"))).send_keys(password)
        sleep(0.1)
        scrollTo(drivers)
        if(str(WebDriverWait(drivers,7).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='password']/div[1]/div/div[1]/input"))).get_attribute('value'))==""):
            recheckfill(drivers,"password",password,By.XPATH,"//*[@id='password']/div[1]/div/div[1]/input")
        
        #button next
        WebDriverWait(drivers,7).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='passwordNext']/div/button/span"))).click()
        
    except:
        pass    
    
    
    try:
        erreur_password=WebDriverWait(drivers,7).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#yDmH0d > c-wiz > div > div.eKnrVb > div > div.j663ec > div > form > span > div.SdBahf.Fjk18.Jj6Lae > div.OyEIQ.uSvLId > div:nth-child(2) > span'))).text
        adderreurlog(str(erreur_password),profile,email,proxy)
        print("<error!> "+erreur_password)
    except:
        pass
        
    

def checkpage(drivers,profile,email,proxy):
    if(str.__contains__(drivers.current_url,'iap')):
        print("<error!> "+"verification number v1")
        adderreurlog(str("verification number v1"),profile,email,proxy)
        
    if(str.__contains__(drivers.current_url,'idvreenable')):
        print("<error!> "+"verification number")
        adderreurlog(str("verification number"),profile,email,proxy)      





def adderecovry(drivers,profile,email,proxy,recovery): 
     
    try:   
        print("check recovry")
        WebDriverWait(drivers,7).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[3]"))).click()
        WebDriverWait(drivers,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='knowledge-preregistered-email-response']"))).send_keys(recovery)
        sleep(0.1)
        scrollTo(drivers)
        if(str(WebDriverWait(drivers,7).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='knowledge-preregistered-email-response']"))).get_attribute('value'))==""):
            recheckfill(drivers,"recovry",recovery,By.XPATH,"//*[@id='knowledge-preregistered-email-response']")
        
        
 
        WebDriverWait(drivers,7).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span'))).click()
        
    except:
        pass                               
    
    try:
        checkpage(drivers,profile,email,proxy)
    except:
        pass 
    
    try:
        erreur_recovry =WebDriverWait(drivers,7).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div.akwVEf > div.d2CFce.cDSmF > div > div.LXRPh > div.dEOOab.RxsGPe > div'))).text
        
        adderreurlog(str(erreur_recovry),profile,email,proxy)
        print("<error!> ",erreur_recovry)
           
           
    except:
        pass
        
        
        
def adderreurlog(error,profile,email,proxy):
    d = GetMoroccoTime()

    errorsyntax=  "!profile: "+profile+" <error>: "+error +"\t "+"proxy:"+proxy+ " boite: " + email+"  Date: "+str(d)+" \n"
    f = open("errorlog.txt", "a")
    f.write(errorsyntax)
    f.close()  
       
def addeconnected(profile,email,proxy):
    d = GetMoroccoTime()

    errorsyntax=">> profile:" + profile +" connected successfully"+" ... "+" boite: " + email +" proxy: "+proxy+  "\t Date: " + str(d)+" \n"
    f = open("connectedlog.txt", "a")
    f.write(errorsyntax)
    f.close()

def arealyconnected(drivers):
    print("check profile")
    if(str.__contains__(drivers.current_url, 'mail.google.com/mail/u/0/')):   
        return True    

    return False
 
 



def deletspam(drivers,email):
    print("delet spam")
    try:
        drivers.get("https://mail.google.com/mail/u/0/#spam")
        sleep(randint(2,4))
        #button Delete all spam messages now
        drivers.find_element(By.XPATH,'(//div[contains(@class,"BltHke nH oy8Mbf")]//Span[contains(@class,"x2")])[1]').click()
        sleep(randint(2,4))
        #button ok 
        drivers.find_element(By.XPATH,'(//button[contains(@name,"ok") and contains(@class,"J-at1-auR J-at1-atl")])[1]').click()
        sleep(randint(2,4))
        #test open spam 
        drivers.find_element(By.XPATH,'(//div[@class="ae4 UI nH oy8Mbf"]//span[@class="bog"])[1]').click()
    except:
        print("spam for ",email," is clean")
        pass
    
         
def notspam(drivers,email):
    print("open not spam",email) 
    drivers.get("https://mail.google.com/mail/u/0/#spam") 
      
    
    while(True):
        
            sleep(randint(1,2)) 
            try:   
             WebDriverWait(drivers,7).until(EC.element_to_be_clickable((By.XPATH,'(//span[@class="bog"])[1]'))).click()
             print("btn open ",email)
            except:
                pass
            #button not spam
             
            sleep(randint(3,4)) 
            
            btn=randint(1,2)
            
            try:
                if(btn==1):
                    WebDriverWait(drivers,7).until(EC.element_to_be_clickable((By.XPATH,"(//div[@class='Bn'])[2]"))).click()
                    print("btn1 ",email)
                else:
                    WebDriverWait(drivers,7).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='bzq bzr IdsTHf']"))).click()
                    print("btn2 ",email)
            
                #button not spam
                 
                #for delete icon drivers.find_element(By.XPATH,'(//div[@class="Bn"])[1]').click()
            except:
                pass 
                
           
 
            #open tab spam tryclick("check pop spam",'body > div.Kj-JD > div.Kj-JD-Jl > button:nth-child(2)',By.CSS_SELECTOR,drivers)
            
            
             
             

     


def delet_trach(drivers,email):
    print("delet trach")
    
    drivers.get("https://mail.google.com/mail/u/0/#trash") 
    sleep(randint(2,4)) 
    try:
        #button Delete all spam messages now
        drivers.find_element(By.XPATH,'(//div[contains(@class,"BltHke nH oy8Mbf")]//Span[contains(@class,"x2")])[1]').click()
        sleep(randint(2,4))
        #button ok 
        drivers.find_element(By.XPATH,'(//button[contains(@name,"ok") and contains(@class,"J-at1-auR J-at1-atl")])[1]').click()
        sleep(randint(2,4))
        #test open spam 
        drivers.find_element(By.XPATH,'(//div[@class="ae4 UI nH oy8Mbf"]//span[@class="bog"])[1]').click()
    except:
        print("delete trach for ",email," is finish")
        pass
 
 
def GetMoroccoTime():
    import pytz
    #pip install pytz
    return datetime.datetime.now(pytz.timezone('Africa/Casablanca'))


   
 
    
import time
from selenium.webdriver.remote.webelement import WebElement

def slow_type(element: WebElement, text: str, delay: float = 0.1):

    for character in text:
        element.send_keys(character)
        time.sleep(delay)    