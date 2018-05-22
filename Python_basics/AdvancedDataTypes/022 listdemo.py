"""
Data type to store more than one value in one variable name
List items are in brackets, separated with "," [ 1, 2, 3 ]
"""

cars = [ "bmw", "honda", "audi"]
empty_list = []
print(empty_list)
print(cars)

print("*#"*20)

print(cars[1])

num_list = [1, 2, 3]
sum_num = num_list[0] + num_list[1]

print(sum_num)

more_cars = [ "bmw", "honda", "audi"]
print(more_cars[1])

more_cars[1] = "Benz"

print(more_cars[1])
print(more_cars)