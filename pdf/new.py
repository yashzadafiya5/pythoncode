import xlrd
import xlsxwriter   

file = ("F:\\avepdf.xlsx")     
wb = xlrd.open_workbook(file)
sheet = wb.sheet_by_index(0) 
# line=sheet.cell_value(0, 0)
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
            try:
                if water[goat]==" ":
                    fire=goat
                    stone=fire+1
                    if water[stone] in aplha:
                        air=stone-1
                        lava=lava+1
                        lol.append(air)
                        # print(lol)
            except KeyError:
                print()
    
    # print(lol)
    badsha1=[]
    listToStrs = ''.join([str(param) for param in line])
    ne=listToStrs[0:lol[0]]
    badsha1.append(ne)
    # print(badsha1)
    

    x=0
    b=x
    while x<lava:
        b=x+1
        try:
            
            k=listToStrs[lol[x]:lol[b]]

            badsha1.append(k)
            # print(badsha1)
            
            
        except IndexError:
            print()
        x=x+1
    
    count=0
    while count<lava:
        count=count+1
        str_count=str(count)
        name="data"+str_count 

    enjoy=''.join(str(num)for num in badsha1)
    joo=enjoy.split(' ')
    new={}
    final=[]
    name=1
    for j in joo:
        new[name]=j
        name=name+1 
    final.append(new)
    # print(final)
    
    # new=[]
    # final=[]
    # name=1
    # for j in badsha1:
    #     new[name]=j
    #     name=name+1 
    # # moi=[]
    # final.append(new)
    # print(new)
    # golion.append(new)
    # print(golion)

    go=1
    while go<lava:
        workbook=xlsxwriter.Workbook("pdfdata.xlsx")
        worksheet=workbook.add_worksheet("firstsheet")

        worksheet.write(0,0,"#")
        worksheet.write(0,1,1)
        worksheet.write(0,2,2)
        worksheet.write(0,3,3)
        worksheet.write(0,4,4)
        for index,entry in enumerate(final):
            worksheet.write(index+1,0,index)
            worksheet.write(index+1,1,entry[1])
            worksheet.write(index+1,2,entry[2])
            worksheet.write(index+1,3,entry[3])
            worksheet.write(index+1,3,entry[4])
            
        workbook.close()
        go=go+1
    
    i=i+1
