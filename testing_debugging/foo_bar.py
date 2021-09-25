my_value = 'foo bar'

# All these are equivalent
print(str(my_value))
print('%s' % my_value)
print(f'{my_value}')
print(format(my_value))
print(my_value.__format__('s'))
print(my_value.__str__())

# Distingush 5 and '5' is hard with print
print(5)
print('5')

int_value = 5
str_value = '5'
print(f'{int_value} == {str_value} ?')

# Using repr while debugging
a = '\x07'
print(a)
print(repr(a))

b = eval(repr(a))
assert a == b

# When debugging with print call repr on the value:
print('\nCalling repr on values:')
print(repr(5))
print(repr('5'))

# equivalent of using %r
print('%r' % 5)
print('%r' % '5')

# Or an f-string with the !r type conversion:
int_value = 5
str_value = '5'
print(f'{int_value!r} != {str_value!r}')


