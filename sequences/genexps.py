#Example 2-5. Initializing a tuple and an array from a generator expression.
import array

symbols = '$%#&*'
print(tuple(ord(s) for s in symbols))

print(array.array('I', (ord(s) for s in symbols)))

#Example 2-6. Cartesian product in a generator expression.
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)
