'''
Created on 01-Jul-2020

@author: venkateshwara D
'''

from random import randint


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

print (random_with_N_digits(2))
print (random_with_N_digits(3))
print (random_with_N_digits(4))
