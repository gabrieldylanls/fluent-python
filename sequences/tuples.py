#Example 2-7. Tuples used as records.
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'CE342567')]

for passport in sorted(traveler_ids):
    print(f'{passport[0]}/{passport[1]}')

for country, _ in traveler_ids:
    print(country)

#Examples of tuple unpacking
latitude, longitude = lax_coordinates
print('Latitude', latitude)
print('Longitude', longitude)

a = 1
b = 2

b, a = a, b

print('a', a)
print('b', b)

t = (20, 8)
print(divmod(*t))

quotient, remainder = divmod(*t)
print('Quotient', quotient)
print('Remainder', remainder)

import os
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print('Filename', filename)

a, b, *rest = range(5)
print((a, b, rest))
a, b, *rest = range(3)
print((a, b, rest))
a, b, *rest = range(2)
print((a, b, rest))
a, *body, c, d = range(5)
print((a, body, c, d))
*head, b, c, d = range(5)
print((head, b, c, d))