"""
Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are Strings, List, Tuple, Dictionary
"""

x = 0
while x < 10:
    print("Value of x is: " + str(x))
    x = x + 1

l = []
num = 0
while num < 10:
    l.append(num)
    print("Value of num is: " + str(num))
    num += 1

print(l)