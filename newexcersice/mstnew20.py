# 20. Creating Dummy Data using Python 

import pandas as pd
import random
from faker import Faker
from random import randrange
from datetime import datetime

nr_of_customers = 1000
fake = Faker('de_DE')
customers = []
for customers_id in range(1,nr_of_customers+1):
    d1 = datetime.strptime(f'1/1/2021', '%m/%d/%Y')
    d2 = datetime.strptime(f'8/10/2021', '%m/%d/%Y')
    transaction_date = fake.date_between(d1, d2)
    name = fake.name()
    gender = random.choice(["M", "F"])
    email = fake.ascii_email()
    city = fake.city()
    product_ID = fake.ean(length=8)
    amount_spent = fake.pyfloat(right_digits=2, positive=True, min_value=1, max_value=100)
    customers.append([transaction_date, name, gender, email, city, product_ID, amount_spent])
customers_df = pd.DataFrame(customers, columns=['Transaction_date','Name', 'Gender','Email', 'City','Product_id', 'Amount_spent'])       
print(customers_df)