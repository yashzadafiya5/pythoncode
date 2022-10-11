from datetime import datetime
from datetime import time
import projectv1modules as pm

db=pm.DBOperation("cochingclass")

def displaycourse():
    sql="select*from course  where isdeleted=%s order by id"
    values=[0]
    table=db.FetchRow(sql,values)
    print('-'*120)
    print(f"'id'{'':8}{'title ':15}{'fees':10}{'duration':12}{'description':11}")
    print('-'*120)
    for row in table:
        print(f"{row['id']}{'':10}{row['title']:10}{'':5}{row['fees']:5}{row['duration']:10}{'':7}{row['description']:25}")
        print('-'*120)
displaycourse()
def displaybatch():
    sql="select * from batch where isdeleted=%s"
    values=[0]
    table=db.FetchRow(sql,values)
    print('-'*120)
    print(f"'id'{'':13}{'courseid ':12}{'':4}{'startdate':12}{'':6}{'enddate':16}{'classtime':11}")
    print('-'*120)
    for row in table:
        startdate = row['startdate'].strftime("%d-%m-%Y")
        enddate = row['enddate'].strftime("%d-%m-%Y")
        # classtime=row['classtime']("%H:%M:%S")
        print(f"{row['id']}{'':10}{row['courseid']:10}{'':5}{'':7}{startdate}{'':7}{enddate}{'':7}{row['classtime']}")
        print('-'*120)
displaybatch()

def displaysubject():
        sql="select*from subject where isdeleted=%s order by id"
        values=[0]
        table=db.FetchRow(sql,values)
        print('-'*120)
        print(f"id'{'':4}{'courseid ':13}{'title':20}{'rate':22}")
        print('-'*120)
        for row in table:
            print(f"{row['id']}{row['courseid']:10}{'':8}{row['title']:5}{'':5}{row['rate']:10}")
            print('-'*120)
displaysubject()
def displaytecher():
    sql="select*from teacher  where isdeleted=%s order by id"
    values=[0]
    table=db.FetchRow(sql,values)
    print('-'*120)
    print(f''''id'{'':8}{'name ':10}{'mobile':20}{'email':22}{'gender':11}{'qulification':11}{'':5}{'experience':11}''')
    print('-'*120)
    for row in table:
        print(f'''{row['id']}{'':10}{row['name']:10}{row['mobile']:5}{'':5}{row['email']:10}{row['gender']:10}{'':8}{row['qulification']:10}{'':10}{row['experience']}''')
        print('-'*120)
displaytecher()
def displaylecture():
    sql="select * from lecture "
    table=db.FetchRow(sql)
    print('-'*120)
    print(f''''id'{'':2}{'teacherid ':12}{'':2}{'subjectid':10}{'':5}{'lecturedate':11}{'':7}{'batchid':11}{'amount':11}{'duration':12}''')
    print('-'*120)
    for row in table:
        lecturedate = row['lecturedate'].strftime("%d-%m-%Y")
        print(f'''{row['id']}{row['teacherid']:10}{'':5}{row['subjectid']:8}{'':11}{lecturedate}{row['batchid']:12}{row['amount']:12}{'':8}{row['duration']:3}{'':6}''')
        print('-'*120)
displaylecture()

