# Example 2-1. Build a list of Unicode codepoints from a string.
symbols = '$!#&*('
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

# Example 2-2. Build a list of Unicode codepoints from a string, take two.
symbols = '$!#&*('
codes = [ord(symbol) for symbol in symbols]
print(codes)

# Example 2-3. The same list built by a listcomp and a map/filter composition.
symbols = '$!#&*('
beyond_ascii = [ord(s) for s in symbols if ord(s) > 35]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 35, map(lambda s: ord(s), symbols)))
print(beyond_ascii)