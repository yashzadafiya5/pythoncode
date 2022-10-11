#billing application
from datetime import datetime
import time
import projectv1modules as pm
db=pm.DBOperation(" billmanagments ")
mainmodulechoice=0
def displaybill():
    sql="select*from product where isdeleted=%s order by id"
    values=[0]
    table=db.FetchRow(sql,values)
    print('-'*120)
    print(f"'id'{'':12}{'name':40}{'detail':35}{'price':11}{'stock':11}")
    print('-'*120)
    for row in table:
        print(f"{row['id']}{'':12}{row['name']:40}{row['detail']:32}{row['price']:11}{row['stock']:11}")
        print('-'*120)
def Displayunbilled():
    sql=" select b.id,name,detail,b.price,quantity  from  product p, bill_product b where productid=p.id and billid=%s"
    values=[0]
    print('='*85)
    print(f"id{'':12}{'name':25}{'detail':25}{'quantity':11}{'price':11}")
    grandtotal=0
    table=db.FetchRow(sql,values)
    for i in table:
        print('-'*85)
        print(f"{i['id']}{'':12}{i['name']:25}{i['detail']:20}{i['quantity']:11}{i['price']:11}")
        grandtotal=grandtotal+(i['quantity']*i['price'])
    print('='*85)
    print(f"GRANDTOTAL={grandtotal:70}")     
while True:
    print(" press 1 for product managment ")
    print(" press 2 for bill managment ")
    print("press 0 for exit ")

    mainmodulechoice=int(input("enter your choice:="))

    if mainmodulechoice==1:
        while True:
            print("="*100)
            print(" press 1 for add new product  ")
            print("-"*100)
            print(" press 2 for delete existing product ")
            print("-"*100)
            print(" press 3 for edit product ")
            print("-"*100)
            print(" press 4 for view product ")
            print("-"*100)
            print("press 0 for exit product module ")
            print("-"*100)
            productmanagment=int(input("enter your choice :="))
            time.sleep(2)
            if productmanagment==1:
                #this field is use for insert detail 
                name=input("enter a productname:")
                detail=input("enter a productdetail:")
                price=int(input("enter a productprice:"))
                stock=int(input("enter a stock:"))
                sql="insert into product (name,detail,price,stock) values(%s,%s,%s,%s)"
                values=[name,detail,price,stock]
                db.RunQuery(sql,values)
            elif productmanagment==2:
                displaybill()
                id=int(input("enter a product id you delet"))
                sql="update product set isdeleted=%s where id=%s"
                values=[1,id]
                db.RunQuery(sql,values)
            elif productmanagment==3:
                #this field is use for update detail 
                displaybill()
                name=input("enter a productname:")
                detail=input("enter a productdetail:")
                price=int(input("enter a productprice:"))
                stock=int(input("enter a stock:"))
                id=int(input("enter a id:"))
                sql="update product set name=%s,detail=%s,price=%s,stock=%s where id=%s"
                values=[name,detail,price,stock,id]
                db.RunQuery(sql,values)
            elif productmanagment==4:
                displaybill()
            elif productmanagment==0:
                print("good byy....")
                break
            else:
                print("invalid input")
    elif mainmodulechoice==2:
        while True:
            print("="*100)
            print(" press 1 add product into bill")
            print("-"*100)
            print(" press 2 delete product from bill")
            print("-"*100)
            print(" press 3 view bill items")
            print("-"*100)
            print(" press 4 save and print bill")
            print("-"*100)
            print(" press 5 get details of bill between given date")
            print("-"*100)
            print(" press 6 search for specific bill by name")
            print("-"*100)
            print("press 0 for exit bill module ")
            print("-"*100)
            billmangement=int(input("enter your choice :="))
            time.sleep(2)
            if billmangement==1:
                displaybill()
                productid=int(input("enter a productid:"))
                quantity=int(input("units of a products:"))
                sql="select price from product where id=%s"
                values=[productid]
                table=db.FetchRow(sql,values)
                if len(table)>0:
                    price=table[0]['price']
                    sql="insert into bill_product(productid,price,quantity)values(%s,%s,%s)"
                    values=[productid,price,quantity]
                    db.RunQuery(sql,values)
                    print("no of row are inserted.....")
            elif billmangement==2:
                Displayunbilled()
                productid=int(input("enter what you want to delete"))
                sql="delete from bill_product where id=%s"
                values=[productid]
                db.RunQuery(sql,values)
            elif billmangement==3:
                Displayunbilled()   
            elif billmangement==4:
                sql = "select sum(price*quantity) 'GrandTotal' from bill_product where billid=%s"
                values = [0]
                table = db.FetchRow(sql,values)
                GrandTotal = table[0]['GrandTotal']
                if GrandTotal!=None:
                    #insert row into bill table
                    customername = input("Enter customer name")
                    email = input("Enter email")
                    isCash = int(input("press 1 for cash or press 2 for credit bill"))
                    sql = "insert into bill (customername,amount,iscash,email) values (%s,%s,%s,%s)"
                    values = [customername,GrandTotal,isCash,email]
                    db.RunQuery(sql,values)
                    
                    #update bill_product
                    sql = "select max(id) 'billid' from bill"
                    table = db.FetchRow(sql)
                    billid = table[0]['billid']
                    
                    sql = "update bill_product set billid=%s where billid=%s"
                    values = [billid,0]
                    db.RunQuery(sql,values)
                    print("Bill generated......")
                else:
                    print("No unbill items ")
            elif billmangement==5:
                print("Enter start date and time")
                day = int(input("Enter start day"))
                month = int(input("Enter start month"))
                year = int(input("Enter start year"))
                start_date_time = datetime(year,month,day)
                print("Enter end date and time")
                day = int(input("Enter start day"))
                month = int(input("Enter start month"))
                year = int(input("Enter start year"))
                end_date_time = datetime(year,month,day)
                sql="select * from bill where billdate>=%s and billdate<=%s "
                values=[start_date_time,end_date_time]
                table=db.FetchRow(sql,values)
                print('-'*120)
                print(f"'id'{'':8}{'title ':15}{'fees':10}{'duration':12}{'description':11}")
                print('-'*120)
                for row in table:
                    print(f"{row['id']}{'':10}{row['title']:10}{'':5}{row['fees']:5}{row['duration']:10}{'':7}{row['description']:25}")
                    print('-'*120)
                print(table)
            elif billmangement==6:
                customername=input("enter a name:")
                sql="select * from bill where customername=%s"
                values=[customername]
                table=db.FetchRow(sql,values)
                print(table)
            elif billmangement==0:
                print("for exit bill module")
                break
            else:
                print("invalid input")
    elif mainmodulechoice==0:
        print("thanks for coming")
        break
    else:
        print("thanks for coming this filed....")

