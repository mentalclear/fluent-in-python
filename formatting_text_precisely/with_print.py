a = 25
b = 75
c = 100

# Problematic output
print(a, ' plus ', b, ' equals ', c, '.')

# Ugly solution
print(a, ' plus ', b, ' equals ', c, '.', sep='')

# With % formatting operator
print('%d plus %d equals %d.' % (a, b, c,))

# Syntax
# format_str % value        # Single value
# format_str % (values)     # One or more values

# Another working example
tup = 10, 20, 30
print('Answers are %d, %d and %d' % tup)

# Syntax:
# %[-][width][.precision]c
print('This is a number: %-6d.' % 255)
print('My name is %10s.' % 'John')

# The Global “format” Function

big_n = 10 ** 12
print(format(big_n, ','))

# Syntax
# format(data, spec)


# the “format” Method
print('{} plus {} equals {}.'.format(a, b, c))

# also works
fss = '{} said, I want {} slices of {}.'

name = 'Pythagoras'
pi = 3.141592
print(fss.format(name, 2, pi))

print('Set = {{ {}, {}, {} }}'.format(15, 35, 25))

# Ordering by position
# { [position] [!r|s|a] [: spec ] }
print('{}; {}; {}!'.format(10, 20, 30))

# but also:
print('The items are {2}, {1}, {0}.'.format(10, 20, 30))

# and
fss = 'The items are {3}, {1}, {0}.'
print(fss.format(10, 20, 30, 40))

# also
print('{0}, {0}, {1}, {1}'.format(100, 200))

# Repr vs String
print(10)       # Prints 10
print(str(10))  # Prints 10

print(repr(10)) # ALSO Prints 10

test_str = 'Here is a \n newline! '
print(test_str)

print(repr(test_str))

print('{}'.format(test_str))

print('{!r}'.format(test_str))
