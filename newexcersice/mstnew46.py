from bs4 import BeautifulSoup
from urllib.request import urlopen


# f = open("html1.html", "a")
# f.write("param patel")
# f.close()

from selenium import webdriver
import time

web=webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chrome.exe")
i=web.get('file:///C:/Users/user/Downloads/html1.html')
print(i)
print(web)
# time.sleep(2)

# name="Param patel"
# last=web.find_element_by_xpath('//*[@id="name"]')
# last.send_keys(name)

# WebPageAddres = f"file:///C:/Users/user/Downloads/html1.html"
# file = urlopen(WebPageAddres)
# print(file)