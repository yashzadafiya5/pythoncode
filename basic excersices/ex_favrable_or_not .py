'''
    13) Write a program to accept male and female person birth day and month separately and calculate the compatibility fand relationship using following criteria

'''


male_birthday=int(input("enter your male_birthday"))
male_birthmonth=int(input("enter your male_birthmonth"))

female_birthday=int(input("enter your female_birthday"))
female_birthmonth=int(input("enter your female_birthmonth"))

male_zodic_sign=' '
if (male_birthday>=21  and male_birthmonth==3) or (male_birthday<=19 and male_birthmonth==4):
    print("your zodic sign is  'aries' and your zodic symbole is 'The ram' ",male_zodic_sign)
male_zodic_sign='aries'
if (male_birthday>=20  and male_birthmonth==4) or (male_birthday<=20 and male_birthmonth==5):
    print("your zodic sign is  'Taurus' and your zodic symbole is 'The Bull' ",male_zodic_sign)
male_zodic_sign='Taurus'
if (male_birthday>=21  and male_birthmonth==5) or (male_birthday<=20 and male_birthmonth==6):
    print("your zodic sign is  'Gemini' and your zodic symbole is 'The Twins' ",male_zodic_sign)
male_zodic_sign= 'Gemini'
if (male_birthday>=21  and male_birthmonth==6) or (male_birthday<=22 and male_birthmonth==7):
    print("your zodic sign is 'Cancer' and your zodic symbole is 'The Crab' ",male_zodic_sign)
male_zodic_sign='Cancer'
if (male_birthday>=23  and male_birthmonth==7) or (male_birthday<=22 and male_birthmonth==8):
    print("your zodic sign is 'Leo' and your zodic symbole is 'The Lion' ",male_zodic_sign)
male_zodic_sign='Virgo'
if (male_birthday>=23  and male_birthmonth==8) or (male_birthday<=22 and male_birthmonth==9):
    print("your zodic sign is 'Virgo' aries and your zodic symbole is 'The Virgin ' ",male_zodic_sign)
male_zodic_sign='Libra'
if (male_birthday>=21  and male_birthmonth==9) or (male_birthday<=19 and male_birthmonth==10):
    print("your zodic sign is 'Libra' and your zodic symbole is 'The Scales' ",male_zodic_sign)
male_zodic_sign='Scandpio'
if (male_birthday>=21  and male_birthmonth==10) or (male_birthday<=19 and male_birthmonth==11):
    print("your zodic sign is 'Scandpio'  and your zodic symbole is 'The Scandpion' ",male_zodic_sign)
male_zodic_sign='Sagittarius'
if (male_birthday>=21  and male_birthmonth==11) or (male_birthday<=19 and male_birthmonth==12):
    print("your zodic sign is 'Sagittarius'  and your zodic symbole is 'The Archer' ",male_zodic_sign)
male_zodic_sign='Capricandn'
if (male_birthday>=21  and male_birthmonth==12) or (male_birthday<=19 and male_birthmonth==1):
    print("your zodic sign is 'Capricandn'  and your zodic symbole is The 'Goat' ",male_zodic_sign)
male_zodic_sign='Aquarius'
if (male_birthday>=21  and male_birthmonth==1) or (male_birthday<=19 and male_birthmonth==2):
    print("your zodic sign is 'Aquarius'  and your zodic symbole is 'The water Bearer' ",male_zodic_sign)
male_zodic_sign='Pisces'
if (male_birthday>=21  and male_birthmonth==2) or (male_birthday<=19 and male_birthmonth==3):
    print("your zodic sign is 'Pisces' and your zodic symbole is 'The Fishes' ",male_zodic_sign)
female_zodic_sign=' '
if (female_birthday>=21  and female_birthmonth==3) or (female_birthday<=19 and female_birthmonth==4):
    print("your zodic sign is  'aries' and your zodic symbole is 'The ram' ",female_zodic_sign)
female_zodic_sign='aries'
if (female_birthday>=20  and female_birthmonth==4) or (female_birthday<=20 and female_birthmonth==5):
    print("your zodic sign is  'Taurus' and your zodic symbole is 'The Bull' ",female_zodic_sign)
