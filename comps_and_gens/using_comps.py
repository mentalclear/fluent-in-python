a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []
for x in a:
    squares.append(x**2)
print(squares)

# list comps ver
squares_comp = [ x ** 2 for x in a]
print(squares_comp)

# Map and lambda
alt = map(lambda x: x ** 2, a)

# even squares:
even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)

#Example with map and filter
alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
assert even_squares == list(alt)

# Set comps and Dict comps
even_squares_dict = {x: x**2 for x in a if x % 2 == 0}
threes_cubed_set = {x**3 for x in a if x % 3 == 0}
print(even_squares_dict)
print(threes_cubed_set)

# Example with map and filter
alt_dict = dict(map(lambda x: (x, x**2),
                filter(lambda x: x % 2 == 0, a)))
alt_set = set(map(lambda x: x**3,
              filter(lambda x: x % 3 == 0, a)))

              
