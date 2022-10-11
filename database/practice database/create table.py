import mysql.connector as con 

db=con.connect(host="localhost",user="root",passwd="",database="cochingclass",port="3306")

print("connection astablised...........")

mycursor=db.cursor()

sql='''create table lecture(id int primary key AUTO_INCREMENT,teacherid int ,subjectid int,batchid int,
duration varchar(64),amount float(4)'''

mycursor.execute(sql)

db.commit()

print("create table complited.......")

