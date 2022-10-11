# import xlrd     

# file = ("F:\\avepdf.xlsx")     
# wb = xlrd.open_workbook(file)
# sheet = wb.sheet_by_index(0)     
# line=sheet.cell_value(0, 0) 


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
integer=['9','8','7','6','5','4','3','2','1','0']
lists=[1,5,0.5]
count=0
for i in lists:
    if integer in lists:    
        print('**')
        count=count+1
    else:    
        print('---')
    
