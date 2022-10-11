import mysql.connector as con 

db=con.connect(host="localhost",user="root",passwd="",database="",port="3306")

print("connection astablised...........")

mycursor=db.cursor()

sql="create database billmanagment"

mycursor.execute(sql)

db.commit()

print("create database complited.......")
