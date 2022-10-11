from datetime import datetime
from datetime import time


import projectv1modules as pm

db=pm.DBOperation('cochingclass')

# generate batch wise lecture detail between given date
# generate of specific teacher between given date


# print("Enter lecturedate date and time")
# day = int(input("Enter start day"))
# month = int(input("Enter start month"))
# year = int(input("Enter start year"))
# lecturedate = datetime(year,month,day)
# sql="select teacherid,subjectid from lecture where teacherid=%s"
# values=[1]
# table=db.FetchRow(sql,values)
# for row in table:
# #         print(row)
# sql="select * from lecture l,batch b  where batchid=b.id and lecturedate=%s"
# values=[lecturedate]

# table=db.FetchRow(sql,values)
# print(f''''id'{'':2}{'teacherid ':12}{'':2}{'subjectid':10}{'':5}{'batchid':10}{'duration':12}{'amount':11}{'lecturedate':11}''')
# for row in table:
#     for row in table:
#         lecturedate = row['lecturedate'].strftime("%d-%m-%Y")
#         print(f'''{row['id']}{'':10}{row['teacherid']:10}{'':5}{row['subjectid']:8}{'':3}{row['batchid']:12}{'':8}{row['duration']:3}{row['amount']:12}{'':6}{lecturedate}''')
#         print('-'*120)


# def displaylecture():
#     sql="select * from lecture "
#     table=db.FetchRow(sql)
#     print('-'*120)
#     print(f''''id'{'':2}{'teacherid ':12}{'':2}{'subjectid':10}{'':5}{'batchid':10}{'duration':12}{'amount':11}{'lecturedate':11}''')
#     print('-'*120)
#     for row in table:
#         lecturedate = row['lecturedate'].strftime("%d-%m-%Y")
#         print(f'''{row['id']}{'':10}{row['teacherid']:10}{'':5}{row['subjectid']}{'':7}{row['batchid']}{'':7}{row['duration']}{row['amount']}{lecturedate}''')
#         print('-'*120)
# displaylecture()
        
# def displaybatch():
#     sql="select * from batch where isdeleted=%s"
#     values=[0]
#     table=db.FetchRow(sql,values)
#     print('-'*120)
#     print(f"'id'{'':13}{'courseid ':12}{'':4}{'startdate':12}{'':6}{'enddate':16}{'classtime':11}")
#     print('-'*120)
#     for row in table:
#         startdate = row['startdate'].strftime("%d-%m-%Y")
#         enddate = row['enddate'].strftime("%d-%m-%Y")
#         classtime=row['classtime'].strftime("%H:%M:%S")
#         print(f"{row['id']}{'':10}{row['courseid']:10}{'':5}{'':7}{startdate}{'':7}{enddate}{'':7}{classtime}")
#         print('-'*120)
# displaybatch()
# def displaytecher():
#     sql="select*from teacher  where isdeleted=%s order by id"
#     values=[0]
#     table=db.FetchRow(sql,values)
#     print('-'*120)
#     print(f''''id'{'':8}{'name ':10}{'mobile':20}{'email':22}{'gender':11}{'qulification':11}{'':5}{'experience':11}''')
#     print('-'*120)
#     for row in table:
#         print(f'''{row['id']}{'':10}{row['name']:10}{row['mobile']:5}{'':5}{row['email']:10}{row['gender']:10}{'':5}{row['qulification']:10}{row['experience']}''')
#         print('-'*120)
# displaytecher()
# def displaysubject():
#         sql="select*from subject where isdeleted=%s order by id"
#         values=[0]
#         table=db.FetchRow(sql,values)
#         print('-'*120)
#         print(f"id'{'':4}{'courseid ':13}{'title':20}{'rate':22}")
#         print('-'*120)
#         for row in table:
#             print(f"{row['id']}{row['courseid']:10}{'':8}{row['title']:5}{'':5}{row['rate']:10}")
#             print('-'*120)
# displaysubject()
# def displaybatch():
#     sql="select startdate,enddate from batch where isdeleted=%s"
#     values=[0]
#     table=db.FetchRow(sql,values)
#     for row in table:
#         print(f"{row['startdate']}{row['enddate']}")

# print("Enter start date and time")
# day = int(input("Enter start day"))
# month = int(input("Enter start month"))
# year = int(input("Enter start year"))
# start_date_time = datetime(year,month,day)
# print("Enter end date and time")
# day = int(input("Enter start day"))
# month = int(input("Enter start month"))
# year = int(input("Enter start year"))
# end_date_time = datetime(year,month,day)

# sql="select * from bill where billdate>=%s and billdate<=%s  "
# values=[start_date_time,end_date_time]
# table=db.FetchRow(sql,values)
# print(table)


# # course management(insert,update,delete,select)

