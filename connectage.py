from myimport import *
from global_def import *
from connectage_def import *







   
def addemails(drivers,profile,proxy,email,password,recovery): 
 while True:
    try:
        show_tab(drivers)
        try:
            # try:
            #     No_internet=WebDriverWait(drivers,3).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div[id="main-message"]>h1>span'))).text
            #     if No_internet=='This site can’t be reached':
                    
            #         print("proxy ",proxy," for",profile," is not working")
            #         killtheard.append(drivers)
            #         drivers.quit()
            #         break
            # except:
                No_internet=WebDriverWait(drivers,3).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'a[href="#buttons"]'))).text
                print(No_internet)
                if No_internet=='Checking the proxy and the firewall':
                    
                    print("proxy ",proxy," for",profile," is not working")
                    killtheard.append(drivers)
                    drivers.quit()
                    break
                
        except:pass
        try:
            if(str.__contains__(drivers.current_url,'gds.google.com')):              
                print("this account deblocked succese "+profile)
                show_tab(drivers)
                try:WebDriverWait(drivers,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'button'))).click()
                except:pass
            if(str.__contains__(drivers.current_url,'#inbox')): 
                drivers.get('https://myaccount.google.com/alert/nt/1668696496000?rfn%3D5%26rfnc%3D4%26eid%3D-7834588343699571215%26et%26origin%3D2')
            if(str.__contains__(drivers.current_url,'notifications?rfn')): 
                try:
                    WebDriverWait(drivers,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'c-wiz>div>div:nth-child(2)>div>div>ul>li>a'))).click()
                
                    sleep(3)
                    show_tab(drivers)
                    try:WebDriverWait(drivers,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'a[aria-label="Check activity"]'))).click()
                    except:pass
                    show_tab(drivers)
                        # drivers.switch_to.window(drivers.window_handles[1])
                    if(str.__contains__(drivers.current_url,'notifications/eid')): 
                        show_tab(drivers)
                        WebDriverWait(drivers,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div[aria-live="polite"]>div:nth-child(8)>button:nth-child(2)'))).click()
                        sleep(4)
                        show_tab(drivers)
                        WebDriverWait(drivers,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div[aria-live="polite"]>div>div:nth-child(5)>button>span:nth-child(4)'))).click()
                    if(str.__contains__(drivers.current_url,'security-checkup')): 
                        print("this account active "+profile)
                        killtheard.append(drivers)
                        drivers.quit() 
                        break
                    if(str.__contains__(drivers.current_url,'#inbox')): 
                        show_tab(drivers)
                        print("this account active "+profile)
                        killtheard.append(drivers)
                        drivers.quit() 
                        break
                
                except:
                    pass
                    if(str.__contains__(drivers.current_url,'notifications?rfn')) or (str.__contains__(drivers.current_url,'notifications/eid')) or (str.__contains__(drivers.current_url,'security-checkup')): 
                        print("this account active "+profile)
                        killtheard.append(drivers)
                        drivers.quit() 
                        break
            if(str.__contains__(drivers.current_url, 'challenge/pwd?')):
                    sleep(2)
                    addepassword(drivers,profile,password,email,proxy,recovery)  
                    break              
        except:pass
        try:
            drivers.refresh()
            print("\nckeck email "+profile)
            if(str.__contains__(drivers.current_url, 'challenge/pwd?')):
                sleep(2)
                addepassword(drivers,profile,password,email,proxy,recovery)
            # sleep(randint(1,2))
            print("la ma5soch pass")
            show_tab(drivers)
            # sleep(randint(1,2))
            WebDriverWait(drivers,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[id='identifierId']"))).send_keys(email)
            sleep(0.1)
            scrollTo(drivers)
            if(str(WebDriverWait(drivers,7).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[id='identifierId']"))).get_attribute('value'))==""):
                 
                recheckfill(drivers,str(email),email,By.CSS_SELECTOR,"input[id='identifierId']")
        
        except:pass
        try:
            if(str.__contains__(drivers.current_url, 'challenge/pwd?')):
                sleep(2)
                addepassword(drivers,profile,password,email,proxy,recovery)
        
            if(str.__contains__(drivers.current_url,'security-checkup')): 
                print(" for",profile," donne ")
                killtheard.append(drivers)
                drivers.quit()
                break
            # else:
            #     print("<error!> proxy ",proxy," for",profile," is not working")
            #     adderreurlog(str("proxy is not working"),profile,email,proxy)
            #     killtheard.append(drivers)
            #     drivers.quit()
        except:pass     
            
        
        #check not foud erreur
        try:
            sleep(randint(1,2)) 
            show_tab(drivers)
            WebDriverWait(drivers,3).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='identifierNext']/div/button/span"))).click()
            sleep(2)
            if(str.__contains__(drivers.current_url, 'challenge/pwd?')):
                addepassword(drivers,profile,password,email,proxy,recovery)
        
            # sleep(randint(1,2))
            try: 
                sleep(randint(1,2))   
                WebDriverWait(drivers,3).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[2]/div[2]/div'))).text
                adderreurlog(str("Email is not found"),profile,email,proxy)
                print("<error!> ",email, " is not found")
                killtheard.append(drivers)
                drivers.quit()
                break
            except:
              pass
            #button next
            
            try:
                WebDriverWait(drivers,2).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'img[id="captchaimg"][src]')))
                print("<error!> ",email, " need capatcha in email")
                # sleep(80)
                killtheard.append(drivers)
                drivers.quit()
            except:pass    
            sleep(2)
            addepassword(drivers,profile,password,email,proxy,recovery)
            
        except:
            pass
    except:
        continue    
              
def addepassword(drivers,profile,password,email,proxy,recovery): 
        sleep(1)
        show_tab(drivers)
        if(str.__contains__(drivers.current_url, 'signin/identifier?')):
            drivers.refresh()
            sleep(1)
            drivers.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en")
            addemails(drivers,profile,proxy,email,password,recovery)
        try:
                WebDriverWait(drivers,2).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'img[id="captchaimg"][src]')))
                print("<error!> ",email, " need capatcha in password")
                # sleep(400)
                killtheard.append(drivers)
                drivers.quit()
        except:pass    
        if(str.__contains__(drivers.current_url, 'challenge/pwd?')):
            print("check password "+profile)
            try:
                drivers.refresh()
                show_tab(drivers)
                WebDriverWait(drivers,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='password']/div[1]/div/div[1]/input"))).send_keys(password)
                sleep(0.1)
                if(str(WebDriverWait(drivers,3).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='password']/div[1]/div/div[1]/input"))).get_attribute('value'))==""):
                    recheckfill(drivers,"password",password,By.XPATH,"//*[@id='password']/div[1]/div/div[1]/input")
                
                #button next
                show_tab(drivers)
                WebDriverWait(drivers,7).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='passwordNext']/div/button/span"))).click()
                adderecovry(drivers,profile,email,proxy,recovery,password)
            except:
                pass    
                
            
            try:
                erreur_password=WebDriverWait(drivers,3).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#yDmH0d > c-wiz > div > div.eKnrVb > div > div.j663ec > div > form > span > div.SdBahf.Fjk18.Jj6Lae > div.OyEIQ.uSvLId > div:nth-child(2) > span'))).text
                adderreurlog(str(erreur_password),profile,email,proxy)
                print("<error!> "+erreur_password)
                killtheard.append(drivers)
                drivers.quit()
                
            except:
                pass
            # try:
            #     disble(drivers,profile,email,proxy,recovery,password)
            # except:
            #     pass 
           
            try:
                
                if(str.__contains__(drivers.current_url, 'mail.google.com/mail/u/0/')):
                    addeconnected(profile,email,proxy)
                    print(email,"connected sucsufuly withoud recovry")
                    killtheard.append(drivers)
                    drivers.quit() 
                    
            except:
                pass
        else:pass
        try:
            if(str.__contains__(drivers.current_url,'gds.google.com')):              
                print("this account deblocked succese "+profile)
                show_tab(drivers)
                try:WebDriverWait(drivers,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'button'))).click()
                except:pass
            if(str.__contains__(drivers.current_url,'#inbox')): 
                drivers.get('https://myaccount.google.com/alert/nt/1668696496000?rfn%3D5%26rfnc%3D4%26eid%3D-7834588343699571215%26et%26origin%3D2')
                try:WebDriverWait(drivers,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'c-wiz>div>div:nth-child(2)>div>div>ul>li>a'))).click()
                except:pass
                
            show_tab(drivers)
            try:WebDriverWait(drivers,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'a[aria-label="Check activity"]'))).click()
            except:pass
            show_tab(drivers)
            # drivers.switch_to.window(drivers.window_handles[1])
            if(str.__contains__(drivers.current_url,'notifications/eid')): 
                show_tab(drivers)
                WebDriverWait(drivers,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div[aria-live="polite"]>div:nth-child(8)>button:nth-child(2)'))).click()
                sleep(4)
                show_tab(drivers)
                WebDriverWait(drivers,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div[aria-live="polite"]>div>div:nth-child(5)>button>span:nth-child(4)'))).click()
            if(str.__contains__(drivers.current_url,'security-checkup')): 
                show_tab(drivers)
                # drivers.close()
                # drivers.switch_to.window(drivers.window_handles[0])
            if(str.__contains__(drivers.current_url,'#inbox')): 
                show_tab(drivers)
                print("this account active "+profile)
                killtheard.append(drivers)
                drivers.quit() 
        except:pass

 
 
 
        
# def disble(drivers,profile,email,proxy,recovery,password):
#     if(str.__contains__(drivers.current_url,'iap')):
#         print("<error!> "+"verification number v1")
#         adderreurlog(str("verification number v1"),profile,email,proxy)
         
#         killtheard.append(drivers)
#         drivers.quit()
        
#     if(str.__contains__(drivers.current_url,'idvreenable')):
#         print("<error!> "+"verification number")
#         adderreurlog(str("verification number"),profile,email,proxy)  
#         killtheard.append(drivers)
#         drivers.quit()
#     if(str.__contains__(drivers.current_url,'disabled')):
#         print("<error!> ",email," is disabled")
#         disble(drivers,profile,email,proxy,recovery,password)
#         killtheard.append(drivers)
#         drivers.quit() 
        
        
        
def adderecovry(drivers,profile,email,proxy,recovery,password): 
    while True:
        try:
            sleep(4) 
            show_tab(drivers)
            
            if(str.__contains__(drivers.current_url,'signin/challenge/pwd?')):
                addepassword(drivers,profile,password,email,proxy,recovery)
            elif(str.__contains__(drivers.current_url,'challenge/ipe?')):
                drivers.back()
                sleep(2)
            elif(str.__contains__(drivers.current_url,'challenge/selection?')):
                try:
                    WebDriverWait(drivers,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div[data-challengetype='13']"))).click()
                    print(profile+' need num for confirmation closed now')
                    killtheard.append(drivers)
                    drivers.quit() 
                    break
                except:
                    pass
            if(str.__contains__(drivers.current_url,'signin/identifier?')):
                addemails(drivers,profile,proxy,email,password,recovery)
            
            if(str.__contains__(drivers.current_url,'challenge/selection?')):
                sleep(2)
                # WebDriverWait(drivers,20).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[3]/div/div[2]'))).click()
                WebDriverWait(drivers,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div[data-challengetype='12']"))).click()
                
                print('add recouvry in '+profile+' v1')
                WebDriverWait(drivers,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input[id="knowledge-preregistered-email-response"]'))).send_keys(recovery)
                sleep(0.1)
                scrollTo(drivers)
                if(str(WebDriverWait(drivers,3).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='knowledge-preregistered-email-response']"))).get_attribute('value'))==""):
                    recheckfill(drivers,"recovry",recovery,By.XPATH,"//*[@id='knowledge-preregistered-email-response']")
                show_tab(drivers)  
                WebDriverWait(drivers,7).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span'))).click()
                sleep(1)
            if(str.__contains__(drivers.current_url,'challenge/selection?')) :
                WebDriverWait(drivers,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'section>div>div>div>ul>li:nth-child(3)>div'))).click()
                print('add recouvry in '+profile+' v2')
                WebDriverWait(drivers,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input[id="knowledge-preregistered-email-response"]'))).send_keys(recovery)
                sleep(0.1)
                scrollTo(drivers)
                if(str(WebDriverWait(drivers,3).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='knowledge-preregistered-email-response']"))).get_attribute('value'))==""):
                    recheckfill(drivers,"recovry",recovery,By.XPATH,"//*[@id='knowledge-preregistered-email-response']")
                show_tab(drivers)  
                WebDriverWait(drivers,7).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span'))).click()
                sleep(1)
                
            
            if(str.__contains__(drivers.current_url,'info/unknownerror?')):  
                WebDriverWait(drivers,7).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div[role="presentation"]>div:nth-child(2)>div>div>div>div>button'))).click()    
            # send key number
            show_tab(drivers)
            sleep(1)
            if(str.__contains__(drivers.current_url,'signin/v2/challenge/kpe?')):
                print('add recouvry in '+profile)
                WebDriverWait(drivers,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input[id="knowledge-preregistered-email-response"]'))).send_keys(recovery)
                sleep(0.1)
                scrollTo(drivers)
                if(str(WebDriverWait(drivers,3).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='knowledge-preregistered-email-response']"))).get_attribute('value'))==""):
                    recheckfill(drivers,"recovry",recovery,By.XPATH,"//*[@id='knowledge-preregistered-email-response']")
                show_tab(drivers)  
                WebDriverWait(drivers,7).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span'))).click()
                
            
            show_tab(drivers) 
            sleep(2)
            if(str.__contains__(drivers.current_url,'disabled')):
                show_tab(drivers) 
                disble(drivers,profile,email,proxy,recovery,password)
                killtheard.append(drivers)
                drivers.quit() 
                break

            elif(str.__contains__(drivers.current_url,'speedbump/idvreenable?continue')):              
                print("this account need code telephone back in disble "+profile)
                # sleep(400)
                f = open("datasources/need_code_telephone.txt", "a")
                f.write('boith:'+str(profile)+':'+str(email)+'\n')
                f.close() 
                killtheard.append(drivers)
                drivers.quit() 
                break
            try:
                if(str.__contains__(drivers.current_url,'gds.google.com')):              
                    print("this account deblocked succese "+profile)
                    show_tab(drivers)
                    try:WebDriverWait(drivers,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'button'))).click()
                    except:pass
                if(str.__contains__(drivers.current_url,'#inbox')): 
                    drivers.get('https://myaccount.google.com/alert/nt/1668696496000?rfn%3D5%26rfnc%3D4%26eid%3D-7834588343699571215%26et%26origin%3D2')
                    try:WebDriverWait(drivers,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'c-wiz>div>div:nth-child(2)>div>div>ul>li>a'))).click()
                    except:pass
                
                show_tab(drivers)
                try:WebDriverWait(drivers,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'a[aria-label="Check activity"]'))).click()
                except:pass
                show_tab(drivers)
                    # drivers.switch_to.window(drivers.window_handles[1])
                if(str.__contains__(drivers.current_url,'notifications/eid')): 
                    show_tab(drivers)
                    WebDriverWait(drivers,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div[aria-live="polite"]>div:nth-child(8)>button:nth-child(2)'))).click()
                    sleep(4)
                    show_tab(drivers)
                    WebDriverWait(drivers,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div[aria-live="polite"]>div>div:nth-child(5)>button>span:nth-child(4)'))).click()
                if(str.__contains__(drivers.current_url,'security-checkup')): 
                    show_tab(drivers)
                    print("this account active "+profile)
                    killtheard.append(drivers)
                    drivers.quit() 
                    break
                
            except:pass
            if(str.__contains__(drivers.current_url,'#inbox')): 
                    show_tab(drivers)
                    print("this account active "+profile)
                    killtheard.append(drivers)
                    drivers.quit() 
                    break
            
            try:
                WebDriverWait(drivers,7).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'body'))).click()  

            except:
                print(profile+' closed now')
                break
        except:
            
           
        # try:
            
        #     erreur_recovry =WebDriverWait(drivers,7).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div.akwVEf > div.d2CFce.cDSmF > div > div.LXRPh > div.dEOOab.RxsGPe > div'))).text
        #     adderreurlog(str(erreur_recovry),profile,email,proxy)
        #     print("<error!> ",erreur_recovry)
        #     killtheard.append(drivers)
        #     drivers.quit() 
            
            
        # except:
        #     pass
            continue
    
        # try:
        #     if(str.__contains__(drivers.current_url,'signin/v2/challenge/selection?')):
        #             adderecovry(drivers,profile,email,proxy,recovery)
        #     elif(str.__contains__(drivers.current_url,'signin/v2/challenge/kpe?')):
        #         show_tab(drivers)  
        #         WebDriverWait(drivers,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input[id="knowledge-preregistered-email-response"]'))).send_keys(recovery)
        #         sleep(0.1)
        #         scrollTo(drivers)
        #         if(str(WebDriverWait(drivers,3).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='knowledge-preregistered-email-response']"))).get_attribute('value'))==""):
        #             recheckfill(drivers,"recovry",recovery,By.XPATH,"//*[@id='knowledge-preregistered-email-response']")
        #         show_tab(drivers)  
        #         WebDriverWait(drivers,7).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span'))).click()

        #     else:
        #         ckeckconnected =arealyconnected(drivers,profile)
        #         if(ckeckconnected):
        #             addeconnected(profile,email,proxy)
        #             print(email,"connected succssufuly")
        #             killtheard.append(drivers)
        #             drivers.quit()
        #         else:
        #             adderreurlog(str(erreur_recovry),profile,email,proxy)
        #             print("<error!> ",email," not connected")
        #             killtheard.append(drivers)
        #             drivers.quit()  
        # except:
        #     pass







def disble(drivers,profile,email,proxy,recovery,password):
 error=0
 while True:               
    try:
                
                sleep(2)
                if(str.__contains__(drivers.current_url,'signin/v2/challenge/kpe?')):
                    adderecovry(drivers,profile,email,proxy,recovery,password)
                # Commencer l'appel
                elif(str.__contains__(drivers.current_url,'disabled/explanation?')):
                    WebDriverWait(drivers,7).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div[role="presentation"]>div:nth-child(2)>div>div>div>div>button'))).click()
                show_tab(drivers) 
                if(str.__contains__(drivers.current_url,'disabled/appeal/received?')):
                    print(profile+" deja reported ")
                    break
                # next
                elif(str.__contains__(drivers.current_url,'disabled/appeal/reviewconsent?')):
                    drivers.find_element(By.CSS_SELECTOR,'div[data-is-touch-wrapper="true"]').click()
                    # add message
                    show_tab(drivers)  
                if(str.__contains__(drivers.current_url,'disabled/appeal/additionalinformation?')):                                                                
                    addmessage=WebDriverWait(drivers,6).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[*]/div/div[1]/div[2]/textarea')))
                    message=dopen("datasources\\messages.txt").getline(randint(1,  int(len(open("datasources\\messages.txt", 'r').readlines()))        ))
                    slow_type(addmessage,message)
                # suivant
                show_tab(drivers)
                if(str.__contains__(drivers.current_url,'disabled/appeal/contactaddress?')):
                    boitadd=dopen("datasources\\boit.txt").getline(randint(1,int(len(open("datasources\\boit.txt", 'r').readlines()))))  
                    # add boit                              
                    addboit=WebDriverWait(drivers,6).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[*]/div[1]/div/div[1]/div/div[1]/input')))
                    slow_type(addboit,boitadd)
                    try:
                        WebDriverWait(drivers,7).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div[role="presentation"]>div:nth-child(2)>div>div>div>div>button'))).click()
                    
                    except:pass
                    WebDriverWait(drivers,7).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'body'))).click()
                    sleep(4)
                    # killtheard.append(drivers)
                    # drivers.quit()
                    # drivers.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/button').click()
                    # fine
                    f = open("datasources/historique_disbl.txt", "a")
                    f.write(f"this email : {email} recouvry : {boitadd} at time : {datetime.datetime.now()}\n")
                    f.close() 
                    print(f"this email : {email} recouvry : {boitadd}")   
                    # killtheard.append(drivers)
                    # drivers.quit()
                    break
    except Exception as e:
        # if error==20:
        #     print('chi mochkil f chkl hada 20 mara ou howa kay3awd')
        #     break
        # error+=1
        # print("probleme in : "+profile+' Exception:  ' + str(e))
        print("probleme in : "+profile)
        sleep(randint(2,4))
        continue
       






         
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
 
 
 
   
  