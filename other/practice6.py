from bs4 import BeautifulSoup

html='''
<html>
<head>
<title>this is a web page</title>
<body>
    <p>
    this is a first paragraf
    </p>
    <p>
    this is a second paragraf
    </p>
</body>
</head>
</html>
'''

soup=BeautifulSoup(html,"html.parser")
title=soup.title.get_text()
print(title)

print('-'*100)

body=soup.body.get_text()
print(body)

print('='*100)    

soups=soup.body.find_all('p')

for i in soups:
    print(soup.get_text())
    print('-'*100)