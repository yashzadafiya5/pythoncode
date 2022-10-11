import mysql.connector as connector

datab=connector.connect(host="localhost",user="root",passwd="",database="student",port="3306")

print("connection astablised..........")
sid=int(input("enter your student id:"))
sname=input("enter your name:")
scity=input("enter your city:")
smobileno=int(input("enter your mobileno:"))
mycursor=datab.cursor()

sql="update  studentdetail set sname=%s, scity=%s,smobileno=%s WHERE sid=%s" 

values=[sname,scity,smobileno,sid]

mycursor.execute(sql,values)

datab.commit()

print("no of rows are updated.....",mycursor.rowcount)