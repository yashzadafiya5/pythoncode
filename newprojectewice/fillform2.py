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

def fill_form(complaints,addmisiondate,room,contactpersonname,hospitalnumber,treatingdoctor,qulificatondoctor,registrationnumber,patientname,patientnumber,hospitalname,city,bed):
    web=webdriver.Chrome("C:\Program Files\Google\Chrome\chromedriver.exe")
    web.get("http://localhost/submit/cash_inv.php")
    dod=web.find_element(By.NAME,"complain")
    dod.send_keys(complaints)
    time.sleep(1)
    dod=web.find_element(By.NAME,"add_date")
    dod.send_keys(addmisiondate)
    time.sleep(1)
    dod=web.find_element(By.NAME,"room")
    dod.send_keys(room)
    time.sleep(1)
    dod=web.find_element(By.NAME,"hos_contact_per")
    dod.send_keys(contactpersonname)
    time.sleep(1)
    dod=web.find_element(By.NAME,"hos_number")
    dod.send_keys(hospitalnumber)
    time.sleep(1)
    dod=web.find_element(By.NAME,"tre_doctor")
    dod.send_keys(treatingdoctor)
    time.sleep(1)
    dod=web.find_element(By.NAME,"qua_doc")
    dod.send_keys(qulificatondoctor)
    time.sleep(1)
    dod=web.find_element(By.NAME,"reg_doc_number")
    dod.send_keys(registrationnumber)
    time.sleep(1)
    dod=web.find_element(By.NAME,"pat_name")
    dod.send_keys(patientname)
    time.sleep(1)   
    dod=web.find_element(By.NAME,"pat_number")
    dod.send_keys(patientnumber)
    time.sleep(1)
    dod=web.find_element(By.NAME,"hos_name")
    dod.send_keys(hospitalname)
    time.sleep(1)   
    dod=web.find_element(By.NAME,"city")
    dod.send_keys(city)
    time.sleep(1)   
    dod=web.find_element(By.NAME,"beds")
    dod.send_keys(bed)
    time.sleep(1)
    btnactive=web.find_element(By.NAME,"submit")
    btnactive.click()

complaints ="yash"
addmisiondate="13/02/2013"
room="Dulex"
contactpersonname="bhavdeep"
hospitalnumber="0221-263-125"
treatingdoctor="good"
qulificatondoctor="mbbs"
registrationnumber="1225"
patientname="vishal joshi"
patientnumber="9857458141"
hospitalname="kiran hospital"
city="surat"
bed="15"
fill_form(complaints,addmisiondate,room,contactpersonname,hospitalnumber,treatingdoctor,qulificatondoctor,registrationnumber,patientname,patientnumber,hospitalname,city,bed)
