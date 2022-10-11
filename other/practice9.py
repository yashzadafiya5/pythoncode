import xlsxwriter



data=[
    {
        "name":"yash zadafiya",
        "std":"it enginering",
        "age":"21",
        "country":"india"
    },    
    {
        "name":"jay andhariya",
        "std":"bba student",
        "age":"22",
        "country":"india"
    },         
    {
        "name":"anjli ghelani",
        "std":"bcom student",
        "age":"24",
        "country":"india"
    }
]

workbook=xlsxwriter.Workbook("demo.xlsx")
worksheet=workbook.add_worksheet("firstsheet")

worksheet.write(0,0,"#")
worksheet.write(0,1,"name")
worksheet.write(0,2,"std")
worksheet.write(0,3,"age")
worksheet.write(0,4,"country")

for index,entry in enumerate(data):
    worksheet.write(index+1,0,str(index))
    worksheet.write(index+1,1,entry["name"])
    worksheet.write(index+1,2,entry["std"])
    worksheet.write(index+1,3,entry["age"])
    worksheet.write(index+1,3,entry["country"])
    
workbook.close()