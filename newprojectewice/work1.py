from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import random
import requests
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen

option=webdriver.ChromeOptions()
# option.add_argument("-incognito")/
# print(option)
name=["param patel"]
browser=webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\chromedriver.exe")
browser.get("https://ewise.paramounttpa.com/")
# print(browser)

loginusername=browser.find_element("name","inpUserName")
loginpassword=browser.find_element("name","inpPassword")
submit=browser.find_element("name","btnLogin")
loginusername.send_keys('11727')
loginpassword.send_keys('Osho@2232')
submit.click()
# browser=webdriver.Chrome(executable_path="C:\chromed
# /river.exe")
# print(browser)
browser.get("https://ewise.paramounttpa.com/ProductSelection.aspx")
time.sleep(5)
# print(browser)
ewise_button=browser.find_element(By.ID,"anchrEWISE")
ewise_button.click()
# https://ewise.paramounttpa.com/Dashboard.aspx?Id=qOQ0FwWQzDEj77RtDxNScw==&Dept=6NTT+O70MWDJATrVsv64vg==&Usercode=11727
browser.get("https://ewise.paramounttpa.com/Dashboard.aspx?Id=qOQ0FwWQzDEj77RtDxNScw==&Dept=6NTT+O70MWDJATrVsv64vg==&Usercode=11727#")
time.sleep(5)
image=browser.find_element(By.ID,"dvRightArrow")
image.click()
time.sleep(5)
investigation_btn=browser.find_element(By.ID,"anchrInvest")
investigation_btn.click()

browser.get("https://ewise.paramounttpa.com/Dashboard.aspx?Id=qOQ0FwWQzDEj77RtDxNScw==&Dept=6NTT+O70MWDJATrVsv64vg==&Usercode=11727#")
time.sleep(5)
claim_inv=browser.find_element(By.ID,"anchrFRD")
claim_inv.click()
# time.sleep(5)
browser.get("https://ewise.paramounttpa.com/Investigation_Search.aspx?Id=175&Dept=+zEKtKmKuVt5qKXPnBIeUQ==&DeptCode=6NTT+O70MWDJATrVsv64vg==")
time.sleep(5)
ccnnumber=browser.find_element(By.ID,"txtCcnSrch6")
ccnnumber.send_keys('5593992')
btnactive=browser.find_element(By.ID,"btnSearchActive")
btnactive.click()
time.sleep(5)
invastigation=browser.find_element(By.ID,"anchrInvestigate1")
invastigation.click()
time.sleep(10)


WebPageAddres = f"https://ewise.paramounttpa.com/Investigation_Search.aspx?Id=175&Dept=+zEKtKmKuVt5qKXPnBIeUQ==&DeptCode=6NTT+O70MWDJATrVsv64vg=="

file = urlopen(WebPageAddres)
html = file.read()
markup='''<i data-toggle="tooltip" data-placement="bottom" title="Telephonic" class="glyphicon glyphicon-earphone" style="font-size:15px"></i>'''
soup = BeautifulSoup(markup)
print(soup.i)
# prices=soup.body.find('i',{'class':'glyphicon glyphicon-earphone'})


# button = browser.find_element(By.ID,"anchrEWISE")
# browser.implicitly_wait(10)
# ActionChains(browser).move_to_element(button).click(button).perform()
# browser.get("https://ewise.paramounttpa.com/Investigation_Search.aspx?Id=175&Dept=+zEKtKmKuVt5qKXPnBIeUQ==&DeptCode=6NTT+O70MWDJATrVsv64vg==")
# ccnnumber=browser.find_element(By.ID,"txtCcnSrch6")
# ccnnumber.send_keys('5593992')
# btnactive=browser.find_element(By.ID,"btnSearchActive")
# btnactive.click()
# time.sleep(60)
# website_form='https://ewise.paramounttpa.com/ProductSelection.aspx'
# response = requests.get(website_form, data={'name':name})
# print("name is "+response.text)
# response_got=response.text
# file1=open('form_data.txt','w')
# file1.write(response_got)
# file1.close()