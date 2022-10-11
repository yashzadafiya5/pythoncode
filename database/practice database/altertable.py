import mysql.connector as con 

mydatabase=con.connect(host="localhost",user='root',passwd="",database="student ",port="3306")

print("connection astablised.........")


mycursor=mydatabase.cursor()

sql="alter table studentdetail  add  email varchar(125) "

mycursor.execute(sql)

mydatabase.commit()

print("no of colums add....")