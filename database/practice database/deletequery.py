import mysql.connector as con 

db=con.connect(host="localhost",user="root",passwd="",database="student",port="3306")

print("connection astablised...........")

sid=int(input("enter a student id:"))
mycursor=db.cursor()

sql="delete from studentdetail where sid=%s"
values=[sid]

mycursor.execute(sql,values)

db.commit()

print("deleted.....",mycursor.rowcount)