from bs4 import BeautifulSoup
from urllib.request import urlopen

def getprice(city_name):

    WebPageAddress = (f"https://www.ndtv.com/fuel-prices/diesel-price-in-{city_name}-city")
    file=urlopen(WebPageAddress)
    html = file.read()
    soup = BeautifulSoup(html,'html.parser')
    prices=soup.body.find('span',{'class':'font-b color-blue'})
    for price in prices:
        print(price.get_text())


if __name__=="__main__":
    cityname="surat"
    getprice(cityname)