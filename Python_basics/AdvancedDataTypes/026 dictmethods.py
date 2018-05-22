"""
Dictionary Methods
"""

car = {'make': 'bmw', 'model': '550i', 'year': 2016}
cars = {'bmw': {'model': '550i', 'year': 2016}, 'benz': {'model': 'E350', 'year': 2015}}

print(car.keys())
print(cars.keys())
print(car.values())
print(cars.values())
print(car.items())

car_copy = car.copy()
print(car_copy)

print(car.pop('model'))
print(car)