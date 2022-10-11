from bs4 import BeautifulSoup
from urllib.request import urlopen

pagesoursedata=[]
WebPageAddres = f'''https://ewise.paramounttpa.com/Investigation_Search.aspx?Id=175&Dept=+zEKtKmKuVt5qKXPnBIeUQ==&DeptCode=6NTT+O70MWDJATrVsv64vg=='''

file = urlopen(WebPageAddres)
html = file.read()

soup = BeautifulSoup(html,'html.parser')
# print(soup)
listToStr = ''.join([str(param) for param in soup])
index = listToStr.find('<td>5320887</td>')
print(index)
# while True:
#     if index>0:
#         print("ok")
#     else:
#         break