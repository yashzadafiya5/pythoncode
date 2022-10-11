# import mysql.connector as co 

# db=co.connect(host="localhost",user="root",passwd="",database="company ",port=3306)

# print("connection establised........")

# mycursor=db.cursor(dictionary=True)

# sql='''select c.customerNumber,customerName,city,country,amount,checkNumber,paymentDate from payments p left join customers c on c.customerNumber=p.customerNumber where c.customerNumber is NULL
# '''

# mycursor.execute(sql)

# table=mycursor.fetchone()
# print(table)

