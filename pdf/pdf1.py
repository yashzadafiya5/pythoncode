import xlrd
import xlsxwriter
file = ("F:\\avepdf.xlsx")     
wb = xlrd.open_workbook(file)
sheet = wb.sheet_by_index(0) 
# line=sheet.cell_value(0, 0)
# golion=[]   
# integer=['9','8','7','6','5','4','3','2','1','0']
# alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]   
# # golion.append(line)
# line_split=" ".join([str(i)for i in line])
# line_split.split(" ")
# # print(line)
# count=1
# lol=[]
# new={}
# lava=0
# for k in line_split:
#     new[count]=k
#     count=count+1
    
# # print(new)
# for key,value in new.items():
#         if new[key] in integer:
#             newdata=key
#             newdata+=1
#             if new[newdata]==" ":
#                 data=newdata
#                 if new[data] in alpha:
#                         air=data-1
#                         lava=lava+1
#                         lol.append(air)
# print(lol)
golion=[]      
i=0

while i<5:    
    line=sheet.cell_value(i, 0)
    count=1
    water={}
    lol=[]
    integer=['9','8','7','6','5','4','3','2','1','0']
    aplha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
    lava=0
    for r in line:
        water[count]=r
        count=count+1
    for key,value in water.items():
        if water[key] in integer:
            goat=key
            goat=goat+1
            
            if water[goat]==" ":
                fire=goat
                stone=fire+1
                if water[stone] in aplha:
                    air=stone-1
                    lava=lava+1
                    lol.append(air)
                    
    i=i+1
print(lol)
print(water)