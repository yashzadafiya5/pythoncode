from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import random
import requests
import time

#Start of login
option=webdriver.ChromeOptions()
name=["param patel"]
browser=webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\chromedriver.exe")
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
browser.get("https://ewise.paramounttpa.com/Dashboard.aspx?Id=qOQ0FwWQzDEj77RtDxNScw==&Dept=6NTT+O70MWDJATrVsv64vg==&Usercode=11727#")
time.sleep(3)
image=browser.find_element(By.ID,"dvRightArrow")
image.click()
time.sleep(3)
investigation_btn=browser.find_element(By.ID,"anchrInvest")
investigation_btn.click()
browser.get("https://ewise.paramounttpa.com/Dashboard.aspx?Id=qOQ0FwWQzDEj77RtDxNScw==&Dept=6NTT+O70MWDJATrVsv64vg==&Usercode=11727#")
time.sleep(3)
claim_inv=browser.find_element(By.ID,"anchrFRD")
claim_inv.click()
browser.get("https://ewise.paramounttpa.com/Investigation_Search.aspx?Id=175&Dept=+zEKtKmKuVt5qKXPnBIeUQ==&DeptCode=6NTT+O70MWDJATrVsv64vg==")
#End of getting to claim investigation page
#Start of finding form fill up
time.sleep(3)
ccnnumber=browser.find_element(By.ID,"txtCcnSrch6")
ccnnumber.send_keys('5593992')
btnactive=browser.find_element(By.ID,"btnSearchActive")
btnactive.click()
time.sleep(3)
btninvestigate = browser.find_element(By.ID,"anchrInvestigate1")
browser.implicitly_wait(10)
ActionChains(browser).move_to_element(btninvestigate).click(btninvestigate).perform()
time.sleep(5)


