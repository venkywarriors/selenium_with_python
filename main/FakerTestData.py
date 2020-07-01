'''
Created on 01-Jul-2020

@author: venkateshwara D
'''
from faker import Faker
fake = Faker()


for x in range(0,5):
    print(fake.name())
    print(fake.address())