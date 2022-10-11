quiz = {1:{"question" : "What is the first name of Iron Man?",
            "answer" : "tony"},
         2:{"question" : "Which avenger is green in color?",
             "answer" : "hulk"},
         3:{"question" : "who is smart in easy learn acadamy",
             "answer" : "yash"}}

# for question in quiz:
qutions=1
while qutions<=3:
    print(quiz[qutions]['question']) 
    attempts = 3
    
    while attempts > 0: 
        answer=input('enetr a answer')
        
        if (answer==quiz[qutions]['answer']):
            print('your answer is correct')
            
            break
        else:
            print(f'your ans is wrong {answer}')
        attempts=attempts-1
        
    qutions=qutions+1
    
print(qutions)
print(attempts)