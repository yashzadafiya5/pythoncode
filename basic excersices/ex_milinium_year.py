#7) write a prgoram to findout whether given year is milinium year or not.
year=int(input("enter a year"))
value=year%1000

if  value==0:
    print(value,"this year is milinium year")
else:
    print(value,"this year is not milinium year")