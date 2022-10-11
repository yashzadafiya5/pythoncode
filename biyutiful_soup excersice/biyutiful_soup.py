# #find a user are enter a city and is city's petrol and diesal price catch

# # from bs4 import BeautifulSoup
# # from urllib.request import urlopen
# # from csv import writer


# # def dieselprice(city):
    
# #     WebPageAddres = f'https://www.creditmantri.com/diesel-price-in-{city}/'

# #     file = urlopen(WebPageAddres)
# #     html = file.read()

# #     soup = BeautifulSoup(html,'html.parser')

# #     prices=soup.body.find('div',{'class':'col-sm-8 col-xs-8 text-center'})
# #     for price in prices:
# #         print(price.get_text())
    
def petrolprice(city):
# #     WebPageAddress = f'https://www.creditmantri.com/petrol-price-in-{city}/'
# #     file = urlopen(WebPageAddress)
# #     html = file.read()

# #     soup = BeautifulSoup(html,'html.parser')

# #     prices=soup.body.find('div',{'class':'col-sm-8 col-xs-8 text-center'})
# #     for price in prices:
# #         print(price.get_text())
        
    
        
# # div.row>table.table-responsive>tbody>tr>td>i.glyphicon glyphicon-earphone           
# # city=input('enter a city'sname :=')
# # dieselprice(city)
# # petrolprice(city)

# # WebPageAddres = f'https://ewise.paramounttpa.com/Investigation_Search.aspx?Id=175&Dept=+zEKtKmKuVt5qKXPnBIeUQ==&DeptCode=6NTT+O70MWDJATrVsv64vg=='

# # file = urlopen(WebPageAddres)

# # html = file.read().decode('utf-8')
# # soup = BeautifulSoup(html.encode('utf-8'))

# # # html = br.response().read().decode('utf-8')
# # # prices=soup.find_all('th')
# # # prices=soup.find_all('td')
# # table = soup.find('table', id='tblClmDtls')
# # rows = table.find_all('tr')
# # print(table,rows)

# # for elem in prices.children:
# #     print(elem)

# # file = urlopen(WebPageAddres)
# # html = file.read()
# # navbar=soup.find(id='')
# # soup = BeautifulSoup(markup)
# # if soup in investigation:
# #     break
# # print(soup.prettify)


# # with open('new.csv','w',encoding='utf8',newline='')as f:
# #     thewriter=writer(f)
# #     header=['title','location','price','area']
# #     thewriter.writerow(header)
# #     for list in lists:
# #         title=list.find('a',class_='listing-search-item_link--title').text.replace('\n','')
# #         location=list.find('a',class_='listing-search-item_link--title').text.replace('\n','')
# #         price=list.find('a',class_='listing-search-item_link--title').text.replace('\n','')
# #         area=list.find('a',class_='listing-search-item_link--title').text.replace('\n','')
# #         info=[title,location,price,area]
# #         thewriter.writerow(info) 


# # import re
# # from bs4 import BeautifulSoup
# # from urllib.request import urlopen

# # pagesoursedata=[]
# # WebPageAddres = f'''https://ewise.paramounttpa.com/Investigation_Search.aspx?Id=175&Dept=+zEKtKmKuVt5qKXPnBIeUQ==&DeptCode=6NTT+O70MWDJATrVsv64vg=='''

# # file = urlopen(WebPageAddres)
# # html = file.read()

# # soup = BeautifulSoup(html,'html.parser')
# # # print(soup)
# # listToStr = ''.join([str(param) for param in soup])
# # # print(listToStr)

# # # string = 'My email is email@example.com and I use it a lot.'
# # # if listToStr in 5320887:
# # search_word = re.search(r"5320887",listToStr)
# # if search_word:
# #     print(search_word.group())
# # else:
# #     print('Word was not found.')

# # from bs4 import BeautifulSoup
# # import requests

# # WebPageAddress = f'https://ewise.paramounttpa.com/Investigation_Search.aspx?Id=175&Dept=+zEKtKmKuVt5qKXPnBIeUQ==&DeptCode=6NTT+O70MWDJATrVsv64vg=='
# # file = requests.get(WebPageAddress)
# # soup = BeautifulSoup(file.text,'html.parser')
# # leg_table=soup.find('table' ,class_ ="table-bordered table-striped")

# # for team in leg_table.find_all("tbody"):
# #     rows=team.findall('tr')
# #     for row in rows:
# #         pl_team=row.findall('td',class_ ='lablecolor')
        
# # print(pl_team)
            
# # # for li in leg_table:
# # #     print(li)
# # # for price in prices:
# # #     print(price.get_text())
    
    
# # import pandas as pd

# # df=pd.read_html('https://ewise.paramounttpa.com/Investigation_Search.aspx?Id=175&Dept=+zEKtKmKuVt5qKXPnBIeUQ==&DeptCode=6NTT+O70MWDJATrVsv64vg==', parse_dates=True)

# # print(df)
# # # df[0].to_csv('append.csv')

# from selenium import webdriver

# driver=webdriver.Chrome('C:\Program Files\Google\Chrome\chromedriver.exe')

# driver.get('https://stackoverflow.com/questions/70827161/get-specific-word-from-a-sentence-if-it-has-a-certain-character')
# print(f"website title is :={driver.ti}")

# driver.quit()
