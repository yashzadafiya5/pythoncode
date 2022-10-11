from tkinter.ttk import Separator
from bs4 import BeautifulSoup
from urllib.request import urlopen  
def gethub(profilename):
    
    WebPageAddres = f"https://github.com/{profilename}"


    file = urlopen(WebPageAddres)
    html = file.read()
    soup = BeautifulSoup(html,'html.parser')
    
    content=soup.body.find('ol',{'class':"d-flex flex-wrap list-style-none gutter-condensed mb-4"})
    for new in content:
        news= ' '.join(new.get_text(strip=True, separator=" ").split())
        print(news)
        
profilename=input("enter your gethub profilename:")
gethub(profilename)