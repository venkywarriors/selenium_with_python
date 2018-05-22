"""
table
object reference count
"""

a="nyc"
b="nyc"

print(a)

a=123

print(a)
print(b)

b=456
print(b)

c='nyc'
d=c

print(c==d)
print(d is c)