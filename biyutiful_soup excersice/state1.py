from bs4 import BeautifulSoup
from urllib.request import urlopen



def dieselprice(city):
    
    WebPageAddres = f"https://traveltriangle.com/blog/best-cafes-in-{city}/"

    file = urlopen(WebPageAddres)
    html = file.read()

    soup = BeautifulSoup(html,'html.parser')

    items=soup.body.find('div',{ })
    for price in items:
        print(price.get_text())

city=input("enter a city'sname :=")
dieselprice(city)
# petrolprice(city)
