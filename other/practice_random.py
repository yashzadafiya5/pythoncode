import random
import datetime
new=random.random()
print(new)

print('givin a random number by using a range',random.randint(1,10))
print('givin a random number by using a range',random.randrange(1,100,6))
print('givin a random number by using a range',random.uniform(1,10))

lists=['yash','bhavdeep','param','kausik',12.15,15.5]
gen=random.choice(lists)
gen=random.choices(lists,k=2)
print(gen)




