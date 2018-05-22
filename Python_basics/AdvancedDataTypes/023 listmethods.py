"""
Built-in methods to help manipulating a list
"""

cars = [ "bmw", "honda", "audi"]

length = len(cars)
print(length)

cars.append("Benz")
print(cars)

cars.insert(1, "Jeep")
print(cars)

x = cars.index("honda")
print(x)

y = cars.pop()
print(y)
print(cars)

cars.remove("Jeep")
print(cars)

slicing = cars[0:2]
a = cars[1:]
print(slicing)
print(a)

print("*#"*20)
print(cars)
cars.sort()

print(cars)