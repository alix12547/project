from time import sleep
from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import os


from selenium import webdriver
driver = webdriver.Firefox()

# options2 = webdriver.FirefoxOptions()
# profile = "profile1"
# path = 'C:\\Users\\admin4\\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles' + profile
# isExist = os.path.exists(path)
# options2.add_argument(
#     '--no-first-run --no-service-autorun --password-store=basic')
# options2.headless=True
# options2.add_argument('--headless')
# if isExist == 0:
#     options2.add_experimental_option("prefs", {
#             "profile.name": profile
#         })
#     options2.add_argument('--user-data-dir='+path)
print("donne")
sleep(600)
    # options2.add_argument('--user-data-dir='+path)
    # listop.append({"option":options2,"profil":profile,'index':i})
# profile_path = r'C:\Users\Admin\AppData\Roaming\Mozilla\Firefox\Profiles\s8543x41.default-release'
# options=Options()
# options.set_preference('profile', profile_path)
# options.set_preference('network.proxy.type', 1)
# options.set_preference('network.proxy.socks', '127.0.0.1')
# options.set_preference('network.proxy.socks_port', 9050)
# options.set_preference('network.proxy.socks_remote_dns', False)
# service = Service(r'C:\Users\admin4\Desktop\project\geckodriver.exe')
# driver = Firefox(service=service, options=options)
# driver.get("https://www.google.com")
# driver.quit()
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
path='C:\\Users\\admin4\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\something.default-release'
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
profile = webdriver.FirefoxProfile('C:\\Users\\admin4\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\something.default-release')

PROXY_HOST = "12.12.12.123"
PROXY_PORT = "1234"
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", PROXY_HOST)
profile.set_preference("network.proxy.http_port", int(PROXY_PORT))
profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()
# desired = DesiredCapabilities.FIREFO

# driver = webdriver.Firefox(firefox_profile=profile, desired_capabilities=desired)
driver.get('http://inventwithpython.com')
sleep(2000)
