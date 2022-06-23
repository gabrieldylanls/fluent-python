#Example 2-5. Initializing a tuple and an array from a generator expression.
import array

symbols = '$%#&*'
print(tuple(ord(s) for s in symbols))

print(array.array('I', (ord(s) for s in symbols)))