female_zodic_sign='Taurus'
if (female_birthday>=21  and female_birthmonth==5) or (female_birthday<=20 and female_birthmonth==6):
    print("your zodic sign is  'Gemini' and your zodic symbole is 'The Twins' ",female_zodic_sign)
female_zodic_sign= 'Gemini'
if (female_birthday>=21  and female_birthmonth==6) or (female_birthday<=22 and female_birthmonth==7):
    print("your zodic sign is 'Cancer' and your zodic symbole is 'The Crab' ",female_zodic_sign)
female_zodic_sign='Cancer'
if (female_birthday>=23  and female_birthmonth==7) or (female_birthday<=22 and female_birthmonth==8):
    print("your zodic sign is 'Leo' and your zodic symbole is 'The Lion' ",female_zodic_sign)
female_zodic_sign='Virgo'
if (female_birthday>=23  and female_birthmonth==8) or (female_birthday<=22 and female_birthmonth==9):
    print("your zodic sign is 'Virgo' aries and your zodic symbole is 'The Virgin ' ",female_zodic_sign)
female_zodic_sign='Libra'
if (female_birthday>=21  and female_birthmonth==9) or (female_birthday<=19 and female_birthmonth==10):
    print("your zodic sign is 'Libra' and your zodic symbole is 'The Scales' ",female_zodic_sign)
female_zodic_sign='Scandpio'
if (female_birthday>=21  and female_birthmonth==10) or (female_birthday<=19 and female_birthmonth==11):
    print("your zodic sign is 'Scandpio'  and your zodic symbole is 'The Scandpion' ",female_zodic_sign)
female_zodic_sign='Sagittarius'
if (female_birthday>=21  and female_birthmonth==11) or (female_birthday<=19 and female_birthmonth==12):
    print("your zodic sign is 'Sagittarius'  and your zodic symbole is 'The Archer' ",female_zodic_sign)
female_zodic_sign='Capricandn'
if (female_birthday>=21  and female_birthmonth==12) or (female_birthday<=19 and female_birthmonth==1):
    print("your zodic sign is 'Capricandn'  and your zodic symbole is The 'Goat' ",female_zodic_sign)
female_zodic_sign='Aquarius'
if (female_birthday>=21  and female_birthmonth==1) or (female_birthday<=19 and female_birthmonth==2):
    print("your zodic sign is 'Aquarius'  and your zodic symbole is 'The water Bearer' ",female_zodic_sign)
female_zodic_sign='Pisces'
if (female_birthday>=21  and female_birthmonth==2) or (female_birthday<=19 and female_birthmonth==3):
    print("your zodic sign is 'Pisces' and your zodic symbole is 'The Fishes' ",female_zodic_sign)


result=''
if male_zodic_sign=='aries' and female_zodic_sign=='aries':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='aries' and female_zodic_sign=='Taurus':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='aries' and female_zodic_sign=='Gemini':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='aries' and female_zodic_sign=='Cancer':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='aries' and female_zodic_sign=='Leo':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='aries' and female_zodic_sign=='Virgo':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='aries' and female_zodic_sign=='Libra':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='aries' and female_zodic_sign=='Scandpio':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='aries' and female_zodic_sign=='Sagittarius':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='aries' and female_zodic_sign=='Capricandn':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='aries' and female_zodic_sign=='Aquarius':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='aries' and female_zodic_sign=='Pisces':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
result=''
if male_zodic_sign=='Taurus' and female_zodic_sign=='aries':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Taurus' and female_zodic_sign=='Taurus':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Taurus' and female_zodic_sign=='Gemini':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Taurus' and female_zodic_sign=='Cancer':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Taurus' and female_zodic_sign=='Leo':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='Taurus' and female_zodic_sign=='Virgo':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Taurus' and female_zodic_sign=='Libra':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Taurus' and female_zodic_sign=='Scandpio':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Taurus' and female_zodic_sign=='Sagittarius':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Taurus' and female_zodic_sign=='Capricandn':
    result='favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Taurus' and female_zodic_sign=='Aquarius':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='Taurus' and female_zodic_sign=='Pisces':
    result='favandable'
    print("shouid be an excellent love match",result)
