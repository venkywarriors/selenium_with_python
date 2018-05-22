"""
A group of code statements which can perform some specific task
Methods are reusable and can be called when needed in the code
"""

def sum_nums(n1, n2):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2

sum1 = sum_nums(2, 8)

sum2 =  sum_nums(3, 3)

string_add = sum_nums('one', 2)
print(string_add)

print(sum1)
print("*************")

def isMetro(city):
    l = ['sfo', 'nyc', 'la']

    if city in l:
        return True
    else:
        return False

x = isMetro('boston')
print(x)