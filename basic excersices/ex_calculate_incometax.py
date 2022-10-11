'''
    +11) Write a Python program to calculate income tax, gross income, net income from monthly income given by user 

yearly income     tax rate
<3,00,000         5%  

>=3,00,000
<5,00,000         10%  

>=5,00,000
<8,00,000         20%

>=8,00,000        30%  

'''
monthly=int(input("enter youe monthly income = "))
gross_income=monthly*12
print("your monthly income is = ",gross_income)
if gross_income<300000:
    tax_rate=(gross_income*5)/100
    print("your income tax ",tax_rate)
elif gross_income>=300000 and gross_income<500000:
    tax_rate=(gross_income*10)/100
    print("your income tax ",tax_rate)
elif gross_income>=500000 and gross_income<800000:
    tax_rate=(gross_income*20)/100
    print("your income tax ",tax_rate)
elif  gross_income>=800000:
    tax_rate=(gross_income*30)/100
    print("your income tax ",tax_rate)
    