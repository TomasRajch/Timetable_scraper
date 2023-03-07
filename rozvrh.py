from cmath import pi # pro goniometrické funkce
import math # pro goniometircké funkce
import geopy # pro výpočty na Zemi
import geopy.distance # pro výpočty na Zemi
import requests # pro webscraping
import selenium # pro webscraping
from os import link # pro webscraping
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np
from csv import writer
from pathlib import Path

n= 0
day, lesson, half = 1, 0, 0
base_folder = Path(__file__).parent.resolve()
data_file = base_folder / "data.csv"
with open('data.csv', 'w', buffering=1, newline='') as f:
    data_writer = writer(f)
    data_writer.writerow(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

linkstring = "https://bakalari.mgplzen.cz/Timetable/Public/Permanent/Class/IO"
options = Options() # nastavuje možnosti Selenia
options.headless = True # zakazuje otevření Chrome okna (Chrome bez GUI)
options.add_argument("--window-size=1920,1200") # nastavení velikosti obrazovky pro emulaci
options.add_argument("--allow-mixed-content") # nastavení pro stahování případných obrázků (nevyužito)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) # spouští okno Selenia
driver.get(linkstring) # otevírá zadanou URL

class_number = 1

class_name = driver.find_element(By.XPATH, '//*[@id="selectedClass"]').text
class_name = class_name.split()
for x in class_name:
    class_number += 1
    class_xpath = '//*[@id="selectedClass"]/option[{}]'.format(class_number)
    print(class_xpath)
    class_code = driver.find_element(By.XPATH, class_xpath).get_attribute("value")
    print("-------------------------")
    print(class_code)
    print("-------------------------")
    linkstring = "https://bakalari.mgplzen.cz/Timetable/Public/Permanent/Class/{}".format(class_code)
    driver.get(linkstring)
    print(linkstring)
    day = 1
    for i in range(5):
        data_day = list()
        day += 1
        lesson = 0
        for i in range(9):
            half = 0
            lesson += 1    
            altitudeXPath = '//*[@id="main"]/div[{}]/div[2]/div[{}]'.format(day, lesson)# hledá zadaný element
            altitude = driver.find_element(By.XPATH, altitudeXPath).text # exportuje vyhledaný string
            if altitude == "":
    #            print(" ")
                data_day.append(altitude)
                print(data_day)
            else:
    #            print("--------")
                try:
                    data_half = list("")
                    for half in range(6):
                        half += 1
                        altitudeXPath = '//*[@id="main"]/div[{}]/div[2]/div[{}]/div/div[{}]/div/div[3]'.format(day, lesson, half)
                        altitude = driver.find_element(By.XPATH, altitudeXPath).text # exportuje vyhledaný string
    #                    print(altitude)
                        print(data_half)
                        data_half.append(altitude)
                except:
                    data_day.append(data_half)
                    pass
        with open("data.csv", "a", encoding="utf-8", newline='') as f:
            data_writer = writer(f)
            data_writer.writerow(data_day)
    
    with open("data.csv", "a", encoding="utf-8", newline='') as f:
        data_writer = writer(f)
        data_writer.writerow("")




#1. hodina
    #po - //*[@id="main"]/div[2]/div[2]/div[1]
    #ut - //*[@id="main"]/div[3]/div[2]/div[1]
    #st - //*[@id="main"]/div[4]/div[2]/div[1]
    #čt - //*[@id="main"]/div[5]/div[2]/div[1]
    #pa - //*[@id="main"]/div[6]/div[2]/div[1]

# pondělí
    # 1 - //*[@id="main"]/div[2]/div[2]/div[1]
    # 2 - //*[@id="main"]/div[2]/div[2]/div[2]
    # 3 - //*[@id="main"]/div[2]/div[2]/div[3]
    # 4 - //*[@id="main"]/div[2]/div[2]/div[4]
    # 5 - //*[@id="main"]/div[2]/div[2]/div[5]
    # 6 - //*[@id="main"]/div[2]/div[2]/div[6]
    # 7 - //*[@id="main"]/div[2]/div[2]/div[7]

# polovina
    # podnělí - 1 hodina - Tv1 - //*[@id="main"]/div[2]/div[2]/div[1]/div/div[1]/div/div[3]
    # pondělí - 1 hodina - Tv2 - //*[@id="main"]/div[2]/div[2]/div[1]/div/div[2]/div/div[3]
    # podnělí - 2 hodina - Tv1 - //*[@id="main"]/div[2]/div[2]/div[2]/div/div[1]/div/div[3]
    # pondělí - 2 hodina - Tv2 - //*[@id="main"]/div[2]/div[2]/div[2]/div/div[2]/div/div[3]
    # pondělí - 4 hodina - AN - //*[@id="main"]/div[2]/div[2]/div[4]/div/div[1]/div/div[3]
    # pondělí - 4 hodina - NA - //*[@id="main"]/div[2]/div[2]/div[4]/div/div[2]/div/div[3]
    # 5 - 
    # 6 - 
    # 7 - 

    #//*[@id="selectedClass"]/option[2]
    #//*[@id="selectedClass"]
    #//*[@id="selectedClass"]/option[17]