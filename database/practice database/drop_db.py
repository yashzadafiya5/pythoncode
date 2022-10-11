import mysql.connector as con 

mydatabase=con.connect(host="localhost",user='root',passwd="",database="student ",port="3306")

print("connection astablised.........")

tables={}

mycursor=mydatabase.cursor()


sql="alter table studentdetail drop column yash  "

mycursor.execute(sql)

mydatabase.commit()

print("no of colums add....")