import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)

soup=BeautifulSoup(html,"html.parser")

cells = soup.find_all('td')
# column = soup.find_all('tr')

# print(column)
dataset=pd.DataFrame(cells)
dataset.head(10)
print(dataset)