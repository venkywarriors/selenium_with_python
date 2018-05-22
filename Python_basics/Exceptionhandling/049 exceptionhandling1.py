"""
Exceptions are errors
We should handle exceptions in our code
to make sure the code is working the way we want and is handling all the unwanted issues
Link to 3.5 built-in exceptions - https://docs.python.org/3/library/exceptions.html
"""

def exceptionHandling():
    try:
        a = 10
        b = 20
        c = 0

        d = (a + b) / c
        print(d)
    # except ZeroDivisionError:
    #     print("Zero Division")
    # except TypeError:
    #     print("Can't add string to integer")
    except:
        print("In the except block")

exceptionHandling()