result=''
if male_zodic_sign=='Gemini' and female_zodic_sign=='aries':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Gemini' and female_zodic_sign=='Taurus':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Gemini' and female_zodic_sign=='Gemini':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Gemini' and female_zodic_sign=='Cancer':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Gemini' and female_zodic_sign=='Leo':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Gemini' and female_zodic_sign=='Virgo':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='Gemini' and female_zodic_sign=='Libra':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Gemini' and female_zodic_sign=='Scandpio':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Gemini' and female_zodic_sign=='Sagittarius':
    result='favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Gemini' and female_zodic_sign=='Capricandn':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Gemini' and female_zodic_sign=='Aquarius':
    result='favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Gemini' and female_zodic_sign=='Pisces':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
result=''
if male_zodic_sign=='Cancer' and female_zodic_sign=='aries':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='Cancer' and female_zodic_sign=='Taurus':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Cancer' and female_zodic_sign=='Gimini':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Cancer' and female_zodic_sign=='Cancer':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Cancer' and female_zodic_sign=='Leo':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Cancer' and female_zodic_sign=='Virgo':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Cancer' and female_zodic_sign=='Libra':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='Cancer' and female_zodic_sign=='Scandpio':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Cancer' and female_zodic_sign=='Sagittarius':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Cancer' and female_zodic_sign=='Capricandn':
    result='favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Cancer' and female_zodic_sign=='Aquarius':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Cancer' and female_zodic_sign=='Pisces':
    result='favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
result=''
if male_zodic_sign=='Leo' and female_zodic_sign=='aries':
    result='favandable'
    print("favandablejodi",result)
elif male_zodic_sign=='Leo' and female_zodic_sign=='Taurus':
    result='critical'
    print("your jodi is critical")
elif male_zodic_sign=='Leo' and female_zodic_sign=='Gimini':
    result='favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Leo' and female_zodic_sign=='cancer':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Leo' and female_zodic_sign=='Leo':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Leo' and female_zodic_sign=='Virgo':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Leo' and female_zodic_sign=='Libra':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Leo' and female_zodic_sign=='Scandpio':
    result='critical'
    print("your jodi is critical")
elif male_zodic_sign=='Leo' and female_zodic_sign=='Sagittarius':
    result='favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Leo' and female_zodic_sign=='Capricandn':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Leo' and female_zodic_sign=='Aquarius':
    result='favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Leo' and female_zodic_sign=='Pisces':
    result='critical'
    print("your jodi is critical")
result=''
if male_zodic_sign=='virgo' and female_zodic_sign=='aries':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='virgo' and female_zodic_sign=='Taurus':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='virgo' and female_zodic_sign=='Gimini':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='virgo' and female_zodic_sign=='cancer':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='virgo' and female_zodic_sign=='Leo':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='virgo' and female_zodic_sign=='Virgo':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='virgo' and female_zodic_sign=='Libra':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='virgo' and female_zodic_sign=='Scandpio':
    result='favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='virgo' and female_zodic_sign=='Sagittarius':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='virgo' and female_zodic_sign=='Capricandn':
    result='favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='virgo' and female_zodic_sign=='Aquarius':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='virgo' and female_zodic_sign=='Pisces':
    result='favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
result=''
if male_zodic_sign=='Libra' and female_zodic_sign=='aries':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Libra' and female_zodic_sign=='Taurus':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Libra' and female_zodic_sign=='Gimini':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Libra' and female_zodic_sign=='cancer':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='Libra' and female_zodic_sign=='Leo':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Libra' and female_zodic_sign=='virgo':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Libra' and female_zodic_sign=='Libra':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Libra' and female_zodic_sign=='Scandpio':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Libra' and female_zodic_sign=='Sagittarius':
    result='favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Libra' and female_zodic_sign=='Capricandn':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='Libra' and female_zodic_sign=='Aquarius':
    result='favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Libra' and female_zodic_sign=='Pisces':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
