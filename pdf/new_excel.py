import xlrd
import xlsxwriter   

file = ("F:\\New1.xlsx")     
wb = xlrd.open_workbook(file)
sheet = wb.sheet_by_index(0) 
line=sheet.cell_value(0, 0)