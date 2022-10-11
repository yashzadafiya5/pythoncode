'''
    12) Write a program to display zodiac symbol & given zodiac sign from given birth day and month as per following criteria.
'''

birthdate=int(input("enter your birthdate"))
birthmonth=int(input("enter your birthmonth"))


if (birthdate>=21  and birthmonth==3) or (birthdate<=19 and birthmonth==4):
    print("your zodic sign is  'aries' and your zodic symbole is 'The ram' ")
if (birthdate>=20  and birthmonth==4) or (birthdate<=20 and birthmonth==5):
    print("your zodic sign is  'Taurus' and your zodic symbole is 'The Bull' ")
if (birthdate>=21  and birthmonth==5) or (birthdate<=20 and birthmonth==6):
    print("your zodic sign is  'Gemini' and your zodic symbole is 'The Twins' ")
if (birthdate>=21  and birthmonth==6) or (birthdate<=22 and birthmonth==7):
    print("your zodic sign is 'Cancer' and your zodic symbole is 'The Crab' ")
if (birthdate>=23  and birthmonth==7) or (birthdate<=22 and birthmonth==8):
    print("your zodic sign is 'Leo' and your zodic symbole is 'The Lion' ")
if (birthdate>=23  and birthmonth==8) or (birthdate<=22 and birthmonth==9):
    print("your zodic sign is 'Virgo' aries and your zodic symbole is 'The Virgin ' ")
if (birthdate>=21  and birthmonth==9) or (birthdate<=19 and birthmonth==10):
    print("your zodic sign is 'Libra' and your zodic symbole is 'The Scales' ")
if (birthdate>=21  and birthmonth==10) or (birthdate<=19 and birthmonth==11):
    print("your zodic sign is 'Scandpio'  and your zodic symbole is 'The Scandpion' ")
if (birthdate>=21  and birthmonth==11) or (birthdate<=19 and birthmonth==12):
    print("your zodic sign is 'Sagittarius'  and your zodic symbole is 'The Archer' ")
if (birthdate>=21  and birthmonth==12) or (birthdate<=19 and birthmonth==1):
    print("your zodic sign is 'Capricandn'  and your zodic symbole is The 'Goat' ")
if (birthdate>=21  and birthmonth==1) or (birthdate<=19 and birthmonth==2):
    print("your zodic sign is 'Aquarius'  and your zodic symbole is 'The water Bearer' ")
if (birthdate>=21  and birthmonth==2) or (birthdate<=19 and birthmonth==3):
    print("your zodic sign is 'Pisces' and your zodic symbole is 'The Fishes' ")