result=''
if male_zodic_sign=='Scandpio' and female_zodic_sign=='aries':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Scandpio' and female_zodic_sign=='Taurus':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Scandpio' and female_zodic_sign=='Gimini':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Scandpio' and female_zodic_sign=='cancer':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Scandpio' and female_zodic_sign=='Leo':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='Scandpio' and female_zodic_sign=='virgo':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Scandpio' and female_zodic_sign=='Lio':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Scandpio' and female_zodic_sign=='Scandpio':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Scandpio' and female_zodic_sign=='Sagittarius':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Scandpio' and female_zodic_sign=='Capricandn':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Scandpio' and female_zodic_sign=='Aquarius':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='Scandpio' and female_zodic_sign=='Pisces':
    result='favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
result=''
if male_zodic_sign=='Sagittarius' and female_zodic_sign=='aries':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Sagittarius' and female_zodic_sign=='Taurus':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Sagittarius' and female_zodic_sign=='Gimini':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Sagittarius' and female_zodic_sign=='cancer':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Sagittarius' and female_zodic_sign=='Leo':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Sagittarius' and female_zodic_sign=='virgo':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='Sagittarius' and female_zodic_sign=='Lio':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Sagittarius' and female_zodic_sign=='Scandpio':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Sagittarius' and female_zodic_sign=='Sagittarius':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Sagittarius' and female_zodic_sign=='Capricandn':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Sagittarius' and female_zodic_sign=='Aquarius':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Sagittarius' and female_zodic_sign=='Pisces':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
    
result=''
if male_zodic_sign=='Capricandn' and female_zodic_sign=='aries':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='Capricandn' and female_zodic_sign=='Taurus':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Capricandn' and female_zodic_sign=='Gimini':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='Capricandn' and female_zodic_sign=='cancer':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Capricandn' and female_zodic_sign=='Leo':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='Capricandn' and female_zodic_sign=='virgo':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Capricandn' and female_zodic_sign=='Lio':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='Capricandn' and female_zodic_sign=='Scandpio':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Capricandn' and female_zodic_sign=='Sagittarius':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='Capricandn' and female_zodic_sign=='Capricandn':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Capricandn' and female_zodic_sign=='Aquarius':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='Capricandn' and female_zodic_sign=='Pisces':
    result='favandable'
    print("shouid be an excellent love match",result)
if male_zodic_sign=='Aquarius' and female_zodic_sign=='aries':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Aquarius' and female_zodic_sign=='Taurus':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='Aquarius' and female_zodic_sign=='Gimini':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Aquarius' and female_zodic_sign=='cancer':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Aquarius' and female_zodic_sign=='Leo':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Aquarius' and female_zodic_sign=='virgo':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Aquarius' and female_zodic_sign=='Lio':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Aquarius' and female_zodic_sign=='Scandpio':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='Aquarius' and female_zodic_sign=='Sagittarius':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Aquarius' and female_zodic_sign=='Capricandn':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Aquarius' and female_zodic_sign=='Aquarius':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Aquarius' and female_zodic_sign=='Pisces':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
result=''
if male_zodic_sign=='Pisces' and female_zodic_sign=='aries':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Pisces' and female_zodic_sign=='Taurus':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Pisces' and female_zodic_sign=='Gimini':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='Pisces' and female_zodic_sign=='cancer':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Pisces' and female_zodic_sign=='Leo':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Pisces' and female_zodic_sign=='virgo':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Pisces' and female_zodic_sign=='Lio':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Pisces' and female_zodic_sign=='Scandpio':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Pisces' and female_zodic_sign=='Sagittarius':
    result='critical'
    print("can be hard to make this relationship progress smothly",result)
elif male_zodic_sign=='Pisces' and female_zodic_sign=='Capricandn':
    result='favandable'
    print("shouid be an excellent love match",result)
elif male_zodic_sign=='Pisces' and female_zodic_sign=='Aquarius':
    result=' less favandable'
    print("maybe good, but both of you need to continue to wandk on relationship",result)
elif male_zodic_sign=='Pisces' and female_zodic_sign=='Pisces':
    result='favandable'
    print("shouid be an excellent love match",result)
else:
        print("maybe good, but both of you need to continue to wandk on relationship ",result)

