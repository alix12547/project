import glob
import os.path
import time

def get_latest_image(new_name ):
    dirpath='C:/Users/admin4/Downloads'
    print(len(dirpath))
    valid_files = [os.path.join(dirpath, filename) for filename in os.listdir(dirpath)]
    valid_files = [f for f in valid_files if '.' in f and \
        f.rsplit('.',1)[-1] in ('jpg','jpeg','png') and os.path.isfile(f)]
    if not valid_files:
        raise ValueError("No valid images in %s" % dirpath)
    pathlast= max(valid_files, key=os.path.getmtime)
    split_tup = os.path.splitext(os.path.split(pathlast)[1])
    os.rename(pathlast, "datasources\\"+new_name+split_tup[1])

# get_latest_image()
from selenium import webdriver
def changepathdownload():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    prefs = {"profile.default_content_settings.popups": 0,
                "download.default_directory": 
                            os.getcwd()+'\image',#IMPORTANT - ENDING SLASH V IMPORTANT
                "directory_upgrade": True}
    options.add_experimental_option("prefs", prefs)
    browser=webdriver.Chrome(options=options)
    time.sleep(6000)

get_latest_image("new_name2" )
# from PIL import Image

# Jpeg = Image.open("profil.png")

# print(Jpeg.info, Jpeg.format, Jpeg.mode, Jpeg.size)