# title=input("enter a title:")
# fees=int(input("enter a fees"))
# duration=int(input("enter duration in days:"))
# description=input("enter a discription for course:")
# sql="insert into course(title,fees,duration,description)values(%s,%s,%s,%s)"
# values=[title,fees,duration,description]
# db.RunQuery(sql,values)
# "-------------------------------------------------------------------------------------------------------------------------"
# # #batch (id,courseid,startdate,enddate,classtime)

# courseid=int(input("enter a courseid"))
# print("Enter a Start Date")
# startday=int(input("enter a start day"))
# startmonth=int(input("enter a start month"))
# startyear=int(input("enter a start year"))
# startdate=datetime(startyear,startmonth,startday)
# print("Enter a end Date")
# endday=int(input("enter a end day"))
# endmonth=int(input("enter a end month"))
# endyear=int(input("enter a end year"))
# enddate=datetime(endyear,endmonth,endday)
# classtime=()
# sql="insert into batch(courseid,)values(%s,%s,%s,%s)"
# values=[courseid,fees,duration,description]
# db.RunQuery(sql,values)

# #subject (id,courseid,title,rate)


# def insertbatch():
#         courseid=int(input("enter a courseid"))
#         print("Enter start date and time")
#         day = int(input("Enter start day"))
#         month = int(input("Enter start month"))
#         year = int(input("Enter start year"))
#         startdate = datetime(year,month,day)
#         print("Enter end date and time")
#         day = int(input("Enter start day"))
#         month = int(input("Enter start month"))
#         year = int(input("Enter start year"))
#         enddate = datetime(year,month,day)
#         Hour=int(input("enter a hour"))
#         Minute=int(input("enter a minute"))
#         Second=int(input("enter a second"))
#         classtime=time(Hour,Minute,Second)
#         sql="insert into batch(courseid,startdate,enddate,classtime)values(%s,%s,%s,%s)"
#         values=[courseid,startdate,enddate,classtime]
#         db.RunQuery(sql,values)
# insertbatch()

# sql="select * from bill where billdate between '2004-01-01' and '2022-12-31'  "

# table=db.FetchRow(sql)
# generate batch wise lecture detail with total amount

# sql="select sum(amount) 'total'from lecture"
# table=db.FetchRow(sql)

# batch = table[0]['total']
   #run insert query 
# sql="select * from batch b,lecture l where batchid=b.id  "  
           
# #    values = [productid,quantity,price]
# table=db.FetchRow(sql)

# for row in table:
#         print(row)

# generate batch wise lecture detail between given date
# print("Enter start date and time")
# day = int(input("Enter start day"))
# month = int(input("Enter start month"))
# year = int(input("Enter start year"))
# startdate = datetime(year,month,day)
# print("Enter end date and time")
# day = int(input("Enter end day"))
# month = int(input("Enter end month"))
# year = int(input("Enter end year"))
# enddate = datetime(year,month,day)

# sql='''select name from batch b,lecture l where batchid=b.id and startdate=%s,enddate=%s '''
# values=[startdate,enddate]
# table=db.FetchRow(sql,values)
# for row in table:
#         print(row)
# '''sql="select courseid from batch where startdate='2002-01-01 00:00:00' and enddate='2002-04-02 00:00:00'  "
# table=db.FetchRow(sql)
# for row in table:
#         print(row)'''
#     print(f"{row['startdate']}{row['enddate']}")
# print(f''''id'{'':2}{'teacherid ':12}{'':2}{'subjectid':10}{'':5}{'batchid':10}{'duration':12}{'amount':11}{'lecturedate':11}''')
# for row in table:
#     for row in table:
#         lecturedate = row['lecturedate'].strftime("%d-%m-%Y")
#         print(f'''{row['id']}{'':10}{row['teacherid']:10}{'':5}{row['subjectid']:8}{'':3}{row['batchid']:12}{'':8}{row['duration']:3}{row['amount']:12}{'':6}{lecturedate}''')
#         print('-'*120)

# print("Enter start date and time")
# day = int(input("Enter start day"))
# month = int(input("Enter start month"))
# year = int(input("Enter start year"))
# startdate = datetime(year,month,day)
# print("Enter end date and time")
# day = int(input("Enter end day"))
# month = int(input("Enter end month"))
# year = int(input("Enter end year"))
# enddate = datetime(year,month,day)
# sql='''select l.id,teacherid,subjectid,batchid,duration,amount,lecturedate from lecture l,batch b where batchid=b.id and startdate=%s and enddate=%s  '''
# values=[startdate,enddate]
# table=db.FetchRow(sql,values)
# print(f''' 'id'{'':2}{'teacherid ':12}{'':2}{'subjectid':10}{'':5}{'batchid':10}{'duration':12}{'amount':11}{'lecturedate':11}''')
# for row in table:
#     lecturedate = row['lecturedate'].strftime("%d-%m-%Y")
#     print(f'''{row['id']}{row['teacherid']:10}{'':5}{row['subjectid']:8}{row['batchid']:12}{row['duration']:3}{row['amount']:12}{lecturedate}''')
        
