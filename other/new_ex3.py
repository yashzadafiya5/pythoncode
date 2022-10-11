#find a user are enter a city and is city's temprature 

from bs4 import BeautifulSoup
from urllib.request import urlopen
city=input("enter a city'sname :=")

WebPageAddress = f"https://www.timeanddate.com/weather/india/{city}"

file = urlopen(WebPageAddress)
html = file.read()

soup = BeautifulSoup(html,'html.parser')

weather=soup.body.find("div",{"class":"h2"})
for paragraph in weather:
    print(paragraph.get_text())
#("div",{"class":"read-more-content"})
#('p',{'class':'b-forecast__table-description-content'})
#("table",{"class":"b-forecast__table js-forecast-table"})
#("p",{"class":"b-forecast__table-description-content"})