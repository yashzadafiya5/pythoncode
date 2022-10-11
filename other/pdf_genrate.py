# import xlrd     
# import re
# from csv import writer
# lst=[]
# values=[]
# second=[]
# # lists=["FINLAND w 15 16 PORTUGAL w 3 28 CANADA 20159 CEYLON 28" ]
# # def text_num_split(item):
# #     for index, letter in enumerate(item, 0):
# #         if letter.isdigit():
# #             return [item[:index],item[index:]]

# file = ("D://avepdf.xlsx")     
# wb = xlrd.open_workbook(file)
# sheet = wb.sheet_by_index(0)     
# line=sheet.cell_value(0, 0)       
# # print(line)
# #ldsclsdlc
# print(line)
# def getpdf(line):
#     lst=[]   
#     second=[] 
#     listToStr = ''.join([str(param) for param in line])
#     # print(listToStr)
#     x=listToStr.split()
#     lst.append(x)
#     lst=x[0:4:3]
#     second.append(lst)
#     lst=x[4:8:3]
#     second.append(lst)
#     lst=x[8:10]
#     second.append(lst)
#     lst=x[10:13]
#     second.append(lst)
#     print(second)
#     return second
# getpdf(line)

# A = ['1','2','3','4','5','6','7','8','9','10']
# count=0
# result = {}
# for i in line:
#    print(i,end='')
#    result.__setitem__(count,i)
#    count=count+1   
# print(result)
 
# for key,value in result.items():
#     # print(key,"",value,end=' ')
#     if value in A:
#         print(key)
#         key=key+1
#         if result[key]==' ':
#             print(f' found ')
# print("good byy")  




import pandas as pd
from csv import writer
df = pd.read_excel (r"f:\avepdf.xlsx")


with open("pdfgenrate.csv",'w',encoding='utf8',newline='')as f:
    thewriter=writer(f)
    header=['title','location','price','area']
    thewriter.writerow(header)
    thewriter.writerow(df)