# sql='''select l.id,teacherid,subjectid,batchid,duration,amount,lecturedate from lecture l,batch b where batchid=b.id  '''
# table=db.FetchRow(sql)
# for row in table:
#         print(row)
# def displaycourse():
#     sql="select*from course  where isdeleted=%s order by id"
#     values=[0]
#     table=db.FetchRow(sql,values)
#     print('-'*120)
#     print(f"'id'{'':8}{'title ':15}{'fees':10}{'duration':12}{'description':11}")
#     print('-'*120)
#     for row in table:
#         print(f"{row['id']}{'':10}{row['title']:10}{'':5}{row['fees']:5}{row['duration']:10}{'':7}{row['description']:25}")
#         print('-'*120)
# displaycourse()
# def displaybatch():
#     sql="select * from batch where isdeleted=%s"
#     values=[0]
#     table=db.FetchRow(sql,values)
#     print('-'*120)
#     print(f"'id'{'':13}{'courseid ':12}{'':4}{'startdate':12}{'':6}{'enddate':16}{'classtime':11}")
#     print('-'*120)
#     for row in table:
#         startdate = row['startdate'].strftime("%d-%m-%Y")
#         enddate = row['enddate'].strftime("%d-%m-%Y")
#         classtime=row['classtime'].strftime("%H:%M:%S")
#         print(f"{row['id']}{'':10}{row['courseid']:10}{'':5}{'':7}{startdate}{'':7}{enddate}{'':7}{classtime}")
#         print('-'*120)
# displaybatch()
# print("Enter start date and time")
# day = int(input("Enter start day"))
# month = int(input("Enter start month"))
# year = int(input("Enter start year"))
# lecturedate = datetime(year,month,day)
# sql='''select name from teacher t,lecture l where teacherid=t.id and lecturedate=%s'''
# values=[lecturedate]
# table=db.FetchRow(sql,values)
# for row in table:
#     print(row)
# print("Enter start date and time")
# day = int(input("Enter start day"))
# month = int(input("Enter start month"))
# year = int(input("Enter start year"))
# lecturedate = datetime(year,month,day)
# sql='''select t.id,name from teacher t,lecture l where teacherid=t.id and lecturedate=%s'''
# values=[lecturedate]
# table=db.FetchRow(sql,values)
# print(f''''id' {'':3}{'name'}''')
# for row in table:
#         print(f"{'':1}{row['id']}{'':6}{row['name']}")
# def displaybatchdetail():
#      print("Enter start date and time")
#      day = int(input("Enter start day"))
#      month = int(input("Enter start month"))
#      year = int(input("Enter start year"))
#      startdate = datetime(year,month,day)
#      print("Enter end date and time")
#      day = int(input("Enter end day"))   
#      month = int(input("Enter end month"))
#      year = int(input("Enter end year"))
#      enddate = datetime(year,month,day)
#      sql='''select l.id,teacherid,subjectid,batchid,duration,amount,lecturedate from lecture l,batch b where batchid=b.id     and startdate='2002-01-01 00:00:00' and enddate='2002-04-02 00:00:00'  '''
#      values=[startdate,enddate]
#      table=db.FetchRow(sql)
#      print(f''' 'id'{'':2}{'teacherid ':12}{'':1}{'subjectid':10}{'':3}{'lecturedate':11}{'':6}{'batchid':11}{'amount':10}{'duration':12}''')
#      for row in table:
#         lecturedate = row['lecturedate'].strftime("%d-%m-%Y")
#         print(f'''{row['id']}{row['teacherid']:10}{'':6}{row['subjectid']:8}{'':8}{lecturedate:2}{'':10}{row['batchid']}{row['amount']:12}{'':8}{row['duration']:3}''')
# displaybatchdetail()
# def displaylecture():
#     sql="select * from lecture "
#     table=db.FetchRow(sql)
#     print('-'*120)
#     print(f''''id'{'':2}{'teacherid ':12}{'':2}{'subjectid':10}{'':5}{'lecturedate':11}{'':7}{'batchid':11}{'amount':11}{'duration':12}''')
#     print('-'*120)
#     for row in table:
#         lecturedate = row['lecturedate'].strftime("%d-%m-%Y")
#         print(f'''{row['id']}{row['teacherid']:10}{'':5}{row['subjectid']:8}{'':11}{lecturedate}{row['batchid']:12}{row['amount']:12}{'':8}{row['duration']:3}{'':6}''')
#         print('-'*120)
# displaylecture()
# def displaytecher():
#     sql="select*from teacher  where isdeleted=%s order by id"
#     values=[0]
#     table=db.FetchRow(sql,values)
#     print('-'*120)
#     print(f''''id'{'':8}{'name ':10}{'mobile':20}{'email':22}{'gender':11}{'qulification':11}{'':5}{'experience':11}''')
#     print('-'*120)
#     for row in table:
#         print(f'''{row['id']}{'':10}{row['name']:10}{row['mobile']:5}{'':5}{row['email']:10}{row['gender']:10}{'':8}{row['qulification']:10}{'':10}{row['experience']}''')
#         print('-'*120)
# displaytecher()
# def displaysubject():
#         sql="select*from subject where isdeleted=%s order by id"
#         values=[0]
#         table=db.FetchRow(sql,values)
#         print('-'*120)
#         print(f"id'{'':4}{'courseid ':13}{'title':20}{'rate':22}")
#         print('-'*120)
#         for row in table:
#             print(f"{row['id']}{row['courseid']:10}{'':8}{row['title']:5}{'':5}{row['rate']:10}")
#             print('-'*120)
# displaysubject()
# def displaybatch():
#     sql="select * from batch where isdeleted=%s"
#     values=[0]
#     table=db.FetchRow(sql,values)
#     print('-'*120)
#     print(f"'id'{'':13}{'courseid ':12}{'':4}{'startdate':12}{'':6}{'enddate':16}{'classtime':11}")
#     print('-'*120)
#     for row in table:
#         startdate = row['startdate'].strftime("%d-%m-%Y")
#         enddate = row['enddate'].strftime("%d-%m-%Y")
#         classtime=row['classtime'].strftime("%H:%M:%S")
#         print(f"{row['id']}{'':10}{row['courseid']:10}{'':5}{'':7}{startdate}{'':7}{enddate}{'':7}{classtime}")
#         print('-'*120)
# displaybatch()
# def displaycourse():
#     sql="select*from course  where isdeleted=%s order by id"
#     values=[0]
#     table=db.FetchRow(sql,values)
#     print('-'*120)
#     print(f"'id'{'':8}{'title ':15}{'fees':10}{'duration':12}{'description':11}")
#     print('-'*120)
#     for row in table:
#         print(f"{row['id']}{'':10}{row['title']:10}{'':5}{row['fees']:5}{row['duration']:10}{'':7}{row['description']:25}")
#         print('-'*120)
# displaycourse()
# generate batch wise lecture detail with total amount

