import projectv1modules as pm
from datetime import datetime
from datetime import time 
from datetime import time as ti
import viewdata as vi
import time
db=pm.DBOperation("cochingclass")

while True:
    print("="*139)
    print("                         ***************************Coaching class management system***************************")
    print("="*139)
    print("-"*100)
    print(" press 1 for course management")
    print("-"*100)
    print(" press 2 for batch management")
    print("-"*100)
    print(" press 3 for subject management")
    print("-"*100)
    print(" press 4 for teacher management")
    print("-"*100)
    print(" press 5 for lecture management")
    print("-"*100)
    print(" press 6 for generate of specific teacher between given date:")
    print("-"*100)
    print(" press 7 for generate batch wise lecture detail with total amount:")
    print("-"*100)
    print(" press 8 for generate batch wise lecture detail between given date :")
    print("-"*100)
    print("press 0 for exit Coaching class management system ")
    print("-"*100)
    Coachingclass=int(input("enter your choice:="))
    time.sleep(1)
    if   Coachingclass==1:
        while True:
            print("*******you enter a course table*******")
            print("-"*100)
            print(" press 1 insert course")
            print("-"*100)
            print(" press 2 update course")
            print("-"*100)
            print(" press 3 delete course")
            print("-"*100)
            print(" press 4 select course")
            print("-"*100)
            print(" press 0 exit course table")
            print("-"*100)
            course=int(input("enter your choice:="))
            if course==1:
                #this field is use for insert Data 
                title=input("enter a title:")
                fees=int(input("enter a fees"))
                duration=int(input("enter duration in days:"))
                description=input("enter a discription for course:")
                sql="insert into course(title,fees,duration,description)values(%s,%s,%s,%s)"
                values=[title,fees,duration,description]
                db.RunQuery(sql,values)
            elif course==2:
                #this field is use for update detail 
                vi.displaycourse()
                id=int(input("enter id whose data you update "))
                title=input("enter a title:")
                fees=int(input("enter a fees"))
                duration=int(input("enter duration in days:"))
                description=input("enter a discription for course:")
                sql="update course set title=%s,fees=%s,duration=%s,description=%s where id=%s"
                values=[title,fees,duration,description,id]
                db.RunQuery(sql,values)
            elif course==3:
                vi.displaycourse()
                id=int(input("enter id you delete course:= "))
                sql="update course set isdeleted=%s where id=%s"
                values=[1,id]
                db.RunQuery(sql,values)
            elif course==4:
                #this field is use for view table 
                vi.displaycourse()
            elif course==0:
                print("exit course table")
                break
            else:
                print("invalid input")
    elif Coachingclass==2:
        while True:
            print("*******you enter a batch table*******")
            print("-"*100)
            print(" press 1 insert batch")
            print("-"*100)
            print(" press 2 update batch")
            print("-"*100)
            print(" press 3 delete batch")
            print("-"*100)
            print(" press 4 select batch")
            print("-"*100)
            print(" press 0 exit batch table")
            print("-"*100)
            batch=int(input("enter your choice:="))
            if batch==1:
                #batch (id,courseid,startdate,enddate,classtime)
                vi.displaycourse()
                courseid=int(input("enter a courseid"))
                print("Enter start date and time")
                day = int(input("Enter start day"))
                month = int(input("Enter start month"))
                year = int(input("Enter start year"))
                startdate = datetime(year,month,day)
                print("Enter end date and time")
                day = int(input("Enter start day"))
                month = int(input("Enter start month"))
                year = int(input("Enter start year"))
                enddate = datetime(year,month,day)
                Hour=int(input("enter a hour"))
                Minute=int(input("enter a minute"))
                Second=int(input("enter a second"))
                classtime=ti(Hour,Minute,Second)
                sql="insert into batch(courseid,startdate,enddate,classtime)values(%s,%s,%s,%s)"
                values=[courseid,startdate,enddate,classtime]
                db.RunQuery(sql,values)
            elif batch==2:
                vi.displaybatch()
                id=int(input("enter a id whose data you update:="))
                courseid=int(input("enter a courseid"))
                print("Enter start date and time")
                day = int(input("Enter start day"))
                month = int(input("Enter start month"))
                year = int(input("Enter start year"))
                startdate = datetime(year,month,day)
                print("Enter end date and time")
                day = int(input("Enter start day"))
                month = int(input("Enter start month"))
                year = int(input("Enter start year"))
                enddate = datetime(year,month,day)
                Hour=int(input("enter a hour"))
                Minute=int(input("enter a minute"))
                Second=int(input("enter a second"))
                classtime=ti(Hour,Minute,Second)
                sql="update batch set courseid=%s,startdate=%s,enddate=%s,classtime=%s where id=%s"
                values=[courseid,startdate,enddate,classtime,id]
                db.RunQuery(sql,values)
            elif batch==3:
                vi.displaybatch()
                id=int(input("enter id you delete batch:= "))
                sql="update batch set isdeleted=%s where id=%s"
                values=[1,id]
                db.RunQuery(sql,values)
            elif batch==4:
                vi.displaybatch()
            elif batch==0:
                print("exit course table")
                break
            else:
                print("invalid input")
    elif Coachingclass==3:
        while True:
            print("*******you enter a subject table*******")
            print("-"*100)
            print(" press 1 insert subject")
            print("-"*100)
            print(" press 2 update subject")
            print("-"*100)
            print(" press 3 delete subject")
            print("-"*100)
            print(" press 4 select subject")
            print("-"*100)
            print(" press 0 exit subject table")
            print("-"*100)
            subject=int(input("enter your choice:="))
            if subject==1:
                id=int(input("enter a id"))
                title=input("enter a title:")
                rate=int(input("enter a rate per subject"))
                sql="select courseid from batch where id=%s"
                values=[id]
                table=db.FetchRow(sql,values)
                for row in table:
                    print(row)
                if len(table)>0:
                    courseid=table[0]['courseid']
                    #this field is use for insert Data 
                    sql="insert into subject(courseid,title,rate)values(%s,%s,%s)"
                    values=[courseid,title,rate]
                    db.RunQuery(sql,values)
            elif subject==2:
                vi.displaysubject()
                id=int(input("enter id"))
                title=input("enter a title:")
                rate=int(input("enter a rate"))
                sql="update subject set title=%s,rate=%s where id=%s"
                values=[title,rate,id]
                db.RunQuery(sql,values)
            elif subject==3:
                vi.displaysubject()
                id=int(input("enter id you delete subject:= "))
                sql="update subject set isdeleted=%s where id=%s"
                values=[1,id]
                db.RunQuery(sql,values)
            elif subject==4:
                #this field is use for view table 
                vi.displaysubject()
            elif subject==0:
                print("exit course table")
                break
            else:
                print("invalid input")
    elif Coachingclass==4:
        while True:
            print("*******you enter a teacher table*******")
            print("-"*100)
            print(" press 1 insert teacher")
            print("-"*100)
            print(" press 2 update teacher")
            print("-"*100)
            print(" press 3 delete teacher")
            print("-"*100)
            print(" press 4  select teacher")
            print("-"*100)
            print(" press 0 exit teacher table")
            print("-"*100)
            techertable=int(input("input enter your choice:="))
            if techertable==1:
                name=input("enter techer name:=")
                mobile=int(input("enter teacher mobileno:="))
                email=(input("enter teacher email"))
                gender=int(input("if teacher is male press'0' and female for press '1':="))
                qulification=(input("press your qulification ex:m.c.a,b.c.a :="))
                print('-'*120)
                print("press '1' for a experience in days and '2' for months and '3' for years:=")
                print('-'*120)
                experience=int(input("enter your choice:="))
                if experience==1:
                    days=int(input("enter expirence in days:="))
                    experience= days * 0.032855 
                elif experience==2:
                    experience=int(input("enter expirence in months:="))
                elif experience==3:
                    year=int(input("enter experience:="))
                    experience= year * 12 
                sql="insert into teacher(name,mobile,email,gender,qulification,experience)values(%s,%s,%s,%s,%s,%s)"
                values=[name,mobile,email,gender,qulification,experience]
                db.RunQuery(sql,values)
            elif techertable==2:
                vi.displaytecher()
                id=int(input("enter a id:= "))
                name=input("enter techer name:=")
                mobile=int(input("enter teacher mobileno:="))
                email=(input("enter teacher email"))
                gender=int(input("if teacher is male press'0' and female for press '1':="))
                qulification=(input("press your qulification ex:m.c.a,b.c.a :="))
                print("press 1 for a experience in days 2 for months and 3 for years:=")
                experience=int(input("enter your choice:="))
                if experience==1:
                    days=int(input("enter expirence in days:="))
                    experience= days * 0.032855 
                elif experience==2:
                    experience=int(input("enter expirence in months:="))
                elif experience==3:
                    year=int(input("enter experience:="))
                    experience= year * 12 
                sql="update teacher set name=%s,mobile=%s,email=%s,gender=%s,qulification=%s,experience=%s where id=%s "
                values=[name,mobile,email,gender,qulification,experience,id]
                db.RunQuery(sql,values)
            elif techertable==3:
                vi.displaytecher()
                id=int(input("enter id you delete teacher:= "))
                sql="update teacher set isdeleted=%s where id=%s"
                values=[1,id]
                db.RunQuery(sql,values)
            elif techertable==4:
                #this field is use for view table 
                vi.displaycourse()
            elif techertable==0:
                print("exit course table")
                break
            else:
                print("invalid input")
    elif Coachingclass==5:
        print("*******you enter a lecture table*******")
        print("-"*100)
        print("press 1 for insert value in lacture table")
        print("-"*100)
        print("press 2 for selct and display lecture table")
        print("-"*100)
        print("press 0 for exit lecture table")
        print("-"*100)
        lacturetable=int(input("enter your choice:="))
        if lacturetable==1:
            vi.displaytecher()
            teacherid=int(input("enter a assign teacherid:="))
            vi.displaysubject()
            subjectid=int(input("enter a assign subjectid:="))
            vi.displaybatch()
            batchid=int(input("enter a assign batchid:="))
            duration=int(input("enter a assign duration:="))
            amount=int(input("enter a assign amount:="))
            print("press 1 for manully enter date press 2 for auto gunrate current date time")
            lecturedate=int(input("enter your choice:="))
            if lecturedate==1:
                day = int(input("Enter start lectureday"))
                month = int(input("Enter start lecturemonth"))
                year = int(input("Enter start lectureyear"))
                lecturedate = datetime(year,month,day)
                print(lecturedate)
            elif lecturedate==2:
                lecturedate = datetime.now()
            sql="insert into  lecture (teacherid,subjectid,batchid,duration,amount,lecturedate)values(%s,%s,%s,%s,%s,%s)"
            values=[teacherid,subjectid,batchid,duration,amount,lecturedate]
            db.RunQuery(sql,values)
        elif lacturetable==2:
            vi.displaylecture()
    elif Coachingclass==6:
        # payout management
        # generate of specific teacher between given date
        vi.displaylecture()
        print("Enter start date and time")
        day = int(input("Enter start day"))
        month = int(input("Enter start month"))
        year = int(input("Enter start year"))
        lecturestartdate = datetime(year,month,day)
        print("Enter end date and time")
        day = int(input("Enter end day"))   
        month = int(input("Enter end month"))
        year = int(input("Enter end year"))
        lectureenddate = datetime(year,month,day)
        sql='''select t.id,name from teacher t,lecture l where teacherid=t.id and lecturedate>=%s and lecturedate<=%s '''
        values=[lecturestartdate,lectureenddate]
        table=db.FetchRow(sql,values)
        print(f''''id' {'':3}{'name'}''')
        for row in table:
            print(f"{'':1}{row['id']}{'':6}{row['name']}")

    elif Coachingclass==7:
        # generate batch wise lecture detail between given date
        vi.displaylecture()
        print("Enter start date and time")
        day = int(input("Enter start day"))
        month = int(input("Enter start month"))
        year = int(input("Enter start year"))
        lecturestartdate = datetime(year,month,day)
        print("Enter end date and time")
        day = int(input("Enter end day"))   
        month = int(input("Enter end month"))
        year = int(input("Enter end year"))
        lectureenddate = datetime(year,month,day)
        sql='''select l.id,teacherid,subjectid,batchid,duration,amount,lecturedate from lecture l,batch b where batchid=b.id and lecturedate>=%s and lecturedate<=%s  '''
        values=[lecturestartdate,lectureenddate]
        table=db.FetchRow(sql,values)
        print(f''' 'id'{'':4}{'teacherid ':12}{'':1}{'subjectid':10}{'':3}{'lecturedate':11}{'':6}{'batchid':11}{'amount':10}{'duration':12}''')
        for row in table:
            lecturedate = row['lecturedate'].strftime("%d-%m-%Y")
            print(f'''{'':2}{row['id']}{row['teacherid']:10}{'':6}{row['subjectid']:8}{'':8}{lecturedate:2}{'':10}{row['batchid']}{row['amount']:12}{'':8}{row['duration']:3}''')
    elif Coachingclass==8:
        # generate batch wise lecture detail with total amount
        sql="select l.id,teacherid,subjectid,batchid,duration,amount,lecturedate from batch b,lecture l where batchid=b.id "
        table=db.FetchRow(sql)
        amount=0
        print(f''' 'id'{'':4}{'teacherid ':12}{'':1}{'subjectid':10}{'':3}{'lecturedate':11}{'':6}{'batchid':11}{'amount':10}{'duration':12}''')
        for row in table:
                print('-'*100)
                lecturedate = row['lecturedate'].strftime("%d-%m-%Y")
                print(f'''{'':2}{row['id']}{row['teacherid']:10}{'':6}{row['subjectid']:8}{'':8}{lecturedate:2}{'':10}{row['batchid']}{row['amount']:12}{'':8}{row['duration']:3}''')
                amount= row['amount']+amount
                print('-'*100)
        print('-'*100)
        print(f"Totalamount = {amount:54}")
    elif Coachingclass==0:
        print("thanks for coming")
        break
    else:
        print("invalid input")
