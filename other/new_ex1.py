#find user enter a date and this date is what zodic sign and this zodic sign is and horoscope is find out
from bs4 import BeautifulSoup
from urllib.request import urlopen


new=[]
date=int(input("enter your date"))
month=int(input("enter your month"))

zodic_sign=''
if (date>=21  and month==3) or (date<=19 and month==4):
    print("your zodic sign is  'aries' and your zodic symbole is 'The ram' ",zodic_sign)
    zodic_sign='aries'
    new.append(zodic_sign)
    listToStr = ' '.join([str(elem) for elem in new])
if (date>=20  and month==4) or (date<=20 and month==5):
    print("your zodic sign is  'Taurus' and your zodic symbole is 'The Bull' ",zodic_sign)
    zodic_sign='Taurus'
    new.append(zodic_sign)
    listToStr = ' '.join([str(elem) for elem in new])
if (date>=21  and month==5) or (date<=20 and month==6):
    print("your zodic sign is  'Gemini' and your zodic symbole is 'The Twins' ",zodic_sign)
    zodic_sign='gemini'
    new.append(zodic_sign)
    listToStr = ' '.join([str(elem) for elem in new])
if (date>=21  and month==6) or (date<=22 and month==7):
    print("your zodic sign is 'Cancer' and your zodic symbole is 'The Crab' ",zodic_sign)
    zodic_sign='cancer'
    new.append(zodic_sign)
    listToStr = ' '.join([str(elem) for elem in new])
if (date>=23  and month==7) or (date<=22 and month==8):
    print("your zodic sign is 'Leo' and your zodic symbole is 'The Lion' ",zodic_sign)
    zodic_sign='leo'
    new.append(zodic_sign)
    listToStr = ' '.join([str(elem) for elem in new])
if (date>=23  and month==8) or (date<=22 and month==9):
    print("your zodic sign is 'Virgo' aries and your zodic symbole is 'The Virgin ' ",zodic_sign)
    zodic_sign='virgo'
    new.append(zodic_sign)
    listToStr = ' '.join([str(elem) for elem in new])
if (date>=21  and month==9) or (date<=19 and month==10):
    print("your zodic sign is 'Libra' and your zodic symbole is 'The Scales' ",zodic_sign)
    zodic_sign='libra'
    new.append(zodic_sign)
    listToStr = ' '.join([str(elem) for elem in new])
if (date>=21  and month==10) or (date<=19 and month==11):
    print("your zodic sign is 'Scandpio'  and your zodic symbole is 'The Scandpion' ",zodic_sign)
    zodic_sign='scorpio'
    new.append(zodic_sign)
    listToStr = ' '.join([str(elem) for elem in new])
if (date>=21  and month==11) or (date<=19 and month==12):
    print("your zodic sign is 'Sagittarius'  and your zodic symbole is 'The Archer' ",zodic_sign)
    zodic_sign='sagittarius'
    new.append(zodic_sign)
    listToStr = ' '.join([str(elem) for elem in new])
if (date>=21  and month==12) or (date<=19 and month==1):
    print("your zodic sign is 'Capricandn'  and your zodic symbole is The 'Goat' ",zodic_sign)
    zodic_sign='capricorn'
    new.append(zodic_sign)
    listToStr = ' '.join([str(elem) for elem in new])
if (date>=21  and month==1) or (date<=19 and month==2):
    print("your zodic sign is 'Aquarius'  and your zodic symbole is 'The water Bearer' ",zodic_sign)
    zodic_sign='aquarius'
    new.append(zodic_sign)
    listToStr = ' '.join([str(elem) for elem in new])
if (date>=21  and month==2) or (date<=19 and month==3):
    print("your zodic sign is 'Pisces' and your zodic symbole is 'The Fishes' ",zodic_sign)
    zodic_sign='pisces'
    new.append(zodic_sign)
    listToStr = ' '.join([str(elem) for elem in new])
    
print(listToStr)
url = f"https://www.prokerala.com/astrology/horoscope/?sign={listToStr}"

file=urlopen(url)
html= file.read()

soup=BeautifulSoup(html,'html.parser')

print(soup.body.find("article").get_text())