# sql="select l.id,teacherid,subjectid,batchid,duration,amount,lecturedate from batch b,lecture l where batchid=b.id "
# table=db.FetchRow(sql)
# amount=0
# print(f''' 'id'{'':4}{'teacherid ':12}{'':1}{'subjectid':10}{'':3}{'lecturedate':11}{'':6}{'batchid':11}{'amount':10}{'duration':12}''')
# for row in table:
#         print('-'*100)
#         lecturedate = row['lecturedate'].strftime("%d-%m-%Y")
#         print(f'''{'':2}{row['id']}{row['teacherid']:10}{'':6}{row['subjectid']:8}{'':8}{lecturedate:2}{'':10}{row['batchid']}{row['amount']:12}{'':8}{row['duration']:3}''')
#         amount= row['amount']+amount
#         print('-'*100)
# print('-'*100)
# print(f"Totalamount = {amount:54}")
# vi.displaylecture()
# print("Enter start date and time")
# day = int(input("Enter start day"))
# month = int(input("Enter start month"))
# year = int(input("Enter start year"))
# lecturestartdate = datetime(year,month,day)
# print("Enter end date and time")
# day = int(input("Enter end day"))   
# month = int(input("Enter end month"))
# year = int(input("Enter end year"))
# lectureenddate = datetime(year,month,day)
# sql='''select t.id,name from teacher t,lecture l where teacherid=t.id and lecturedate>=%s and lecturedate<=%s and isdeleted=%s'''
# values=[lecturestartdate,lectureenddate,0]
# table=db.FetchRow(sql,values)
# print(f''''id' {'':3}{'name'}''')
# for row in table:
#     print(f"{'':1}{row['id']}{'':6}{row['name']}")
id = int(input("Enter batch id to update batch: "))
courseid = int(input("Enter courseid: "))
startdate = input("Enter statrdate of batch in format %Y-%m-%d: ")
enddate = input("Enter enddate of batch in format %Y-%m-%d: ")
print("Enter classtime of batch")
hour = int(input("Enter hour"))
minute = int(input("Enter minute"))
second = int(input("Enter seconds"))
classtime = time(hour,minute,second)
sql = "update batch set courseid=%s,startdate=%s,enddate=%s,classtime=%s where id=%s"
values = [id,courseid,startdate,enddate,classtime]
db.RunQuery(sql,values)
print("-"*100)