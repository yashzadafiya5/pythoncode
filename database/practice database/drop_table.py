import mysql.connector as con 

mydatabase=con.connect(host="localhost",user='root',passwd="",database="",port="3306")

print("connection astablised.........")

tables={}

mycursor=mydatabase.cursor()


sql="drop database student "

mycursor.execute(sql)

mydatabase.commit()

print("no of colums add....")