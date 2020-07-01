'''
Created on 01-Jul-2020

@author: venkateshwara D
'''
import string 
import random 


'''The random.choices() method returns a list with the randomly selected element from the specified sequence.

You can weigh the possibility of each result with the weights parameter or the cum_weights parameter.

The sequence can be a string, a range, a list, a tuple or any other kind of sequence.

Syntax
random.choices(sequence, weights=None, cum_weights=None, k=1)'''

def random_AlphaPrefix(N):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
    return res

def random_Characters(N):
    res = ''.join(random.choices(string.ascii_letters, k = N))
    return res

# print result 
print("The generated random alpha string : " + random_AlphaPrefix(8))
print("The generated random string : " + random_Characters(8))