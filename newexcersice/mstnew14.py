# 14. Scrape Table From a Website using Python 
from selenium import webdriver

driver=webdriver.Chrome("c:\webdrivers\choromedriver.exe")
driver.get('https://www.worldometers.info/coronavirus/')
driver.maximize_window()

alldata=driver.find_elements_by_xpath('//tbody/tr/td[2]/a')
for new in alldata:
    print(new.text)