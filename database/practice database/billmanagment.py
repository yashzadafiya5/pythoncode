import mysql.connector as con 

db=con.connect(host="localhost",user="root",passwd="",database="billmanagment",port="3306")

print("connection astablised...........")

mycursor=db.cursor()

sql='''create table billform(comp varchar(64) ,address varchar,nammdit varchar(64),address1dit varchar,gstindit varchar(64),pandit varchar(64),statedit varchar(64) ,invoice int ,invoicedate datetime,challanno int,vehicalno varchar(64) '''

mycursor.execute(sql)

db.commit()

print("create table complited.......")

