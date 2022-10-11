import mysql.connector as con 

datab=con.connect(host="localhost",user="root",passwd="",database="students",port="3306")

mycursor=datab.cursor(dictionary=True)

sql="select * from studentdetail"

mycursor.execute(sql)

table=mycursor.fetchall()
print(f" {'sid':2} {'sname':67} {'smobileno':20}{'sweight':9}{'sgender':6}")

for i in table:
    msg=(f"{i['sid']:4} {i['sname']:14}{i['smobileno']:64} {i['sweight']:14} {i['sgender']:6}")
    print(msg)