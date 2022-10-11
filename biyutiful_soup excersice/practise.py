from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import random
import requests
import time

def secondform(complain):

    option=webdriver.ChromeOptions()
    name=["param patel"]
    browser=webdriver.Chrome(executable_path="C:\chromedriver.exe")
    browser.get("https://ewise.paramounttpa.com/")
    loginusername=browser.find_element("name","inpUserName")
    loginpassword=browser.find_element("name","inpPassword")
    submit=browser.find_element("name","btnLogin")
    loginusername.send_keys('11727')
    loginpassword.send_keys('Osho@2232')
    submit.click()
    #End of login
    #Start of getting to claim investigation page
    browser.get("https://ewise.paramounttpa.com/ProductSelection.aspx")
    time.sleep(3)
    ewise_button=browser.find_element(By.ID,"anchrEWISE")
    ewise_button.click()