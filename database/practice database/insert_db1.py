import mysql.connector as con 

db=con.connect(host="localhost",user="root",passwd="",database="students",port="3306")

print("connection astablised...........")

sname=input("enter your name:")
smobileno=int(input("enter your mobileno:"))
sweight=float(input("enter your weight:"))
sgender=int(input("enter your sgender you are male='0' female='1':"))

mycursor=db.cursor()


sql="insert into  studentdetail (sname,smobileno,sweight,sgender)values(%s,%s,%s,%s)" 

values=[sname,smobileno,sweight,sgender]

mycursor.execute(sql,values)

db.commit()

print("inserted.....",mycursor.rowcount)


